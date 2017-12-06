..
   This file is part of IDUtils
   Copyright (C) 2015 CERN.

   IDUtils is free software; you can redistribute it and/or modify
   it under the terms of the Revised BSD License; see LICENSE file for
   more details.

   In applying this license, CERN does not waive the privileges and immunities
   granted to it by virtue of its status as an Intergovernmental Organization
   or submit itself to any jurisdiction.


Changes
=======

Version 1.0.0 (2017-12-07)

- Fixes handling of unicode characters in DOIs.
- Adds support for APS style arXiv identifiers.

Version 0.2.4 (2017-01-30)

- Removes `Python 3.3` from a list of supported Python versions and
  adds `Python 3.6`
- Moves from `isbnid (v0.3.4)` to `isbnid_fork (v0.4.4)` library.

Version 0.2.3 (2016-09-21)

- Adds an optional parameter in `idutils.to_url` to use HTTPS scheme
  for PID providers that support it.
- Detects and parses Handles and DOIs without the "http(s)://", and
  ignores whitespace after scheme tags (eg. "doi:  10.123/456").

Version 0.2.2 (2016-09-16)

- Fixes issue where a valid ISBN with dashes and spaces could not be
  normalized.

Version 0.2.1 (2016-06-17)

- Changes ISBN normalization to use `isbnid` instead of `isbnlib`. Now,
  importing this library will not change the default socket timeout, resulting
  in unwanted side effects.

Version 0.2.0 (2016-04-07)

- Changes URL resolution for DOIs to use https://doi.org instead of
  http://dx.doi.org according to
  https://www.doi.org/doi_handbook/3_Resolution.html#3.8

Version 0.1.1 (2015-07-22)

- Fixes GND validation and normalization.
- Replaces invalid package name in `run-tests.sh` and makes `run-tests.sh` file
  executable. One can now use `docker-compose run --rm web /code/run-tests.sh`
  to run all the CI tests (pep257, sphinx, test suite).
- Initial release of Docker configuration suitable for local developments.
  `docker-compose build` rebuilds the image,
  `docker-compose run --rm web /code/run-tests.sh` runs the test suite.

Version 0.1.0 (2015-07-02)

- First public release.
