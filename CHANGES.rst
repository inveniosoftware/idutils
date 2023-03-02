..
   This file is part of IDUtils
   Copyright (C) 2015-2023 CERN.
   Copyright (C) 2022 Northwestern University.

   IDUtils is free software; you can redistribute it and/or modify
   it under the terms of the Revised BSD License; see LICENSE file for
   more details.

   In applying this license, CERN does not waive the privileges and immunities
   granted to it by virtue of its status as an Intergovernmental Organization
   or submit itself to any jurisdiction.


Changes
=======

Version 1.1.14 (2023-03-02)

- Fixes ORCiD validation, by adding the new ISNI block range.

Version 1.1.13 (2022-10-05)

- Fixes an ISBN normalization issue.

Version 1.1.12 (2022-02-28)

- Replaces ``isbnid_fork`` with ``isbnlib``

Version 1.1.11 (2022-01-28)

- Normalize pmid + their URL identifiers

Version 1.1.10 (2022-01-11)

- Add purl.fdlp.gov as a valid PURL netloc
- Normalize ror identifiers

Version 1.1.9 (2021-08-30)

- Update ARK's NAAN regex per https://datatracker.ietf.org/doc/html/draft-kunze-ark-28#section-2.3.

Version 1.1.8 (2020-08-13)

- Adds support for GEO and ArrayExpress identifiers.

Version 1.1.7 (2020-06-22)

- Updates Software Heritage identifiers
- Adds Research Organization Registry identifiers
- Fixes DeprctationWarnings by using raw strings for regular expressions

Version 1.1.6 (2020-05-07)

- Deprecates Python versions lower than 3.6.0. Now supporting 3.6.0 and 3.7.0.

Version 1.1.5 (2020-02-26)

- Adds support for Software Heritage identifiers.
- Fixes handling of non-digit characters in DOI detection.

Version 1.1.4 (2019-09-27)

- Adds support for ASCL identifiers.
- Fixes the ADS identifier regex to also detect lower-case author initials.

Version 1.1.3 (2019-09-17)

- Adds support for HTTPS ORCiD identifiers.

Version 1.1.2 (2019-02-12)

- Adds support for HAL identifiers.

Version 1.1.1 (2018-11-18)

- Changes URL resolution for bibcodes to use https://ui.adsabs.harvard instead
  of https://adsabs.harvard.edu/abs/.
- Allows choosing HTTP/HTTPS for any generated URL by ``idutils.to_url``.

Version 1.1.0 (2018-08-17)

- Adds support for genomic identifiers: SRA, BioProject, BioSample, Ensembl,
  UniProt, RefSeq, GenBank/RefSeq.
- Fixes bug in bibcode detection for non-capitalized journals.

Version 1.0.1 (2018-05-02)

- Fixes bug causing invalid DOIs to be accepted.

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
