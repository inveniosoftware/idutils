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
    ("email", validators.is_email),
    ("sha1", validators.is_sha1),
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
