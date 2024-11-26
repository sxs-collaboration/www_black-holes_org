#!/usr/bin/env python

import argparse

import sxs

from warnings import warn
from textwrap import fill

def write_insp_resp_to_md(responses):
    """Take a JSON response from INSPIRE (e.g. return from
    `sxs.utilities.inspire.query`) and write it to a bunch of .md files"""
    for resp in responses:
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
        arxiv = md['arxiv_eprints'][0]['value']
        if 'dois' in md:
            if (len(md['dois']) > 1):
                warn(f"More than 1 dois in {iid}; using first.")
            doi_str = f" \"{md['dois'][0]['value']}\""
        else:
            doi_str = ""
        if (len(md['abstracts']) > 1):
            warn(f"More than 1 abstracts in {iid}; using first.")
        abstract_str = md['abstracts'][0]['value']
        abstract_str = fill(abstract_str,
                            initial_indent='  ',
                            subsequent_indent='  ')
        with open(f"{texkey}.md", 'w') as f:
            f.write(f"""---
title: "{title}"
authors:{authors_str}
jref:{jref_str}
doi:{doi_str}
date: {date}
arxiv: "{arxiv}"
abstract: |
{abstract_str}
---
""")

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
