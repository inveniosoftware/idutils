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

"""Pytest configuration."""

import pytest


@pytest.fixture(scope="module")
def extra_entry_points():
    """Register `custom_scheme` entrypoints."""
    return {
        "idutils.custom_schemes": [
            "custom_scheme = mock_module.custom_schemes:custom_scheme",
            "custom_scheme2 = mock_module.custom_schemes:custom_scheme2",
        ]
    }
