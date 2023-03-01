# -*- coding: utf-8 -*-
#
# This file is part of IDUtils
# Copyright (C) 2015-2022 CERN.
# Copyright (C) 2015-2018 Alan Rubin.
#
# IDUtils is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

"""Persistent identifier utilities tests."""

from __future__ import absolute_import, print_function

import idutils

identifiers = [
    ('urn:isbn:0451450523', ['urn', 'isbn'], '', ''),
    ('urn:isan:0000-0000-9E59-0000-O-0000-0000-2', ['urn', ], '', ''),
    ('urn:issn:0167-6423', ['urn', ], '', ''),
    ('urn:ietf:rfc:2648', ['urn', ], '', ''),
    ('urn:mpeg:mpeg7:schema:2001', ['urn', ], '', ''),
    ('urn:oid:2.16.840', ['urn', ], '', ''),
    ('urn:uuid:6e8bc430-9c3a-11d9-9669-0800200c9a66', ['urn', ], '', ''),
    ('urn:nbn:de:bvb:19-146642', ['urn', ], '',
        'http://nbn-resolving.org/urn:nbn:de:bvb:19-146642'),
    ('urn:lex:eu:council:directive:2010-03-09;2010-19-UE', ['urn', ], '', ''),
    ('ark:/13030/tqb3kh97gh8w', ['ark'], '', ''),
    ('ark:/c8131/g3js3v', ['ark'], '', ''),
    ('http://www.example.org/ark:/13030/tqb3kh97gh8w', ['ark', 'url'], '', ''),
    ('10.1016/j.epsl.2011.11.037', ['doi', 'handle'],
        '10.1016/j.epsl.2011.11.037',
        'http://doi.org/10.1016/j.epsl.2011.11.037'),
    ('doi:10.1016/j.epsl.2011.11.037', ['doi', 'handle'],
        '10.1016/j.epsl.2011.11.037',
        'http://doi.org/10.1016/j.epsl.2011.11.037'),
    ('doi: 10.1016/j.epsl.2011.11.037', ['doi', 'handle'],
        '10.1016/j.epsl.2011.11.037',
        'http://doi.org/10.1016/j.epsl.2011.11.037'),
    ('DOI:10.1016/j.epsl.2011.11.037', ['doi', 'handle'],
        '10.1016/j.epsl.2011.11.037',
        'http://doi.org/10.1016/j.epsl.2011.11.037'),
    ('http://dx.doi.org/10.1016/j.epsl.2011.11.037', ['doi', 'url', ],
        '10.1016/j.epsl.2011.11.037',
        'http://doi.org/10.1016/j.epsl.2011.11.037'),
    ('https://doi.org/10.1016/j.epsl.2011.11.037', ['doi', 'url', ],
        '10.1016/j.epsl.2011.11.037',
        'http://doi.org/10.1016/j.epsl.2011.11.037'),
    ('doi.org/10.1016/j.epsl.2011.11.037', ['doi', 'handle'],
        '10.1016/j.epsl.2011.11.037',
        'http://doi.org/10.1016/j.epsl.2011.11.037'),
    (u'10.1016/üникóδé-дôΐ', ['doi', 'handle'],
        u'10.1016/üникóδé-дôΐ',
        u'http://doi.org/10.1016/üникóδé-дôΐ'),
    (u'10.1016/སྦ་བཞེད་', ['doi', 'handle'],
        u'10.1016/སྦ་བཞེད་',
        u'http://doi.org/10.1016/སྦ་བཞེད་'),
    ('10.1002/(SICI)1521-3978(199806)46:4/5<493::AID-PROP493>3.0.CO;2-P',
        ['doi', 'handle'],
        '10.1002/(SICI)1521-3978(199806)46:4/5<493::AID-PROP493>3.0.CO;2-P',
        ('http://doi.org/'
         '10.1002/(SICI)1521-3978(199806)46:4/5<493::AID-PROP493>3.0.CO;2-P')),
    ('9783468111242', ['isbn', 'ean13'], '978-3-468-11124-2', ''),
    ('9798847781275', ['isbn', 'ean13'], '9798847781275', ''),
    ('978-65-87773-12-4', ['isbn'], '', ''),
    ('4006381333931', ['ean13'], '', ''),
    ('73513537', ['ean8'], '', ''),
    ('15626865', ['issn', 'pmid'], '1562-6865', ''),
    ('10013/epic.10033', ['handle'], '',
        'http://hdl.handle.net/10013/epic.10033'),
    ('hdl:10013/epic.10033', ['handle'], '10013/epic.10033',
        'http://hdl.handle.net/10013/epic.10033'),
    ('hdl: 10013/epic.10033', ['handle'], '10013/epic.10033',
        'http://hdl.handle.net/10013/epic.10033'),
    ('HDL:10013/epic.10033', ['handle'], '10013/epic.10033',
        'http://hdl.handle.net/10013/epic.10033'),
    ('hdl.handle.net/10013/epic.10033', ['handle'], '10013/epic.10033',
        'http://hdl.handle.net/10013/epic.10033'),
    ('http://hdl.handle.net/10013/epic.10033', ['handle', 'url'],
        '10013/epic.10033', 'http://hdl.handle.net/10013/epic.10033'),
    ('https://hdl.handle.net/10013/epic.10033', ['handle', 'url'],
        '10013/epic.10033', 'http://hdl.handle.net/10013/epic.10033'),
    ('978-3-905673-82- 1', ['isbn'], '978-3-905673-82-1', ''),
    ('978-3-905673-82-1', ['isbn'], '978-3-905673-82-1', ''),
    ('0-9752298-0-X', ['isbn'], '978-0-9752298-0-4', ''),
    ('0077-5606', ['issn'], '', ''),
    ('urn:lsid:ubio.org:namebank:11815', ['lsid', 'urn'], '', ''),
    ('0A9 2002 12B4A105 7', ['istc'], '', ''),
    ('1188-1534', ['issn'], '1188-1534', ''),
    ('12082125', ['pmid'], '12082125',
        'http://pubmed.ncbi.nlm.nih.gov/12082125'),
    ('pmid:12082125', ['pmid'], '12082125',
        'http://pubmed.ncbi.nlm.nih.gov/12082125'),
    ('https://pubmed.ncbi.nlm.nih.gov/12082125', ['pmid', 'url'], '12082125',
        'http://pubmed.ncbi.nlm.nih.gov/12082125'),
    ('https://pubmed.ncbi.nlm.nih.gov/12082125/', ['pmid', 'url'], '12082125',
        'http://pubmed.ncbi.nlm.nih.gov/12082125'),
    ('http://purl.oclc.org/foo/bar', ['purl', 'url'], '',
        'http://purl.oclc.org/foo/bar'),
    ('https://purl.fdlp.gov/GPO/gpo154197', ['purl', 'url'], '',
        'https://purl.fdlp.gov/GPO/gpo154197'),
    ('http://www.heatflow.und.edu/index2.html', ['url'], '',
        'http://www.heatflow.und.edu/index2.html'),
    ('urn:nbn:de:101:1-201102033592', ['urn'], '',
        'http://nbn-resolving.org/urn:nbn:de:101:1-201102033592'),
    ('PMC2631623', ['pmcid'], '',
        'http://www.ncbi.nlm.nih.gov/pmc/PMC2631623'),
    ('2011ApJS..192...18K', ['ads'], '',
        'http://ui.adsabs.harvard.edu/#abs/2011ApJS..192...18K'),
    ('2016arXiv161002026S', ['ads'], '',
        'http://ui.adsabs.harvard.edu/#abs/2016arXiv161002026S'),
    ('ads:2011ApJS..192...18K', ['ads'], '2011ApJS..192...18K',
        'http://ui.adsabs.harvard.edu/#abs/2011ApJS..192...18K'),
    ('ads:2017zndo....495787v', ['ads'], '2017zndo....495787v',
        'http://ui.adsabs.harvard.edu/#abs/2017zndo....495787v'),
    ('0000000218250097', ['orcid', 'isni'], '0000-0002-1825-0097',
        'http://orcid.org/0000-0002-1825-0097'),
    ('http://orcid.org/0000-0002-1825-0097', ['orcid', 'url'],
     '0000-0002-1825-0097', 'http://orcid.org/0000-0002-1825-0097'),
    ('https://orcid.org/0000-0002-1825-0097', ['orcid', 'url'],
        '0000-0002-1825-0097', 'http://orcid.org/0000-0002-1825-0097'),
    ('0000-0002-1694-233X', ['orcid', 'isni'], '0000-0002-1694-233X',
        'http://orcid.org/0000-0002-1694-233X'),
    ('0009-0005-6000-7479', ['orcid', 'isni'], '0009-0005-6000-7479',
        'http://orcid.org/0009-0005-6000-7479'),
    ('https://orcid.org/0009-0002-4767-9017', ['orcid', 'url'],
        '0009-0002-4767-9017', 'http://orcid.org/0009-0002-4767-9017'),
    ('1422-4586-3573-0476', ['isni'], '', ''),
    ('arXiv:1310.2590', ['arxiv', ], 'arXiv:1310.2590',
        'http://arxiv.org/abs/arXiv:1310.2590'),
    ('arxiv:1310.2590', ['arxiv', ], 'arXiv:1310.2590',
        'http://arxiv.org/abs/arXiv:1310.2590'),
    ('1310.2590', ['arxiv', ], 'arXiv:1310.2590',
        'http://arxiv.org/abs/arXiv:1310.2590'),
    ('math.GT/0309136', ['arxiv', ], 'arXiv:math/0309136',
        'http://arxiv.org/abs/arXiv:math/0309136'),
    ('hep-th/9901001v27', ['arxiv', ], 'arXiv:hep-th/9901001v27',
        'http://arxiv.org/abs/arXiv:hep-th/9901001v27'),
    ('arxiv:math.GT/0309136v2', ['arxiv', ], 'arXiv:math/0309136v2',
        'http://arxiv.org/abs/arXiv:math/0309136v2'),
    ('arXiv:hep-th/9901001v27', ['arxiv', ], 'arXiv:hep-th/9901001v27',
        'http://arxiv.org/abs/arXiv:hep-th/9901001v27'),
    ('9912.12345v2', ['arxiv', ], 'arXiv:9912.12345v2',
        'http://arxiv.org/abs/arXiv:9912.12345v2'),
    ('arXiv:hep-th/1601.07616', ['arxiv', ], 'arXiv:1601.07616',
        'http://arxiv.org/abs/arXiv:1601.07616'),
    ('hep-th/1601.07616', ['arxiv', ], 'arXiv:1601.07616',
        'http://arxiv.org/abs/arXiv:1601.07616'),
    ('http://d-nb.info/gnd/1055864695', ['gnd', 'url'], 'gnd:1055864695',
        'http://d-nb.info/gnd/1055864695'),
    ('GND:4079154-3', ['gnd', ], 'gnd:4079154-3',
        'http://d-nb.info/gnd/4079154-3'),
    ('4079154-3', ['gnd', ], 'gnd:4079154-3',
        'http://d-nb.info/gnd/4079154-3'),
    ('SRX3529244', ['sra', ], '',
        'http://www.ebi.ac.uk/ena/data/view/SRX3529244'),
    ('SRR6437777', ['sra', ], '',
        'http://www.ebi.ac.uk/ena/data/view/SRR6437777'),
    ('PRJNA224116', ['bioproject', ], '',
        'http://www.ebi.ac.uk/ena/data/view/PRJNA224116'),
    ('SAMN08289383', ['biosample', ], '',
        'http://www.ebi.ac.uk/ena/data/view/SAMN08289383'),
    ('ENSG00000012048', ['ensembl', ], '',
        'http://www.ensembl.org/id/ENSG00000012048'),
    ('ENSMUST00000017290', ['ensembl', ], '',
        'http://www.ensembl.org/id/ENSMUST00000017290'),
    ('P02833', ['uniprot', ], '',
        'http://purl.uniprot.org/uniprot/P02833'),
    ('Q9GYV0', ['uniprot', ], '',
        'http://purl.uniprot.org/uniprot/Q9GYV0'),
    ('NZ_JXSL01000036.1', ['refseq', ], '',
        'http://www.ncbi.nlm.nih.gov/entrez/viewer.fcgi?val='
        'NZ_JXSL01000036.1'),
    ('NM_206454', ['refseq', ], '',
        'http://www.ncbi.nlm.nih.gov/entrez/viewer.fcgi?val=NM_206454'),
    ('XM_002113800.1', ['refseq', ], '',
        'http://www.ncbi.nlm.nih.gov/entrez/viewer.fcgi?val=XM_002113800.1'),
    ('GCA_000002275.2', ['genome', ], '',
        'http://www.ncbi.nlm.nih.gov/assembly/GCA_000002275.2'),
    ('GCF_000001405.38', ['genome', ], '',
        'http://www.ncbi.nlm.nih.gov/assembly/GCF_000001405.38'),
    ('GPL9', ['geo', ], '',
        'http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL9'),
    ('GSM888', ['geo', ], '',
        'http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM888'),
    ('GSE55396', ['geo', ], '',
        'http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE55396'),
    ('GDS1234', ['geo', ], '',
        'http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GDS1234'),
    ('A-MEXP-1171', ['arrayexpress_array', ], '',
     'http://www.ebi.ac.uk/arrayexpress/arrays/A-MEXP-1171'),
    ('A-AFFY-17', ['arrayexpress_array', ], '',
     'http://www.ebi.ac.uk/arrayexpress/arrays/A-AFFY-17'),
    ('E-MEXP-1712', ['arrayexpress_experiment', ], '',
        'http://www.ebi.ac.uk/arrayexpress/experiments/E-MEXP-1712'),
    ('E-MTAB-424', ['arrayexpress_experiment', ], '',
        'http://www.ebi.ac.uk/arrayexpress/experiments/E-MTAB-424'),
    ('E-MTAB-4020', ['arrayexpress_experiment', ], '',
        'http://www.ebi.ac.uk/arrayexpress/experiments/E-MTAB-4020'),
    ('E-TABM-14', ['arrayexpress_experiment', ], '',
        'http://www.ebi.ac.uk/arrayexpress/experiments/E-TABM-14'),
    ('E-FLYC-6', ['arrayexpress_experiment', ], '',
        'http://www.ebi.ac.uk/arrayexpress/experiments/E-FLYC-6'),
    ('hal:inserm-13102590', ['hal', ], 'inserm-13102590',
        'http://hal.archives-ouvertes.fr/inserm-13102590'),
    ('inserm-13102590', ['hal', ], 'inserm-13102590',
        'http://hal.archives-ouvertes.fr/inserm-13102590'),
    ('mem_13102590', ['hal', ], 'mem_13102590',
        'http://hal.archives-ouvertes.fr/mem_13102590'),
    ('ascl:1908.011', ['ascl', ], 'ascl:1908.011', 'http://ascl.net/1908.011'),
    ('swh:1:cnt:94a9ed024d3859793618152ea559a168bbcbb5e2', ['swh', ],
        'swh:1:cnt:94a9ed024d3859793618152ea559a168bbcbb5e2',
        ('http://archive.softwareheritage.org/'
         'swh:1:cnt:94a9ed024d3859793618152ea559a168bbcbb5e2')),
    ('swh:1:dir:d198bc9d7a6bcf6db04f476d29314f157507d505', ['swh', ],
        'swh:1:dir:d198bc9d7a6bcf6db04f476d29314f157507d505',
        ('http://archive.softwareheritage.org/'
         'swh:1:dir:d198bc9d7a6bcf6db04f476d29314f157507d505')),
    ('swh:1:rev:309cf2674ee7a0749978cf8265ab91a60aea0f7d', ['swh', ],
        'swh:1:rev:309cf2674ee7a0749978cf8265ab91a60aea0f7d',
        ('http://archive.softwareheritage.org/'
         'swh:1:rev:309cf2674ee7a0749978cf8265ab91a60aea0f7d')),
    ('swh:1:rel:22ece559cc7cc2364edc5e5593d63ae8bd229f9f', ['swh', ],
        'swh:1:rel:22ece559cc7cc2364edc5e5593d63ae8bd229f9f',
        ('http://archive.softwareheritage.org/'
         'swh:1:rel:22ece559cc7cc2364edc5e5593d63ae8bd229f9f')),
    ('swh:1:snp:c7c108084bc0bf3d81436bf980b46e98bd338453', ['swh', ],
        'swh:1:snp:c7c108084bc0bf3d81436bf980b46e98bd338453',
        ('http://archive.softwareheritage.org/'
         'swh:1:snp:c7c108084bc0bf3d81436bf980b46e98bd338453')),
    (('swh:1:dir:d198bc9d7a6bcf6db04f476d29314f157507d505'
      ';origin=https://github.com/user/repo'), ['swh', ],
        ('swh:1:dir:d198bc9d7a6bcf6db04f476d29314f157507d505'
         ';origin=https://github.com/user/repo'),
        ('http://archive.softwareheritage.org/'
         'swh:1:dir:d198bc9d7a6bcf6db04f476d29314f157507d505'
         ';origin=https://github.com/user/repo')),
    ('03yrm5c26', ['ror'], '03yrm5c26', 'http://ror.org/03yrm5c26'),
    ('http://ror.org/03yrm5c26', ['ror', 'url'], '03yrm5c26',
     'http://ror.org/03yrm5c26'),
    (('swh:1:cnt:78e48f800c950530e36d3712d9e2e89673f23562'
      ';origin=https://github.com/python/cpython'
      ';visit=swh:1:snp:cd510e99a42139ed36f15a5774301c113c3e494b'
      ';anchor=swh:1:rel:ae1f6af15f3e4110616801e235873e47fd7d1977'
      ';path=/Programs/python.c;lines=12-16'), ['swh', ],
     ('swh:1:cnt:78e48f800c950530e36d3712d9e2e89673f23562'
      ';origin=https://github.com/python/cpython'
      ';visit=swh:1:snp:cd510e99a42139ed36f15a5774301c113c3e494b'
      ';anchor=swh:1:rel:ae1f6af15f3e4110616801e235873e47fd7d1977'
      ';path=/Programs/python.c;lines=12-16'),
     ('http://archive.softwareheritage.org/'
      'swh:1:cnt:78e48f800c950530e36d3712d9e2e89673f23562'
      ';origin=https://github.com/python/cpython'
      ';visit=swh:1:snp:cd510e99a42139ed36f15a5774301c113c3e494b'
      ';anchor=swh:1:rel:ae1f6af15f3e4110616801e235873e47fd7d1977'
      ';path=/Programs/python.c;lines=12-16')),
    (('swh:1:cnt:78e48f800c950530e36d3712d9e2e89673f23562'
      ';anchor=swh:1:rel:ae1f6af15f3e4110616801e235873e47fd7d1977'
      ';visit=swh:1:snp:cd510e99a42139ed36f15a5774301c113c3e494b'
      ';path=/Programs/python.c;lines=12-16'
      ';origin=https://github.com/python/cpython'), ['swh', ],
     ('swh:1:cnt:78e48f800c950530e36d3712d9e2e89673f23562'
      ';anchor=swh:1:rel:ae1f6af15f3e4110616801e235873e47fd7d1977'
      ';visit=swh:1:snp:cd510e99a42139ed36f15a5774301c113c3e494b'
      ';path=/Programs/python.c;lines=12-16'
      ';origin=https://github.com/python/cpython'),
     ('http://archive.softwareheritage.org/'
      'swh:1:cnt:78e48f800c950530e36d3712d9e2e89673f23562'
      ';anchor=swh:1:rel:ae1f6af15f3e4110616801e235873e47fd7d1977'
      ';visit=swh:1:snp:cd510e99a42139ed36f15a5774301c113c3e494b'
      ';path=/Programs/python.c;lines=12-16'
      ';origin=https://github.com/python/cpython'))
]


def test_detect_schemes():
    """Test scheme detection."""
    for i, expected_schemes, normalized_value, url_value in identifiers:
        schemes = idutils.detect_identifier_schemes(i)
        assert schemes == expected_schemes, i


def test_is_type():
    """Test type detection."""
    for i, schemes, normalized_value, url_value in identifiers:
        for s in schemes:
            assert getattr(idutils, 'is_%s' % s)(i)


def test_normalize_pid():
    """Test persistent id normalization."""
    for i, expected_schemes, normalized_value, url_value in identifiers:
        assert idutils.normalize_pid(i, expected_schemes[0]) == \
           (normalized_value or i)

    assert idutils.normalize_pid(None, 'handle') is None


def test_idempotence():
    """Test persistent id normalization."""
    for i, expected_schemes, normalized_value, url_value in identifiers:
        val_norm = idutils.normalize_pid(i, expected_schemes[0])
        assert expected_schemes[0] in \
            idutils.detect_identifier_schemes(val_norm)


def test_to_url():
    """Test URL generation."""
    for i, expected_schemes, normalized_value, url_value in identifiers:
        assert idutils.to_url(
            idutils.normalize_pid(i, expected_schemes[0]), expected_schemes[0]
        ) == url_value
        assert idutils.to_url(
            idutils.normalize_pid(i, expected_schemes[0]), expected_schemes[0],
            url_scheme='https',
        ) == (url_value.replace('http://', 'https://')
              # If the value is already a URL its scheme is preserved
              if expected_schemes[0] not in ['purl', 'url'] else url_value)


def test_valueerror():
    """Test for bad validators."""
    # Many validators rely on a special length of the identifier before
    # testing further. This test, checks that the validators are still
    # well-behaved when the length matches, but the persistent identifier
    # is invalid.
    for i in range(20):
        nonsense_pid = "a" * i
        assert idutils.detect_identifier_schemes(nonsense_pid) == []


def test_compund_ean():
    """Test EAN validation."""
    assert idutils.is_ean('4006381333931')
    assert idutils.is_ean('73513537')


def test_compund_isbn():
    """Test ISBN validation."""
    assert idutils.is_isbn('978-3-905673-82-1')
    assert idutils.is_isbn13('978-3-905673-82-1')
    assert not idutils.is_isbn10('978-3-905673-82-1')
    assert idutils.is_isbn('0-9752298-0-X')
    assert not idutils.is_isbn13('0-9752298-0-X')
    assert idutils.is_isbn10('0-9752298-0-X')


def test_doi():
    """Test DOI validation."""
    assert idutils.is_doi('10.1000/123456')
    assert idutils.is_doi('10.1038/issn.1476-4687')
    assert idutils.is_doi('10.1000.10/123456')
    assert not idutils.is_doi('10.1000/')
    assert not idutils.is_doi('10.10O0/123456')
    assert not idutils.is_doi('10.1.NOTGOOD.0/123456')


def test_ascl():
    """Test ASCL validation."""
    assert idutils.is_ascl('ascl:1908.011')
    assert idutils.is_ascl('ascl:1908.0113')
    assert not idutils.is_ascl('1990.0803')
