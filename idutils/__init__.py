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

"""Small library for persistent identifiers used in scholarly communication.

Setting up custom schemes
-------------------------
In order to define your own custom schemes you can use the following entrypoint to
register them

.. code-block:: python

    [options.entry_points]
    idutils.custom_schemes =
        my_new_scheme = my_module.get_scheme_config_func

The entry point ``'my_new_scheme = my_module.get_scheme_config_func'`` defines an entry
point named ``my_new_scheme`` pointing to the function ``my_module.get_scheme_config_func``
which returns the config for your new registered scheme.

That function must return a dictionary with the following format:

.. code-block:: python

    def get_scheme_config_func():
        return {
            # See examples in `idutils.validators` file.
            "validator": lambda value: True else False,
            # Used in `idutils.normalizers.normalize_pid` function.
            "normalizer": lambda value: normalized_value,
            # See examples in `idutils.detectors.IDUTILS_SCHEME_FILTER` config.
            "filter": ["list_of_schemes_to_filter_out"],
            # Used in `idutils.normalizers.to_url` function.
            "url_generator": lambda scheme, normalized_pid: "normalized_url",
        }

Each key is optional and if not provided a default value is defined in
`idutils.ext._set_default_custom_scheme_config()` function.
"""

import importlib
import pkgutil
from warnings import warn

warn(
    "Implicit imports (e.g., 'import idutils; idutils.function;') might be removed in the next major version. Please use explicit imports (e.g., 'from idutils import function;') instead.",
    DeprecationWarning,
    stacklevel=2,
)

__version__ = "1.3.0"


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
