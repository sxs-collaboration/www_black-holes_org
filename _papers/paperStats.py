#!/usr/bin/env python

import numpy as np

def loadYamlMD(paths, filterKey=None):
    """Load the yaml metadata from an iterable of `paths`.
    The easiest way to generate the paths is probably something like:

        import glob
        sxsPaperPaths = glob.glob("path/to/www_black-holes_org/_papers/*.md")

    Optional argument filterKey is the name of a yaml field to filter on, where
    an absent field is taken to mean False. Values you might want are
    `filterKey='used_spec'` or `filterKey='used_spectre'`.
    """

    import yaml
    from yaml import Loader
    from pathlib import Path

    yamlMD = {p[:-3]: yaml.load_all(Path(p).read_text(), Loader=Loader).send(None)
              for p in paths}

    if filterKey is None:
        return yamlMD

    return {k:v for k, v in yamlMD.items() if v.get(filterKey,False)}

def datesFromYamlMD(yamlMD):
    """Get a numpy array of dtype datetime64[D] from the 'date' field in a bunch
    of yaml metadata.
    """

    return np.array(sorted([v['date'] for k,v in yamlMD.items()]),
                    dtype='datetime64[D]')

def datePlot(ax, dates, ylabel, color='blue', alpha=0.5):
    """Plot a (presumably sorted) sequence of dates as a timeseries of
    cumulative number vs. time, with some lighter filling under the curve.
    """

    ax.plot(dates, 1+np.arange(len(dates)), color=color)
    ax.fill_between(dates, 1+np.arange(len(dates)), color=color, alpha=alpha)
    ax.set_xlabel('Date')
    ax.set_ylabel(ylabel)

def queryINSPreferstoCreatedField(yamlMD):
    """Given some yaml metadata where each item has an 'insp_recid' (INSPIRE
    record id), query INSPIRE to find all the 'created' timestamps of the
    'refersto' records, i.e. the dates when our papers have been cited. The does
    count self-citations. If paper X cited both Y and Z that appear in yamlMD,
    then paper X will get counted twice (as it should!).

    Note: This will break if one of our papers was cited more than 10k times
    (like record 1421100 , the GW150914 discovery PRL).
    """

    from itertools import chain
    import sxs

    cite_query_strings = [f"refersto:recid:{v['insp_recid']}" for k,v in yamlMD.items()]
    query_response = list(map(lambda s: sxs.utilities.inspire.query(s, fields="created"),
                              cite_query_strings))
    return list(chain(*query_response))

def inspResponseCiteDates(inspResponse):
    """Given an INSPIRE response (e.g. from `queryINSPreferstoCreatedField`),
    return a numpy array of dtype datetime64[D] from the 'created' field.
    """

    return np.array(sorted([c['created'] for c in inspResponse]), dtype='datetime64[D]')

############################################################

if __name__ == "__main__":

    import glob
    import matplotlib as mpl
    from matplotlib import pyplot as plt

    sxsPaperFilenames = glob.glob("*.md")

    SpECPaperYaml    = loadYamlMD(sxsPaperFilenames, 'used_spec')
    SpECTREPaperYaml = loadYamlMD(sxsPaperFilenames, 'used_spectre')

    SpECPaperDates    = datesFromYamlMD(SpECPaperYaml)
    SpECTREPaperDates = datesFromYamlMD(SpECTREPaperYaml)

    fig, ax = plt.subplots()
    datePlot(ax, SpECPaperDates, 'SpEC Publications')

    fig.savefig("SpECPaperStats.pdf")

    SpECTRECiteQueryResponses = queryINSPreferstoCreatedField(SpECTREPaperYaml)
    SpECTRECiteDates = inspResponseCiteDates(SpECTRECiteQueryResponses)

    fig, ax = plt.subplots()
    datePlot(ax, SpECTRECiteDates, 'SpECTRE citations')
    datePlot(ax, SpECTREPaperDates, 'SpECTRE Publications (orange) citations (blue)', color='orange')
    ax.set_yscale("log")

    fig.savefig("SpECTREPaperStats.pdf")
