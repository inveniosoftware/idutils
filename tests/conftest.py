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
from invenio_app.factory import create_api


@pytest.fixture(scope="module")
def create_app(entry_points):
    """Application factory fixture."""
    return create_api


@pytest.fixture(scope="module")
def base_app(base_app):
    """Application factory fixture."""
    with base_app.app_context():
        yield base_app


@pytest.fixture(scope="module")
def extra_entry_points():
    """Register `custom_scheme` entrypoints."""
    return {
        "idutils.custom_schemes": [
            "custom_scheme = mock_module.custom_schemes:custom_scheme"
        ]
    }
