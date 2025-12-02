# -*- coding: utf-8 -*-
#
# This file is part of IDUtils
# Copyright (C) 2015-2022 CERN.
# Copyright (C) 2015-2018 Alan Rubin.
# Copyright (C) 2025 Will Riley.
# Copyright (C) 2025 Graz University of Technology.
#
# IDUtils is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

"""Persistent identifier utilities tests."""


# om idutils import is_wikidata


def test_kk():
    """Test kk."""
    from idutils import is_wikidata

    assert is_wikidata("wikidata:Q303")


def test_namespace_import():
    """Test wikidata validation."""
    import idutils

    assert idutils.is_wikidata("wikidata:Q303")
