#!/usr/bin/env python

import argparse
from warnings import warn
import yaml
from pathlib import Path
from textwrap import fill
from yaml import Loader

from inspToMd import md_format_str

############################################################

def rewrite_md(bibkey, spec=False, spectre=False, used=True):
    """Parse <bibkey>.md, and rewrite it, setting one of the used_spec or
    used_spectre flags to the value of `used`."""

    if not (spec ^ spectre):
        raise ValueError("rewrite_md requires exactly one of spec or spectre.")

    md_file = Path(f"{bibkey}.md")
    yamlMD = yaml.load_all(md_file.read_text(),
                           Loader=Loader).send(None)

    yamlMD['authors_str'] = "\n" + "\n".join([f"  - \"{a}\"" for a in
                                              yamlMD['authors']])

    if yamlMD.get('jref', None):
        yamlMD['jref_str'] = f" \"{yamlMD['jref']}\""
    else:
        yamlMD['jref_str'] = ""

    if yamlMD.get('doi', None):
        yamlMD['doi_str'] = f" \"{yamlMD['doi']}\""
    else:
        yamlMD['doi_str'] = ""

    if yamlMD.get('arxiv', None):
        yamlMD['arxiv_str'] = f" \"{yamlMD['arxiv']}\""
    else:
        yamlMD['arxiv_str'] = ""

    yamlMD['iid'] = yamlMD['insp_recid']
    yamlMD['used_spec_str'] = " true" if yamlMD.get('used_spec', False) else ""
    yamlMD['used_spectre_str'] = " true" if yamlMD.get('used_spectre', False) else ""
    yamlMD['abstract_str'] = fill(yamlMD['abstract'],
                                  initial_indent='  ',
                                  subsequent_indent='  ',
                                  break_long_words=False)

    # Modify the desired flag. Exactly one of spec, spectre was set
    which_key = 'used_spec_str' if spec else 'used_spectre_str'
    yamlMD[which_key] = " true" if used else ""

    with open(md_file, 'w') as f:
            f.write(md_format_str.format(**yamlMD))

if __name__ == "__main__":
    help = """Set used_spec or used_spectre to true or false in one or more
    bibkeys' markdown files."""
    parser = argparse.ArgumentParser(
        description=help, formatter_class=argparse.RawTextHelpFormatter
    )
    spec_spectre_group = parser.add_mutually_exclusive_group()
    arg_spec = spec_spectre_group.add_argument(
        '--spec', action='store_true',
        help="Modify the used_spec flag.")
    spec_spectre_group.add_argument(
        '--spectre', action='store_true',
        help="Modify the used_spectre flag.")
    parser.add_argument(
        '--used', action=argparse.BooleanOptionalAction,
        default=True,
        help="""Set the used_[spec|spectre] flag to true
(or false for --no--used). (default: %(default)s)""")
    parser.add_argument(
        "bibkeys",
        nargs='+',
        help="""INSPIRE bibkey(s) of papers whose flags we modify."""
    )

    args = parser.parse_args()

    # Check that exactly one of spec/spectre used
    if not (args.spec ^ args.spectre):
        raise argparse.ArgumentError(arg_spec,
            "Must specify exactly one of --spec or --spectre")

    bibkeys = set(args.bibkeys)
    for bibkey in bibkeys:
        try:
            rewrite_md(bibkey, args.spec, args.spectre, args.used)
        except:
            warn(f"Failed to rewrite {bibkey}.md, check the file?")
