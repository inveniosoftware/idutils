# SPDX-FileCopyrightText: 2015-2024 CERN.
# SPDX-FileCopyrightText: 2018 Alan Rubin.
# SPDX-FileCopyrightText: 2019 Inria.
# SPDX-FileCopyrightText: 2022 University of Münster.
# SPDX-FileCopyrightText: 2026 Graz University of Technology.
# SPDX-License-Identifier: BSD-3-Clause
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

"""Small library for persistent identifiers used in scholarly communication."""

import importlib
import pkgutil

__version__ = "1.6.0"


def import_attributes():
    """For backwards compatibility! Import everything for `idutils.__func__` and `from idutils import __func__` to work."""
    package_name = __name__

    importlib.import_module
    for _, file_name, _ in pkgutil.walk_packages(__path__):
        module = importlib.import_module(f".{file_name}", package_name)

        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)

            # Make sure it's not private or built-in
            if not attribute_name.startswith("_"):
                globals()[attribute_name] = attribute


import_attributes()
