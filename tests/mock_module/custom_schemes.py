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
