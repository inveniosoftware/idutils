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

"""Functions for detecting the persistent identifier."""

from . import validators
from .proxies import custom_schemes_registry
from .schemes import IDUTILS_PID_SCHEMES as _IDUTILS_PID_SCHEMES
from .schemes import IDUTILS_SCHEME_FILTER as _IDUTILS_SCHEME_FILTER

IDUTILS_PID_SCHEMES = _IDUTILS_PID_SCHEMES
"""Definition of scheme name and associated test function.

Order of list is important, as identifier scheme detection will test in the
order given by this list."""


IDUTILS_SCHEME_FILTER = _IDUTILS_SCHEME_FILTER
"""(present_scheme, [list of schemes to remove if present_scheme found])."""


def detect_identifier_schemes(val):
    """Detect persistent identifier scheme for a given value.

    .. note:: Some schemes like PMID are very generic.
    """
    schemes = []
    scheme_validators = IDUTILS_PID_SCHEMES + custom_schemes_registry().pick_scheme_key(
        "validator"
    )
    for scheme, test in scheme_validators:
        if test(val):
            schemes.append(scheme)

    # GNDs and ISBNs numbers can clash...
    if "gnd" in schemes and "isbn" in schemes:
        # ...in which case check explicitly if it's clearly a GND
        if val.lower().startswith("gnd:"):
            schemes.remove("isbn")

    if "viaf" in schemes and "url" in schemes:
        # check explicitly if it's a viaf
        for viaf_url in validators.viaf_urls:
            if val.startswith(viaf_url):
                schemes.remove("url")
    if "viaf" in schemes and "handle" in schemes:
        # check explicitly if it's a viaf
        for viaf_url in validators.viaf_urls:
            if val.startswith(viaf_url):
                schemes.remove("handle")

    scheme_filter = IDUTILS_SCHEME_FILTER + custom_schemes_registry().pick_scheme_key(
        "filter"
    )
    for first, remove_schemes in scheme_filter:
        if first in schemes:
            schemes = list(filter(lambda x: x not in remove_schemes, schemes))

    if (
        "handle" in schemes
        and "url" in schemes
        and not val.startswith("http://hdl.handle.net/")
        and not val.startswith("https://hdl.handle.net/")
    ):
        schemes = list(filter(lambda x: x != "handle", schemes))
    elif "handle" in schemes and ("ark" in schemes or "arxiv" in schemes):
        schemes = list(filter(lambda x: x != "handle", schemes))

    return schemes
