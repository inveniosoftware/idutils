..
   This file is part of IDUtils
   Copyright (C) 2015-2018 CERN.
   Copyright (C) 2018 Alan Rubin.

   IDUtils is free software; you can redistribute it and/or modify
   it under the terms of the Revised BSD License; see LICENSE file for
   more details.

   In applying this license, CERN does not waive the privileges and immunities
   granted to it by virtue of its status as an Intergovernmental Organization
   or submit itself to any jurisdiction.

.. currentmodule:: idutils

Small library for validating and normalising persistent identifiers used in
scholarly communication.

* Free software: Revised BSD license
* Documentation: https://idutils.readthedocs.io.

Features
========

- Validation and normalization of persistent identifiers.
- Detection of persistent identifier scheme.
- Generation of resolving links for persistent identifiers.
- Supported schemes: ISBN10, ISBN13, ISSN, ISTC, DOI, Handle, EAN8, EAN13, ISNI
  ORCID, ARK, PURL, LSID, URN, Bibcode, arXiv, PubMed ID, PubMed Central ID,
  GND, SRA, BioProject, BioSample, Ensembl, UniProt, RefSeq, Genome Assembly,
  GEO, ArrayExpress.

Installation
============

The IDUtils package is on PyPI so all you need is:

.. code-block:: console

    $ pip install idutils


API
===

.. automodule:: idutils
   :members: is_isbn10, is_isbn13, is_isbn, is_issn, is_istc, is_doi, is_handle, is_ean8, is_ean13, is_ean, is_isni, is_orcid, is_purl, is_url, is_lsid, is_urn, is_ads, is_arxiv_post_2007, is_arxiv_pre_2007, is_arxiv, is_pmid, is_pmcid, is_gnd, is_sra, is_bioproject, is_biosample, is_ensembl, is_uniprot, is_refseq, is_genome, is_geo, is_arrayexpress_array, is_arrayexpress_experiment, detect_identifier_schemes, normalize_doi, normalize_handle, normalize_ads, normalize_orcid, normalize_gnd, normalize_pmid, normalize_arxiv, normalize_pid, to_url


.. include:: ../CHANGES.rst

.. include:: ../CONTRIBUTING.rst

License
=======

.. include:: ../LICENSE

.. include:: ../AUTHORS.rst
