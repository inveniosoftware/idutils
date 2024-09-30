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

"""Functions for detecting the persistent identifier."""

from . import validators
from .proxies import current_idutils

IDUTILS_PID_SCHEMES = [
    ("doi", validators.is_doi),
    ("ark", validators.is_ark),
    ("handle", validators.is_handle),
    ("purl", validators.is_purl),
    ("lsid", validators.is_lsid),
    ("urn", validators.is_urn),
    ("ads", validators.is_ads),
    ("arxiv", validators.is_arxiv),
    ("ascl", validators.is_ascl),
    ("hal", validators.is_hal),
    ("pmcid", validators.is_pmcid),
    ("isbn", validators.is_isbn),
    ("issn", validators.is_issn),
    ("orcid", validators.is_orcid),
    ("isni", validators.is_isni),
    ("ean13", validators.is_ean13),
    ("ean8", validators.is_ean8),
    ("istc", validators.is_istc),
    ("gnd", validators.is_gnd),
    ("ror", validators.is_ror),
    ("pmid", validators.is_pmid),
    ("url", validators.is_url),
    ("sra", validators.is_sra),
    ("bioproject", validators.is_bioproject),
    ("biosample", validators.is_biosample),
    ("ensembl", validators.is_ensembl),
    ("uniprot", validators.is_uniprot),
    ("refseq", validators.is_refseq),
    ("genome", validators.is_genome),
    ("geo", validators.is_geo),
    ("arrayexpress_array", validators.is_arrayexpress_array),
    ("arrayexpress_experiment", validators.is_arrayexpress_experiment),
    ("swh", validators.is_swh),
    ("viaf", validators.is_viaf),
]
"""Definition of scheme name and associated test function.

Order of list is important, as identifier scheme detection will test in the
order given by this list."""


IDUTILS_SCHEME_FILTER = [
    (
        "url",
        # None these can have URLs, in which case we exclude them
        ["isbn", "istc", "urn", "lsid", "issn", "ean8", "viaf"],
    ),
    ("ean8", ["gnd", "pmid", "viaf"]),
    ("ean13", ["gnd", "pmid"]),
    ("isbn", ["gnd", "pmid"]),
    ("orcid", ["gnd", "pmid"]),
    ("isni", ["gnd", "pmid"]),
    (
        "issn",
        [
            "gnd",
            "viaf",
        ],
    ),
    ("pmid", ["viaf"]),
]
"""(present_scheme, [list of schemes to remove if present_scheme found])."""


def detect_identifier_schemes(val):
    """Detect persistent identifier scheme for a given value.

    .. note:: Some schemes like PMID are very generic.
    """
    schemes = []
    scheme_validators = IDUTILS_PID_SCHEMES + current_idutils.pick_scheme_key(
        "validator"
    )
    for scheme, test in scheme_validators:
        if test(val):
            schemes.append(scheme)

    # GNDs and ISBNs numbers can clash...
    if "gnd" in schemes and "isbn" in schemes:
        # ...in which case check explicitly if it's clearly a GND
        if val.lower().startswith("gnd:"):
            schemes.remove("isbn")

    if "viaf" in schemes and "url" in schemes:
        # check explicitly if it's a viaf
        for viaf_url in validators.viaf_urls:
            if val.startswith(viaf_url):
                schemes.remove("url")
    if "viaf" in schemes and "handle" in schemes:
        # check explicitly if it's a viaf
        for viaf_url in validators.viaf_urls:
            if val.startswith(viaf_url):
                schemes.remove("handle")

    scheme_filter = IDUTILS_SCHEME_FILTER + current_idutils.pick_scheme_key("filter")
    for first, remove_schemes in scheme_filter:
        if first in schemes:
            schemes = list(filter(lambda x: x not in remove_schemes, schemes))

    if (
        "handle" in schemes
        and "url" in schemes
        and not val.startswith("http://hdl.handle.net/")
        and not val.startswith("https://hdl.handle.net/")
    ):
        schemes = list(filter(lambda x: x != "handle", schemes))
    elif "handle" in schemes and ("ark" in schemes or "arxiv" in schemes):
        schemes = list(filter(lambda x: x != "handle", schemes))

    return schemes
