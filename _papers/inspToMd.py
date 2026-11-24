#!/usr/bin/env python

import argparse
from dataclasses import dataclass, field
from pathlib import Path
import re
from textwrap import fill
from warnings import warn

import sxs
import yaml
from yaml import Loader

def has_mathml(s: str) -> bool:
    """True if the argument string contains mathml."""
    return "</math>" in s

# For re_delimit_dollars below. (?<!\\) is a negative lookbehind for a
# backslash, because we only want to match dollar signs that do not follow
# backslashes. In real LaTeX this wouldn't actually work because you can have
# line break (double backslash) characters before a $ delimiter. I don't think
# anybody would really do that in practice (especially for inline math), but
# it's technically allowed. We ignore this possibility... and will eventually
# fix the wrong assumption if it ever actually arises.
dollar_math_pat = re.compile(r'(?<!\\)(\$)(.+?)(?<!\\)(\$)', re.DOTALL)

def re_delimit_dollars(s: str) -> str:
    r"""Try to replace $...$ delimited math with \(...\) in abstracts.
    The arXiv allows math delimited with single dollar signs.  However our
    website uses paired delimiters \(...\).  Attempt to replace dollar sign
    delimited groups appropriately.  If the argument string contains mathml
    tags, do nothing.
    """

    if has_mathml(s):
        return s

    # Pattern.sub with count=0 (default) will already replace every occurence
    # for us. The negative lookbehinds are assertions that don't count as
    # capture groups, which is why we want \2 as the content of the math group
    return dollar_math_pat.sub(r'\\(\2\\)', s)

# The format of the markdown file. This would be an f-string, except we want to
# be able to reuse it. To interpolate local variables into it, you can do
# md_format_str.format(**locals())
md_format_str = \
"""---
title: "{title}"
authors:{authors_str}
jref:{jref_str}
doi:{doi_str}
date: {date}
arxiv:{arxiv_str}
insp_recid: {iid}
used_spec:{used_spec_str}
used_spectre:{used_spectre_str}
abstract: |
{abstract_str}
---
"""

@dataclass
class UpdateSummary:
    """Collects what happened while writing INSPIRE records to disk, so that it
    can be reported all at once (e.g. in a PR description) with `to_markdown`.

    `new` and `updated` hold (texkey, description) pairs; `ignored` holds the
    list of texkeys of each ignored record; `problems` holds warning strings;
    `unchanged` counts records whose files were already up to date."""
    new: list = field(default_factory=list)
    updated: list = field(default_factory=list)
    ignored: list = field(default_factory=list)
    problems: list = field(default_factory=list)
    unchanged: int = 0

    def problem(self, msg):
        """Record a problem, and also emit it as a warning."""
        warn(msg)
        self.problems.append(msg)

    def to_markdown(self):
        """Format the summary as markdown, with each category sorted by texkey
        and the ignored papers folded away in a <details> element."""
        def entries(pairs):
            return "\n".join(f"- `{texkey}`: {desc}"
                             for texkey, desc in sorted(pairs))

        sections = ["## Summary of changes"]
        if self.problems:
            sections.append(f"### Problems ({len(self.problems)})\n\n"
                            + "\n".join(f"- {p}" for p in self.problems))
        if self.new:
            sections.append(f"### New papers ({len(self.new)})\n\n"
                            + entries(self.new))
        if self.updated:
            sections.append(f"### Updated papers ({len(self.updated)})\n\n"
                            + entries(self.updated))
        if not (self.problems or self.new or self.updated):
            sections.append("No new or updated papers.")
        if self.unchanged:
            sections.append(f"{self.unchanged} other paper(s) from INSPIRE "
                            "were already up to date.")
        if self.ignored:
            ignored = "\n".join("- " + ", ".join(f"`{k}`" for k in texkeys)
                                for texkeys in sorted(self.ignored))
            sections.append(
                "<details>\n<summary>Ignored papers "
                f"({len(self.ignored)}), found in the papers-to-ignore list"
                f"</summary>\n\n{ignored}\n\n</details>")
        return "\n\n".join(sections) + "\n"

def describe(resp):
    """Short description of an INSPIRE record: title and first author."""
    md = resp['metadata']
    authors = md['authors']
    etal = " et al." if len(authors) > 1 else ""
    return f"\"{md['titles'][0]['title']}\" by {authors[0]['full_name']}{etal}"

def format_jref(pub_infos):
    """Format a journal reference like 'Phys.Rev.D 114, 064077 (2026)' from a
    list of INSPIRE publication_info entries. Uses the first entry that names a
    journal, preferring ones that aren't errata, and only includes the parts
    that are present. Returns '' if no entry names a journal (e.g. the only
    entry is a conference record)."""
    journal_infos = [p for p in pub_infos if p.get('journal_title')]
    if not journal_infos:
        return ''
    p = next((p for p in journal_infos if p.get('material') != 'erratum'),
             journal_infos[0])

    ref = p['journal_title']
    if p.get('journal_volume'):
        ref += f" {p['journal_volume']}"
    # Some journals use article IDs, others page numbers
    page = p.get('artid') or p.get('page_start')
    if page:
        ref += f", {page}"
    if p.get('year'):
        ref += f" ({p['year']})"
    return ref

def insp_resp_to_md(resp, used_spec=None, used_spectre=None):
    """Take a single JSON response from INSPIRE (one element of the list
    returned by `sxs.utilities.inspire.query`) and produce a markdown string to
    be written to a file. The optional arguments `used_spec` and `used_spectre`
    will set the corresponding values in the markdown."""

    iid = resp['id']
    md = resp['metadata']
    if (len(md['texkeys']) > 1):
        warn(f"More than 1 texkeys in {iid}; using first.")
    texkey = md['texkeys'][0]
    if (len(md['titles']) > 1):
        warn(f"More than 1 titles in {iid}; using first.")
    title = md['titles'][0]['title']
    authors = [a['full_name'] for a in md['authors']]
    if len(authors) == 1:
        authors_str = f" \"{authors[0]}\""
    else:
        authors_str = "\n" + "\n".join([f"  - \"{a}\"" for a in authors])
    jref = format_jref(md.get('publication_info', []))
    jref_str = f" \"{jref}\"" if jref else ""
    date = md['earliest_date']
    if 'arxiv_eprints' in md:
        if (len(md['arxiv_eprints']) > 1):
            warn(f"More than 1 arxiv #s in {iid}; using first.")
        arxiv_str = f" \"{md['arxiv_eprints'][0]['value']}\""
    else:
        arxiv_str = ""
    if 'dois' in md:
        if (len(md['dois']) > 1):
            warn(f"More than 1 dois in {iid}; using first.")
        doi_str = f" \"{md['dois'][0]['value']}\""
    else:
        doi_str = ""
    if 'abstracts' in md:
        if (len(md['abstracts']) > 1):
            warn(f"More than 1 abstracts in {iid}; using first.")
        abstract_str = re_delimit_dollars(md['abstracts'][0]['value'])
        abstract_str = fill(abstract_str,
                            initial_indent='  ',
                            subsequent_indent='  ',
                            break_long_words=False)
    else:
        # Somehow there are INSPIRE records without abstracts... emit a warning
        # but continue with empty abstract string.
        warn(f"No abstract for {iid}; using empty string.")
        abstract_str = ''
    used_spec_str = " true" if used_spec else ""
    used_spectre_str = " true" if used_spectre else ""

    return md_format_str.format(**locals())

def write_insp_resp_to_md(responses, summary=None, check_recids=True):
    """Take a JSON response from INSPIRE (e.g. return from
    `sxs.utilities.inspire.query`) and write it to a bunch of .md files.
    Record what was done in `summary` (an UpdateSummary; a new one is made if
    not given), and return it."""

    if summary is None:
        summary = UpdateSummary()

    if check_recids:
        import glob
        from paperStats import loadYamlMD

        paperPaths = glob.glob("*.md")
        yamlMD = loadYamlMD(paperPaths)
        recids = set([ v['insp_recid'] for _, v in yamlMD.items() ])

    for resp in responses:
        md = resp['metadata']
        # If there's no texkey, we don't know what to do
        if 'texkeys' in md and (len(md['texkeys']) > 0):
            texkey = md['texkeys'][0]
        else:
            summary.problem(f"Didn't find a texkey in {resp['id']}; skipping!")
            continue

        # Try to get values of used_spec and used_spectre if something is
        # available on disk
        extra_args = {}
        md_file = Path(f"{texkey}.md")
        if md_file.exists():
            try:
                yamlMD = yaml.load_all(md_file.read_text(),
                                       Loader=Loader).send(None)
                used_keys = {k: yamlMD.get(k)
                             for k in ['used_spec', 'used_spectre']}
                extra_args.update(used_keys)
            except:
                summary.problem(f"Couldn't read `{md_file}` as yaml")

        if check_recids and (resp['id'] in recids):
            if not md_file.exists():
                summary.problem(
                    f"recid {resp['id']} in file OTHER than `{texkey}.md`")

        new_text = insp_resp_to_md(resp, **extra_args)
        if not md_file.exists():
            summary.new.append((texkey, describe(resp)))
        elif md_file.read_text() != new_text:
            summary.updated.append((texkey, describe(resp)))
        else:
            summary.unchanged += 1
            continue
        md_file.write_text(new_text)

    return summary

############################################################

if __name__ == "__main__":
    help = """Query INSPIRE and emit some MD files"""
    parser = argparse.ArgumentParser(
        description=help, formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "query",
        help=(
            "INSPIRE query. Typical queries might be (with the quotes):\n - 'a"
            " Last, First'\n - 't Part of Title'\n - 'texkey"
            " Lovelace:2024wra'\n - 'eprint 2410.00265'\n - 'aff Caltech and a"
            " Last, First'\nSee"
            " https://help.inspirehep.net/knowledge-base/inspire-paper-search/"
            " for more detailed queries."
        ),
    )

    args = parser.parse_args()
    summary = write_insp_resp_to_md(sxs.utilities.inspire.query(args.query))
    print(summary.to_markdown(), end="")
