#!/usr/bin/env python

import argparse

import dateparser

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
    "K.C.Nelli.1",
    "Y.Kim.62",
    "A.Khairnar.1",
]

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

    args = parser.parse_args()

    date = dateparser.parse(args.date)
    date_str = date.strftime("%Y-%m-%d")

    au_str = " or ".join([f"author:{id}" for id in sxs_insp_names])

    insp_query = f"find du {date_str} and ({au_str})"

    write_insp_resp_to_md(sxs.utilities.inspire.query(insp_query))
