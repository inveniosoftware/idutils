# -*- coding: utf-8 -*-
#
# This file is part of IDUtils
# Copyright (C) 2024 CERN.
#
# IDUtils is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

"""ID normalizer helper functions."""

import unicodedata

import isbnlib

from .proxies import custom_schemes_registry
from .utils import *
from .validators import is_arxiv_post_2007, is_arxiv_pre_2007


def normalize_doi(val):
    """Normalize a DOI."""
    m = doi_regexp.match(val)
    return m.group(2)


def normalize_handle(val):
    """Normalize a Handle identifier."""
    m = handle_regexp.match(val)
    return m.group(2)


def normalize_ads(val):
    """Normalize an ADS bibliographic code."""
    val = unicodedata.normalize("NFKD", val)
    m = ads_regexp.match(val)
    return m.group(2)


def normalize_orcid(val):
    """Normalize an ORCID identifier."""
    for orcid_url in orcid_urls:
        if val.startswith(orcid_url):
            val = val[len(orcid_url) :]
            break
    val = val.replace("-", "").replace(" ", "")

    return "-".join([val[0:4], val[4:8], val[8:12], val[12:16]])


def normalize_gnd(val):
    """Normalize a GND identifier."""
    m = gnd_regexp.match(val)
    return f"gnd:{m.group(2)}"


def normalize_urn(val):
    """Normalize a URN."""
    if val.startswith(urn_resolver_url):
        val = val[len(urn_resolver_url) :]
    if val.lower().startswith("urn:"):
        val = val[len("urn:") :]
    return "urn:{0}".format(val)


def normalize_pmid(val):
    """Normalize a PubMed ID."""
    m = pmid_regexp.match(val)
    return m.group(2)


def normalize_arxiv(val):
    """Normalize an arXiv identifier."""
    if not val.lower().startswith("arxiv:"):
        val = "arXiv:{0}".format(val)
    elif val[:6] != "arXiv:":
        val = "arXiv:{0}".format(val[6:])

    # Normalize old identifiers to preferred scheme as specified by
    # http://arxiv.org/help/arxiv_identifier_for_services
    # (i.e. arXiv:math.GT/0309136 -> arXiv:math/0309136)
    m = is_arxiv_pre_2007(val)
    if m and m.group(3):
        val = "".join(m.group(1, 2, 4, 5))
        if m.group(6):
            val += m.group(6)

    m = is_arxiv_post_2007(val)
    if m:
        val = "arXiv:" + ".".join(m.group(2, 3))
        if m.group(4):
            val += m.group(4)
    return val


def normalize_hal(val):
    """Normalize a HAL identifier."""
    val = val.replace(" ", "").lower().replace("hal:", "")
    return val


def normalize_isbn(val):
    """Normalize an ISBN identifier.

    Also converts ISBN10 to ISBN13.
    """
    if is_isbn10(val):
        val = isbnlib.to_isbn13(val)
    return isbnlib.mask(isbnlib.canonical(val))


def normalize_issn(val):
    """Normalize an ISSN identifier."""
    val = val.replace(" ", "").replace("-", "").strip().upper()
    return "{0}-{1}".format(val[:4], val[4:])


def normalize_ror(val):
    """Normalize a ROR."""
    m = ror_regexp.match(val)
    return m.group(1)


def normalize_viaf(val):
    """Normalize a VIAF identifier."""
    for viaf_url in viaf_urls:
        if val.startswith(viaf_url):
            val = val[len(viaf_url) :]
            break
    if val.lower().startswith("viaf:"):
        val = val[len("viaf:") :]
    return "viaf:{0}".format(val)


def normalize_pid(val, scheme):
    """Normalize an identifier.

    E.g. doi:10.1234/foo and http://dx.doi.org/10.1234/foo and 10.1234/foo
    will all be normalized to 10.1234/foo.
    """
    if not val:
        return val

    if scheme == "doi":
        return normalize_doi(val)
    elif scheme == "handle":
        return normalize_handle(val)
    elif scheme == "ads":
        return normalize_ads(val)
    elif scheme == "pmid":
        return normalize_pmid(val)
    elif scheme == "arxiv":
        return normalize_arxiv(val)
    elif scheme == "orcid":
        return normalize_orcid(val)
    elif scheme == "gnd":
        return normalize_gnd(val)
    elif scheme == "isbn":
        return normalize_isbn(val)
    elif scheme == "issn":
        return normalize_issn(val)
    elif scheme == "hal":
        return normalize_hal(val)
    elif scheme == "ror":
        return normalize_ror(val)
    elif scheme == "urn":
        return normalize_urn(val)
    elif scheme == "viaf":
        return normalize_viaf(val)
    else:
        for custom_scheme, normalizer in custom_schemes_registry().pick_scheme_key(
            "normalizer"
        ):
            if scheme == custom_scheme:
                return normalizer(val)
    return val


IDUTILS_LANDING_URLS = {
    "doi": "{scheme}://doi.org/{pid}",
    "handle": "{scheme}://hdl.handle.net/{pid}",
    "arxiv": "{scheme}://arxiv.org/abs/{pid}",
    "ascl": "{scheme}://ascl.net/{pid}",
    "orcid": "{scheme}://orcid.org/{pid}",
    "pmid": "{scheme}://pubmed.ncbi.nlm.nih.gov/{pid}/",
    "pmcid": "{scheme}://pmc.ncbi.nlm.nih.gov/articles/{pid}/",
    "ads": "{scheme}://ui.adsabs.harvard.edu/#abs/{pid}",
    "gnd": "{scheme}://d-nb.info/gnd/{pid}",
    "urn": "{scheme}://nbn-resolving.org/{pid}",
    "sra": "{scheme}://www.ebi.ac.uk/ena/data/view/{pid}",
    "bioproject": "{scheme}://www.ebi.ac.uk/ena/data/view/{pid}",
    "biosample": "{scheme}://www.ebi.ac.uk/ena/data/view/{pid}",
    "ensembl": "{scheme}://www.ensembl.org/id/{pid}",
    "uniprot": "{scheme}://purl.uniprot.org/uniprot/{pid}",
    "refseq": "{scheme}://www.ncbi.nlm.nih.gov/entrez/viewer.fcgi?val={pid}",
    "genome": "{scheme}://www.ncbi.nlm.nih.gov/assembly/{pid}",
    "geo": "{scheme}://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={pid}",
    "arrayexpress_array": "{scheme}://www.ebi.ac.uk/arrayexpress/arrays/{pid}",
    "arrayexpress_experiment": "{scheme}://www.ebi.ac.uk/arrayexpress/experiments/{pid}",
    "hal": "{scheme}://hal.archives-ouvertes.fr/{pid}",
    "swh": "{scheme}://archive.softwareheritage.org/{pid}",
    "ror": "{scheme}://ror.org/{pid}",
    "viaf": "{scheme}://viaf.org/viaf/{pid}",
}
"""URL generation configuration for the supported PID providers."""


def to_url(val, scheme, url_scheme="http"):
    """Convert a resolvable identifier into a URL for a landing page.

    :param val: The identifier's value.
    :param scheme: The identifier's scheme.
    :param url_scheme: Scheme to use for URL generation, 'http' or 'https'.
    :returns: URL for the identifier.

    .. versionadded:: 0.3.0
       ``url_scheme`` used for URL generation.
    """
    pid = normalize_pid(val, scheme)
    landing_urls = IDUTILS_LANDING_URLS
    if scheme in landing_urls:
        if scheme == "gnd" and pid.startswith("gnd:"):
            pid = pid[len("gnd:") :]
        if scheme == "urn" and not pid.lower().startswith("urn:nbn:"):
            return ""
        if scheme == "ascl":
            pid = val.split(":")[1]
        if scheme == "viaf" and pid.startswith("viaf:"):
            pid = pid[len("viaf:") :]
            url_scheme = "https"
        return landing_urls[scheme].format(scheme=url_scheme, pid=pid)
    elif scheme in ["purl", "url"]:
        return pid
    else:
        for custom_scheme, url_generator in custom_schemes_registry().pick_scheme_key(
            "url_generator"
        ):
            if scheme == custom_scheme:
                return url_generator(url_scheme, pid)

    return ""
