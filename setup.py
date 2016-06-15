# -*- coding: utf-8 -*-
#
# This file is part of IDUtils
# Copyright (C) 2015, 2016 CERN.
#
# IDUtils is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.


"""Small library for persistent identifiers used in scholarly communication."""

import os

from setuptools import setup

readme = open('README.rst').read()
history = open('CHANGES.rst').read()

install_requires = [
    'six>=1.7.2',
    'isbnid>=0.3.4',
]

tests_require = [
    'check-manifest>=0.25',
    'coverage>=4.0',
    'isort>=4.2.2',
    'pydocstyle>=1.0',
    'pytest-cache>=1.0',
    'pytest-cov>=1.8.0',
    'pytest-pep8>=1.0.6',
    'pytest-runner>=2.6.2',
    'pytest>=2.8.0',
]

extras_require = {
    'docs': [
        'Sphinx>=1.3',
    ],
    'tests': tests_require
}


extras_require['all'] = []
for reqs in extras_require.values():
    extras_require['all'].extend(reqs)

setup_requires = [
    'pytest-runner>=2.7.0'
]

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('idutils', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='IDUtils',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    keywords='persistent identifiers',
    license='Revised BSD License',
    author='Invenio Software',
    author_email='info@invenio-software.org',
    url='https://github.com/inveniosoftware/idutils',
    packages=[
        'idutils',
    ],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
