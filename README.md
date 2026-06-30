<!--
SPDX-FileCopyrightText: 2015 CERN.
SPDX-FileCopyrightText: 2026 California Institute of Technology.
SPDX-License-Identifier: BSD-3-Clause

In applying this license, CERN does not waive the privileges and immunities
granted to it by virtue of its status as an Intergovernmental Organization
or submit itself to any jurisdiction.
-->

# IDUtils

[![CI](https://github.com/inveniosoftware/idutils/workflows/CI/badge.svg)](https://github.com/inveniosoftware/idutils/actions?query=workflow%3ACI)
[![Coverage](https://img.shields.io/coveralls/inveniosoftware/idutils.svg)](https://coveralls.io/r/inveniosoftware/idutils)
[![Release](https://img.shields.io/github/tag/inveniosoftware/idutils.svg)](https://github.com/inveniosoftware/idutils/releases)
[![Downloads](https://img.shields.io/pypi/dm/idutils.svg)](https://pypi.python.org/pypi/idutils)
[![License](https://img.shields.io/github/license/inveniosoftware/idutils.svg)](https://github.com/inveniosoftware/idutils/blob/master/LICENSE)

Small library for validating and normalising persistent identifiers used in
scholarly communication.

- Free software: Revised BSD license
- Documentation: https://inveniosoftware.github.io/idutils/.

## Features

- Validation and normalization of persistent identifiers.
- Detection of persistent identifier scheme.
- Generation of resolving links for persistent identifiers.
- Supported schemes: ISBN10, ISBN13, ISSN, ISTC, DOI, Handle, EAN8, EAN13, ISNI
  ORCID, ARK, PURL, LSID, URN, Bibcode, arXiv, PubMed ID, PubMed Central ID,
  GND, SRA, BioProject, BioSample, Ensembl, UniProt, RefSeq, GenBank/RefSeq, SWH,
  OpenAlex, CSTR, RRID, RAiD.

## Installation

The IDUtils package is on PyPI so all you need is:

```console
$ pip install idutils
```
