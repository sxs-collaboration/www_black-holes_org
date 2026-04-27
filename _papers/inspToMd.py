#!/usr/bin/env python

import argparse
from pathlib import Path
from textwrap import fill
from warnings import warn

import sxs
import yaml
from yaml import Loader

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

def insp_resp_to_md(resp, used_spec=None, used_spectre=None, summarize=True):
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
    if 'publication_info' in md:
        pub_info = md['publication_info']
        if (len(pub_info) > 1):
            warn(f"More than 1 publication_info in {iid}; using first.")
        pub_info = pub_info[0]
        jref_str = f" \"{pub_info.get('journal_title','')} " + \
            f"{pub_info.get('journal_volume','')}, " + \
            f"{pub_info.get('artid','')} ({pub_info.get('year','')})\""
    else:
        jref_str = ""
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
        abstract_str = md['abstracts'][0]['value']
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

    if summarize:
        etal = " et al." if len(authors)>1 else ""
        print(f"- {texkey}: \"{title}\" by {authors[0]}{etal}")

    return md_format_str.format(**locals())

def write_insp_resp_to_md(responses, summarize=True, check_recids=True):
    """Take a JSON response from INSPIRE (e.g. return from
    `sxs.utilities.inspire.query`) and write it to a bunch of .md files"""

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
            warn_str = f"Didn't find a texkey in {resp['id']}; skipping!"
            warn(warn_str)
            if summarize:
                print("- " + warn_str)
            continue

        # Try to get values of used_spec and used_spectre if something is
        # available on disk
        extra_args = {"summarize": summarize}
        md_file = Path(f"{texkey}.md")
        if md_file.exists():
            if summarize:
                print(f"- {texkey}.md found on disk, overwriting")
            try:
                yamlMD = yaml.load_all(md_file.read_text(),
                                       Loader=Loader).send(None)
                used_keys = {k: yamlMD.get(k)
                             for k in ['used_spec', 'used_spectre']}
                extra_args.update(used_keys)
            except:
                warn_str = f"Couldn't read {md_file} as yaml"
                warn(warn_str)
                if summarize:
                    print("- " + warn_str)

        if check_recids and (resp['id'] in recids):
            if not md_file.exists():
                warn_str = f"recid {resp['id']} in file OTHER than {texkey}.md"
                warn(warn_str)
                if summarize:
                    print("- " + warn_str)

        with open(md_file, 'w') as f:
            f.write(insp_resp_to_md(resp, **extra_args))

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
    write_insp_resp_to_md(sxs.utilities.inspire.query(args.query))
