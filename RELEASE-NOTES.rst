============================
 IDUtils v0.2.3 is released
============================

IDUtils v0.2.3 was released on 2016-09-21

About
-----

Small library for persistent identifiers used in scholarly communication.

New features
------------

- Adds an optional parameter in `idutils.to_url` to use HTTPS scheme
  for PID providers that support it.

Improved features
-----------------

- Detects and parses Handles and DOIs without the "http(s)://", and
  ignores whitespace after scheme tags (eg. "doi:  10.123/456").

Installation
------------

   $ pip install idutils==0.2.3

Documentation
-------------

   http://idutils.readthedocs.org/en/v0.2.3

Homepage
--------

   https://github.com/inveniosoftware/idutils

Good luck and thanks for choosing IDUtils.

| Invenio Development Team
|   Email: info@inveniosoftware.org
|   Twitter: http://twitter.com/inveniosoftware
|   GitHub: http://github.com/inveniosoftware
|   URL: http://inveniosoftware.org
