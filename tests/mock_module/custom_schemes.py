# SPDX-FileCopyrightText: 2024 CERN.
# SPDX-License-Identifier: BSD-3-Clause
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

"""Mock module custom scheme validators."""


def custom_scheme():
    """Define validator for `custom_scheme`."""
    return {
        "validator": lambda value: True if value == "custom_scheme_valid" else False,
        "normalizer": lambda value: value,
        "filter": ["orcid"],
        "url_generator": lambda scheme, normalized_pid: f"{scheme}://custom/scheme/{normalized_pid}",
    }


def custom_scheme2():
    """Define validator for `custom_scheme2`."""
    return {
        "validator": lambda value: value == "custom_scheme2_valid",
        "normalizer": lambda value: value,
        "filter": ["orcid"],
        "url_generator": lambda scheme, normalized_pid: f"{scheme}://custom/scheme2/{normalized_pid}",
    }
