# SPDX-FileCopyrightText: 2024 CERN.
# SPDX-License-Identifier: BSD-3-Clause
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

"""Persistent identifier utilities tests."""

import pytest

from idutils.normalizers import to_url
from idutils.proxies import custom_schemes_registry


def test_custom_registry_singleton(entry_points):
    """Test that the registry is instantiated only once."""
    instance1 = custom_schemes_registry()

    instance2 = custom_schemes_registry()

    assert instance1 is instance2


def test_custom_registry_url():
    url1 = to_url("12345", "custom_scheme")
    url2 = to_url("12345", "custom_scheme2")

    assert "http://custom/scheme/12345" == url1
    assert "http://custom/scheme2/12345" == url2
