# SPDX-FileCopyrightText: 2024 CERN.
# SPDX-License-Identifier: BSD-3-Clause
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

"""Proxy definitions."""

from .ext import CustomSchemesRegistry

custom_schemes_registry = lambda: CustomSchemesRegistry()
"""Proxy to the custom scheme registrty."""
