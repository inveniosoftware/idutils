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

from .detectors import *
from .normalizers import *
from .proxies import *
from .schemes import *
from .utils import *
from .validators import *

__version__ = "1.5.0"
