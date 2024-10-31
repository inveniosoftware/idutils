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

"""Extension class to collect and register new schemes via entrypoints.

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

Note: You can only add new schemes but not override existing ones.
"""

from threading import Lock

from importlib_metadata import entry_points

from .schemes import IDUTILS_PID_SCHEMES

# when Python >=3.12, remove importlib_metadata and replace with:
# from importlib.metadata import entry_points


def _set_default_custom_scheme_config(scheme_config):
    """Return the default config for a custom scheme."""
    # List of possible keys
    default_config = {
        "validator": lambda x: True,
        "normalizer": lambda x: x,
        "filter": [],
        "url_generator": lambda scheme, normalized_pid: None,
    }

    assert all(
        scheme_key in default_config.keys() for scheme_key in scheme_config.keys()
    )

    # Merge the provided scheme config with defaults
    return {**default_config, **scheme_config}


class CustomSchemesRegistry:
    """Singleton class for loading and storing custom schemes from entry points."""

    _instance = None
    _lock = Lock()  # To ensure thread-safe singleton creation

    def __new__(cls):
        """Create a new instance."""
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._custom_schemes_registry = (
                    {}
                )  # Internal dictionary to store schemes
                cls._instance._load_entry_points("idutils.custom_schemes")
        return cls._instance

    @property
    def custom_schemes(self):
        """Return the registered custom registered schemes.

        Each item of the registry is of the format:
            {
                "custom_scheme": {

                    # See examples in `idutils.validators` file.
                    "validator": lambda value: True else False,
                    # Used in `idutils.normalizers.normalize_pid` function.
                    "normalizer": lambda value: normalized_value,
                    # See examples in `idutils.detectors.IDUTILS_SCHEME_FILTER` config.
                    "filter": ["list_of_schemes_to_filter_out"],
                    # Used in `idutils.normalizers.to_url` function.
                    "url_generator": lambda scheme, normalized_pid: "normalized_url"

                }

            }

        """
        return self._custom_schemes_registry

    def pick_scheme_key(self, key):
        """Serialize the registered custom registered schemes by key.

        Return a list of tuples [(<scheme_name>, <scheme_config_key_value>)]
        """
        return [(scheme, config[key]) for scheme, config in self.custom_schemes.items()]

    def _load_entry_points(self, ep_name):
        """Load entry points into the internal registry."""
        existing_id_names = set(scheme[0] for scheme in IDUTILS_PID_SCHEMES)

        # Load entry points from the specified group
        for ep in set(entry_points(group=ep_name)):
            name = ep.name

            # Ensure no custom scheme overrides existing ones
            assert name not in existing_id_names, f"Scheme {name} already exists!"

            # Load the function from entry point
            scheme_register_func = ep.load()
            assert callable(scheme_register_func), f"{name} must be callable!"

            # Call the function to get the scheme config
            scheme_config = scheme_register_func()

            # Set default config values if needed
            scheme_config = _set_default_custom_scheme_config(scheme_config)

            # Store in the registry
            self._custom_schemes_registry.setdefault(name, scheme_config)
