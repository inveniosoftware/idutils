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

"""Persistent identifier utilities tests."""

import pytest

from idutils.proxies import custom_schemes_registry


def test_custom_registry_singleton(entry_points):
    """Test that the registry is instantiated only once."""
    instance1 = custom_schemes_registry()

    instance2 = custom_schemes_registry()

    assert instance1 is instance2
