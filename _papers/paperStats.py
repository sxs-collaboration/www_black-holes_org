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

def sessionForINSPQueries():
    """Provide an https session with some default retry settings for repeatedly
    querying INSPIRE."""

    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry

    session = requests.Session()

    ## Retry automatically on certain types of errors
    retry = Retry(
        total=10,
        backoff_factor=0.1,
        status_forcelist=[
            413,  # Request Entity Too Large
            429,  # Too Many Requests
            500,  # Internal Server Error
            502,  # Bad Gateway
            503,  # Service Unavailable
            504,  # Gateway Timeout
        ],
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)

    return session

def queryINSPAggregateBuckets(session, recid):
    """Query the (undocumented but exposed) INSPIRE API "facets"
    endpoint for getting the aggregate citations "bucket" data for
    some particular INSPIRE record id.
    """

    facets_url = "https://inspirehep.net/api/literature/facets"
    params = { "q": f"refersto:recid:{recid}" }

    response = session.get(facets_url, params=params)
    if response.status_code != 200:
        print(f"An error occurred when trying to access <{facets_url}>.", file=sys.stderr)
        try:
            print(response.json(), file=sys.stderr)
        except:
            pass
        response.raise_for_status()
        raise RuntimeError()  # Will only happen if the response was not strictly an error

    try:
        json_response = response.json()
    except ValueError:
        print(f"Response from {url} does not contain valid JSON; returning early.")
        return None

    return json_response['aggregations']['earliest_date']['buckets']

def inspAggregateBucketsToDict(date_buckets):
    """Convert INSPIRE buckets data to a normal dict."""

    return {int(d['key_as_string']): d['doc_count'] for d in date_buckets}

def queryINSPSeveralAggregateBuckets(session, yamlMD):
    """Given some yaml metadata where each item has an 'insp_recid' (INSPIRE
    record id), query INSPIRE for all of their aggregate citations "bucket"
    data."""

    return [queryINSPAggregateBuckets(session, v['insp_recid'])
            for k,v in yamlMD.items()]

def inspJoinSeveralAggregateBucketsToDict(severalBuckets):
    """Join several papers' worth of INSPIRE aggregate citation "bucket" data
    into a single dict."""

    citeDicts = list(map(inspAggregateBucketsToDict, severalBuckets))
    joinedCiteDict = {}
    for d in citeDicts:
        for year, count in d.items():
            oldCount = joinedCiteDict.get(year, 0)
            newCount = oldCount + count
            joinedCiteDict[year] = newCount
    return joinedCiteDict

def bucketDictToVects(bucketDict):
    """Take a dict derived from bucket data (e.g. from
    `inspJoinSeveralAggregateBucketsToDict`) and convert it to two numpy
    vectors. The first is a vector of years, and the second is a vector of
    citations per year."""

    years = bucketDict.keys()
    years = np.array(list(map(str, range(min(years),max(years)+1))), dtype='datetime64[Y]')
    counts = np.zeros(len(years), dtype='int')
    for k, v in bucketDict.items():
        y = np.datetime64(str(k))
        counts[ np.argwhere(years==y) ] = v
    return years, counts

def citationsPerYearPlot(ax, years, counts, ylabel, rwidth=0.9):
    """Make a plot of citations per year from years, counts vectors,
    e.g. returned by `bucketDictToVects`."""

    ax.hist(years, weights=counts, bins=len(years), rwidth=rwidth)
    ax.set_ylabel(ylabel)

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
    fig.savefig("SpECPaperStats.png")

    SpECTRECiteQueryResponses = queryINSPreferstoCreatedField(SpECTREPaperYaml)
    SpECTRECiteDates = inspResponseCiteDates(SpECTRECiteQueryResponses)

    fig, ax = plt.subplots()
    datePlot(ax, SpECTRECiteDates, 'SpECTRE citations')
    datePlot(ax, SpECTREPaperDates, 'SpECTRE Publications (orange) citations (blue)', color='orange')
    ax.set_yscale("log")

    fig.savefig("SpECTREPaperStats.pdf")
    fig.savefig("SpECTREPaperStats.png")

    ############################################################
    session = sessionForINSPQueries()
    SpECAggregates = queryINSPSeveralAggregateBuckets(session, SpECPaperYaml)
    SpECCiteDict = inspJoinSeveralAggregateBucketsToDict(SpECAggregates)
    SpECyears, SpECcounts = bucketDictToVects(SpECCiteDict)

    fig, ax = plt.subplots()
    citationsPerYearPlot(ax, SpECyears, SpECcounts, 'SpEC citations per year')

    fig.savefig("SpECCitationsPerYear.pdf")
    fig.savefig("SpECCitationsPerYear.png")
