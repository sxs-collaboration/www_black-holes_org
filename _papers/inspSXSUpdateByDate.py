#!/usr/bin/env python

import argparse
import dateparser
from warnings import warn

import sxs

from inspToMd import write_insp_resp_to_md

sxs_insp_names = [
    # Faculty
    "Nils.Deppe.1",
    "M.D.Duez.5",
    "S.E.Field.3",
    "F.Foucart.1",
    "L.E.Kidder.1",
    "G.Lovelace.1",
    "E.R.Most.1",
    "M.Okounkova.2",
    "R.Owen.2",
    "H.P.Pfeiffer.1",
    "M.A.Scheel.1",
    "Leo.C.Stein.1",
    "S.A.Teukolsky.1",
    "Vijay.Varma.1",
    "A.B.Zimmerman.1",

    # Academic staff
    "M.Boyle.1",
    "L.T.Buchman.2",
    "W.Throwe.2",

    # Postdocs
    "M.Giesler.1",
    "G.Lara.2",
    "O.Long.3",
    "K.Mitman.1",
    "Nils.L.Vu.1",

    # Students
    "A.Khairnar.1",
    "Y.Kim.62",
    "Oliver.Markwell.1",
    "Peter.J.Nee.1",
    "K.C.Nelli.1",
]

############################################################

def filterResponse(insp_resp, ignore_bibs):
    """Filter the response from INSPIRE, ignoring the papers with bibkeys in the
    list ignore_bibs. Emit warnings about all the ignore papers
    """

    # This would be a one-liner list comprehension, except we actually want to
    # emit a warning for each paper.

    filtered = []
    for paper in insp_resp:
        texkey = paper['metadata']['texkeys'][0]
        if texkey not in ignore_bibs:
            filtered.append(paper)
        else:
            warn(f"Ignoring {texkey}, found in the papers-to-ignore list.")
    return filtered

############################################################

if __name__ == "__main__":
    help = """Query INSPIRE for papers by SXS authors updated on a specific date"""
    parser = argparse.ArgumentParser(
        description=help, formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "--date",
        default="today",
        required=False,
        help="""A date (parsed by dateparser) on which papers were updated on INSPIRE.
(default: %(default)s)"""
    )
    parser.add_argument(
        "--ignore-file",
        type=argparse.FileType('r'),
        default="papersToIgnore.txt",
        required=False,
        help="""Path to a file with bibkeys to ignore, one bibkey per line.
(default: %(default)s)"""
    )

    args = parser.parse_args()

    date = dateparser.parse(args.date)
    date_str = date.strftime("%Y-%m-%d")

    au_str = " or ".join([f"author:{id}" for id in sxs_insp_names])

    insp_query = f"find du {date_str} and ({au_str})"

    ignore_bibs = [line.strip() for line in args.ignore_file.readlines()]

    write_insp_resp_to_md(
        filterResponse(
            sxs.utilities.inspire.query(insp_query),
            ignore_bibs))
