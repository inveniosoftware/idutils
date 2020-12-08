..
   This file is part of IDUtils
   Copyright (C) 2015 CERN.

   IDUtils is free software; you can redistribute it and/or modify
   it under the terms of the Revised BSD License; see LICENSE file for
   more details.

   In applying this license, CERN does not waive the privileges and immunities
   granted to it by virtue of its status as an Intergovernmental Organization
   or submit itself to any jurisdiction.


=======
IDUtils
=======

.. image:: https://github.com/inveniosoftware/idutils/workflows/CI/badge.svg
        :target: https://github.com/inveniosoftware/idutils/actions?query=workflow%3ACI

.. image:: https://img.shields.io/coveralls/inveniosoftware/idutils.svg
        :target: https://coveralls.io/r/inveniosoftware/idutils

.. image:: https://img.shields.io/github/tag/inveniosoftware/idutils.svg
        :target: https://github.com/inveniosoftware/idutils/releases

.. image:: https://img.shields.io/pypi/dm/idutils.svg
        :target: https://pypi.python.org/pypi/idutils

.. image:: https://img.shields.io/github/license/inveniosoftware/idutils.svg
        :target: https://github.com/inveniosoftware/idutils/blob/master/LICENSE


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
  GND, SRA, BioProject, BioSample, Ensembl, UniProt, RefSeq, GenBank/RefSeq.

Installation
============

The IDUtils package is on PyPI so all you need is:

.. code-block:: console

    $ pip install idutils
