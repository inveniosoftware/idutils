# SPDX-FileCopyrightText: 2024 CERN.
# SPDX-License-Identifier: BSD-3-Clause
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

"""Mock module custom scheme normalizers."""


def custom_scheme_normalizer(value):
    """Define normalizer for `custom_scheme`."""
    return f"normalized_{value}"
