# -*- coding: utf-8 -*-
#
# This file is part of IDUtils
# Copyright (C) 2015-2024 CERN.
# Copyright (C) 2018 Alan Rubin.
# Copyright (C) 2019 Inria.
# Copyright (C) 2022 University of Münster.
# Copyright (C) 2025 Graz University of Technology.
#
# IDUtils is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

"""Small library for persistent identifiers used in scholarly communication."""

import pkgutil
from importlib import import_module
from warnings import warn

__version__ = "1.5.0"


def import_module_by_name(name):
    """Import module."""
    package_name = __name__
    for _, file_name, _ in pkgutil.walk_packages(__path__):
        module = import_module(f".{file_name}", package_name)

        for attribute_name in dir(module):
            if attribute_name == name:
                return getattr(module, attribute_name)


def __getattr__(name: str):
    """__getattr__"""
    try:
        return import_module(f".{name}", __name__)
    except ImportError:
        warn(
            f"Accessing '{name}' via the package namespace idutils is deprecated. "
            f"Please use 'from idutils.moduleA import {name}' instead. "
            "Namespace access will be removed in a future version.",
            DeprecationWarning,
            stacklevel=2,
        )
        return import_module_by_name(name)
