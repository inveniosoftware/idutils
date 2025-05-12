# -*- coding: utf-8 -*-
#
# This file is part of IDUtils
# Copyright (C) 2024 CERN.
# Copyright (C) 2025 Will Riley.
#
# IDUtils is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

"""Utility file containing ID validators."""

import unicodedata
from urllib.parse import urlparse

from .utils import *
from .utils import _convert_x_to_10


def is_isbn(val):
    """Test if argument is an ISBN-10 or ISBN-13 number."""
    if is_isbn10(val) or is_isbn13(val):
        if val[0:3] in ["978", "979"] or not is_ean13(val):
            return True
    return False


def is_issn(val):
    """Test if argument is an ISSN number."""
    try:
        val = val.replace("-", "").replace(" ", "").upper()
        if len(val) != 8:
            return False
        r = sum([(8 - i) * (_convert_x_to_10(x)) for i, x in enumerate(val)])
        return not (r % 11)
    except ValueError:
        return False


def is_istc(val):
    """Test if argument is a International Standard Text Code.

    See http://www.istc-international.org/html/about_structure_syntax.aspx
    """
    val = val.replace("-", "").replace(" ", "").upper()
    if len(val) != 16:
        return False
    sequence = [11, 9, 3, 1]
    try:
        r = sum([int(x, 16) * sequence[i % 4] for i, x in enumerate(val[:-1])])
        ck = hex(r % 16)[2:].upper()
        return ck == val[-1]
    except ValueError:
        return False


def is_doi(val):
    """Test if argument is a DOI."""
    return doi_regexp.match(val)


def is_handle(val):
    """Test if argument is a Handle.

    Note, DOIs are also handles, and handle are very generic so they will also
    match e.g. any URL your parse.
    """
    return handle_regexp.match(val) and not is_swh(val)


def is_ean8(val):
    """Test if argument is a International Article Number (EAN-8)."""
    if len(val) != 8:
        return False
    sequence = [3, 1]
    try:
        r = sum([int(x) * sequence[i % 2] for i, x in enumerate(val[:-1])])
        ck = (10 - r % 10) % 10
        return ck == int(val[-1])
    except ValueError:
        return False


def is_ean13(val):
    """Test if argument is a International Article Number (EAN-13)."""
    if len(val) != 13:
        return False
    sequence = [1, 3]
    try:
        r = sum([int(x) * sequence[i % 2] for i, x in enumerate(val[:-1])])
        ck = (10 - r % 10) % 10
        return ck == int(val[-1])
    except ValueError:
        return False


def is_ean(val):
    """Test if argument is a International Article Number (EAN-13 or EAN-8).

    See http://en.wikipedia.org/wiki/International_Article_Number_(EAN).
    """
    return is_ean13(val) or is_ean8(val)


def is_isni(val):
    """Test if argument is an International Standard Name Identifier."""
    val = val.replace("-", "").replace(" ", "").upper()
    if len(val) != 16:
        return False
    try:
        r = 0
        for x in val[:-1]:
            r = (r + int(x)) * 2
        ck = (12 - r % 11) % 11
        return ck == _convert_x_to_10(val[-1])
    except ValueError:
        return False


def is_orcid(val):
    """Test if argument is an ORCID ID.

    See http://support.orcid.org/knowledgebase/
        articles/116780-structure-of-the-orcid-identifier
    """
    for orcid_url in orcid_urls:
        if val.startswith(orcid_url):
            val = val[len(orcid_url) :]
            break

    val = val.replace("-", "").replace(" ", "")
    if is_isni(val):
        val = int(val[:-1], 10)  # Remove check digit and convert to int.
        return any(start <= val <= end for start, end in orcid_isni_ranges)
    return False


def is_ark(val):
    """Test if argument is an ARK."""
    res = urlparse(val)
    return ark_suffix_regexp.match(val) or (
        res.scheme == "http"
        and res.netloc != ""
        and
        # Note res.path includes leading slash, hence [1:] to use same reexp
        ark_suffix_regexp.match(res.path[1:])
        and res.params == ""
    )


def is_purl(val):
    """Test if argument is a PURL."""
    res = urlparse(val)
    purl_netlocs = [
        "purl.org",
        "purl.oclc.org",
        "purl.net",
        "purl.com",
        "purl.fdlp.gov",
    ]
    return (
        res.scheme in ["http", "https"]
        and res.netloc in purl_netlocs
        and res.path != ""
    )


def is_url(val):
    """Test if argument is a URL."""
    res = urlparse(val)
    return bool(res.scheme and res.netloc)


def is_lsid(val):
    """Test if argument is a LSID."""
    return is_urn(val) and lsid_regexp.match(val)


def is_urn(val):
    """Test if argument is an URN."""
    res = urlparse(val)
    return bool(res.scheme == "urn" and res.netloc == "" and res.path != "")


def is_ads(val):
    """Test if argument is an ADS bibliographic code."""
    val = unicodedata.normalize("NFKD", val)
    return ads_regexp.match(val)


def is_arxiv_post_2007(val):
    """Test if argument is a post-2007 arXiv ID."""
    return arxiv_post_2007_regexp.match(val) or arxiv_post_2007_with_class_regexp.match(
        val
    )


def is_arxiv_pre_2007(val):
    """Test if argument is a pre-2007 arXiv ID."""
    return arxiv_pre_2007_regexp.match(val)


def is_arxiv(val):
    """Test if argument is an arXiv ID.

    See http://arxiv.org/help/arxiv_identifier and
        http://arxiv.org/help/arxiv_identifier_for_services.
    """
    return is_arxiv_post_2007(val) or is_arxiv_pre_2007(val)


def is_hal(val):
    """Test if argument is a HAL identifier.

    See (https://hal.archives-ouvertes.fr)
    """
    return hal_regexp.match(val)


def is_pmid(val):
    """Test if argument is a PubMed ID.

    Warning: PMID are just integers, with no structure, so this function will
    say any integer is a PubMed ID
    """
    return pmid_regexp.match(val)


def is_pmcid(val):
    """Test if argument is a PubMed Central ID."""
    return pmcid_regexp.match(val)


def is_gnd(val):
    """Test if argument is a GND Identifier."""
    return gnd_regexp.match(val)


def is_sra(val):
    """Test if argument is an SRA accession."""
    return sra_regexp.match(val)


def is_bioproject(val):
    """Test if argument is a BioProject accession."""
    return bioproject_regexp.match(val)


def is_biosample(val):
    """Test if argument is a BioSample accession."""
    return biosample_regexp.match(val)


def is_ensembl(val):
    """Test if argument is an Ensembl accession."""
    return ensembl_regexp.match(val)


def is_uniprot(val):
    """Test if argument is a UniProt accession."""
    return uniprot_regexp.match(val)


def is_refseq(val):
    """Test if argument is a RefSeq accession."""
    return refseq_regexp.match(val)


def is_genome(val):
    """Test if argument is a GenBank or RefSeq genome assembly accession."""
    return genome_regexp.match(val)


def is_geo(val):
    """Test if argument is a Gene Expression Omnibus (GEO) accession."""
    return geo_regexp.match(val)


def is_arrayexpress_array(val):
    """Test if argument is an ArrayExpress array accession."""
    return arrayexpress_array_regexp.match(val)


def is_arrayexpress_experiment(val):
    """Test if argument is an ArrayExpress experiment accession."""
    return arrayexpress_experiment_regexp.match(val)


def is_ascl(val):
    """Test if argument is a ASCL accession."""
    return ascl_regexp.match(val)


def is_rfc3987_ipath_absolute(val):
    """Test if the argument is an <ipath-absolute> from RFC 3987."""
    return rfc3987_reg_exps["ipath_absolute"].fullmatch(val) is not None


def is_rfc3987_iri(val):
    """Test if the argment is an <iri> from RFC 3987."""
    return rfc3987_reg_exps["iri"].fullmatch(val) is not None


def is_swh(val):
    """Test if argument is a Software Heritage identifier.

    https://docs.softwareheritage.org/devel/swh-model/persistent-identifiers.html#syntax
    """
    m = swh_before_qualifiers_regexp.match(val)
    if m is not None:
        qualifiers = m.group("qualifiers")
        if qualifiers is None:
            return True
        else:
            qualifiers = str(qualifiers)[1:]  # remove the first semi-colon
            qualifiers = qualifiers.split(";")  # split by semi-colon
            for qualifier in qualifiers:
                m = swh_qualifier_values_regexp.match(qualifier)
                if m is None:
                    return False
                else:
                    qualifier_dict = m.groupdict()

                    # origin value must be IRI according to RFC 3987
                    origin_value = qualifier_dict["origin_value"]
                    if origin_value is not None and not is_rfc3987_iri(
                        str(origin_value)
                    ):
                        return False

                    # path value must be an <ipath-absolute>
                    path_value = qualifier_dict["path_value"]
                    if path_value is not None and not is_rfc3987_ipath_absolute(
                        str(path_value)
                    ):
                        return False
            return True
    return False


def is_ror(val):
    """Test if argument is a ROR id."""
    return ror_regexp.match(val)


def is_viaf(val):
    """Test if argument is a VIAF id."""
    for viaf_url in viaf_urls:
        if val.startswith(viaf_url):
            return True
    res = viaf_regexp.match(val)
    if res:
        return viaf_regexp.match(val).group() == val
    else:
        return False


def is_email(val):
    """Test if argument looks like an email address.

    Note this test is designed to distinguish an email from other identifier
    schemes only. It does not imply a valid address / domain etc.
    """
    return email_regexp.match(val)


def is_sha1(val):
    """Test if argument is a valid SHA-1 (hex) hash."""
    return sha1_regexp.match(val)
