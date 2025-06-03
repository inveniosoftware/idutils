# -*- coding: utf-8 -*-
#
# This file is part of IDUtils
# Copyright (C) 2015-2024 CERN.
# Copyright (C) 2018 Alan Rubin.
# Copyright (C) 2019 Inria.
# Copyright (C) 2022 University of Münster.
#
# IDUtils is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

"""Small library for persistent identifiers used in scholarly communication."""

import importlib
import pkgutil
from warnings import warn

warn(
    "Implicit imports (e.g., 'import idutils; idutils.function;') might be removed in the next major version. Please use explicit imports (e.g., 'from idutils import function;') instead.",
    DeprecationWarning,
    stacklevel=2,
)

__version__ = "1.4.4"


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
