#!/usr/bin/env python

import argparse
import subprocess
from warnings import warn

############################################################

if __name__ == "__main__":
    help = """Remove one or more bibkeys' markdown files, and add it (them) to
    the list of papers to ignore."""
    parser = argparse.ArgumentParser(
        description=help, formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "--ignore-file",
        type=argparse.FileType('r+'),
        default="papersToIgnore.txt",
        required=False,
        help="""Path to a file with bibkeys to ignore, one bibkey per line.
(default: %(default)s)"""
    )
    parser.add_argument(
        "bibkeys",
        nargs='+',
        help="""INSPIRE bibkey(s) of papers to remove from repo and add to the
ignore-file."""
    )

    args = parser.parse_args()

    cur_ignore_bibs = set([line.strip()
                           for line in args.ignore_file.readlines()])

    new_ignore_bibs = set(args.bibkeys)

    # Warn about those already in the intersection
    for bibkey in new_ignore_bibs & cur_ignore_bibs:
        warn(f"skipping bibkey {bibkey}, "
             f"it's already in {args.ignore_file.name}.")

    new_ignore_bibs = new_ignore_bibs - cur_ignore_bibs

    for bibkey in new_ignore_bibs:
        # check=True will raise CalledProcessError if not success
        subprocess.run(['git', 'rm', bibkey + '.md'], check=True)
        args.ignore_file.write(bibkey + '\n')

    args.ignore_file.flush()
    args.ignore_file.close()

    # Now git add the updated ignore file
    # check=True will raise CalledProcessError if not success
    subprocess.run(['git', 'add', args.ignore_file.name], check=True)
