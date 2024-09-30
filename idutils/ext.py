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

"""Invenio IDUtils module for managing persistent identifiers used in scholarly communication."""

from importlib_metadata import entry_points

from .detectors import IDUTILS_PID_SCHEMES
from .proxies import current_idutils


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

    return {**default_config, **scheme_config}


class IDUtils(object):
    """Invenio extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialiation."""
        self.init_idutils_registry()
        app.extensions["idutils"] = self

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
                "url_generator": lambda scheme, normalized_pid: "normalized_url",
            }
        }

        See examples in `idutils.validators` file.
        """
        return self._custom_schemes

    def pick_scheme_key(self, key):
        """Serialize the registered custom registered schemes by key.

        Return a list of tuples [(<scheme_name>, <scheme_config_key_value>)]
        """
        return [(scheme, config[key]) for scheme, config in self.custom_schemes.items()]

    def init_idutils_registry(self):
        """Initialize custom schemes registries."""
        self._custom_schemes = {}
        self._load_entry_point(
            self._custom_schemes,
            "idutils.custom_schemes",
        )

    def _load_entry_point(self, registry, ep_name):
        """Load entry points inton the given registry."""
        existing_id_names = set(scheme[0] for scheme in IDUTILS_PID_SCHEMES)
        for ep in set(entry_points(group=ep_name)):
            name = ep.name
            # Assert that the custom scheme is not overriding any existing scheme
            assert name not in existing_id_names

            scheme_register_func = ep.load()
            assert callable(scheme_register_func)

            scheme_config = scheme_register_func()
            scheme_config = _set_default_custom_scheme_config(scheme_config)
            registry.setdefault(name, scheme_config)


def finalize_app(app):
    """Finalize app."""
    init(app)


def api_finalize_app(app):
    """Finalize app."""
    init(app)


def init(app):
    """Init app."""
    ext = app.extensions["idutils"]
