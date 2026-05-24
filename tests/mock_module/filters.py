# SPDX-FileCopyrightText: 2024 CERN.
# SPDX-License-Identifier: BSD-3-Clause
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

"""Mock module custom scheme filters."""


def custom_scheme_filter(value):
    """Define filter for `custom_scheme`.

    Exclude `orcid` scheme.
    """
    return ["orcid"]
