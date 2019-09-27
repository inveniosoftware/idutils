# -*- coding: utf-8 -*-
#
# This file is part of IDUtils
# Copyright (C) 2015-2019 CERN.
# Copyright (C) 2018 Alan Rubin.
# Copyright (C) 2019 Inria.
#
# IDUtils is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

"""Small library for persistent identifiers used in scholarly communication."""

from __future__ import absolute_import, print_function

import re

from isbn import ISBN
from six.moves.urllib.parse import urlparse

from .version import __version__

ENSEMBL_PREFIXES = (
    "ENSPMA",  # Petromyzon marinus (Lamprey)
    "ENSNGA",  # Nannospalax galili (Upper Galilee mountains blind mole rat)
    "ENSOPR",  # Ochotona princeps (Pika)
    "ENSMNE",  # Macaca nemestrina (Pig-tailed macaque)
    "MGP_C57BL6NJ_",  # Mus musculus (Mouse C57BL/6NJ)
    "MGP_LPJ_",  # Mus musculus (Mouse LP/J)
    "FB",  # Drosophila melanogaster (Fruitfly)
    "ENSORL",  # Oryzias latipes (Medaka)
    "ENSONI",  # Oreochromis niloticus (Tilapia)
    "ENSOCU",  # Oryctolagus cuniculus (Rabbit)
    "ENSXET",  # Xenopus tropicalis (Xenopus)
    "ENSRRO",  # Rhinopithecus roxellana (Golden snub-nosed monkey)
    "ENSCAT",  # Cercocebus atys (Sooty mangabey)
    "ENSAME",  # Ailuropoda melanoleuca (Panda)
    "MGP_CASTEiJ_",  # Mus musculus castaneus (Mouse CAST/EiJ)
    "ENSCSAV",  # Ciona savignyi
    "ENSMAU",  # Mesocricetus auratus (Golden Hamster)
    "ENSFAL",  # Ficedula albicollis (Flycatcher)
    "ENSTRU",  # Takifugu rubripes (Fugu)
    "ENSPTR",  # Pan troglodytes (Chimpanzee)
    "ENSTTR",  # Tursiops truncatus (Dolphin)
    "ENSCJA",  # Callithrix jacchus (Marmoset)
    "ENSSAR",  # Sorex araneus (Shrew)
    "ENSVPA",  # Vicugna pacos (Alpaca)
    "ENSLAC",  # Latimeria chalumnae (Coelacanth)
    "ENSPVA",  # Pteropus vampyrus (Megabat)
    "ENSPAN",  # Papio anubis (Olive baboon)
    "ENSHGLF",  # Heterocephalus glaber (Naked mole-rat female)
    "MGP_PWKPhJ_",  # Mus musculus musculus (Mouse PWK/PhJ)
    "MGP_NZOHlLtJ_",  # Mus musculus (Mouse NZO/HlLtJ)
    "ENSCAF",  # Canis lupus familiaris (Dog)
    "MGP_AJ_",  # Mus musculus (Mouse A/J)
    "ENSMOD",  # Monodelphis domestica (Opossum)
    "ENSMGA",  # Meleagris gallopavo (Turkey)
    "ENSPCO",  # Propithecus coquereli (Coquerel's sifaka)
    "ENSFDA",  # Fukomys damarensis (Damara mole rat)
    "ENSBTA",  # Bos taurus (Cow)
    "ENSGAL",  # Gallus gallus (Chicken)
    "ENSLAF",  # Loxodonta africana (Elephant)
    "ENSGGO",  # Gorilla gorilla gorilla (Gorilla)
    "ENSCAP",  # Cavia aperea (Brazilian guinea pig)
    "ENSMMU",  # Macaca mulatta (Macaque)
    "ENSAPL",  # Anas platyrhynchos (Duck)
    "ENSCEL",  # Caenorhabditis elegans (Caenorhabditis elegans)
    "ENSMEU",  # Notamacropus eugenii (Wallaby)
    "ENSCGR",  # Cricetulus griseus (Chinese hamster CriGri)
    "ENSANA",  # Aotus nancymaae (Ma's night monkey)
    "ENSGMO",  # Gadus morhua (Cod)
    "ENSPEM",  # Peromyscus maniculatus bairdii (Northern American deer mouse)
    "MGP_C3HHeJ_",  # Mus musculus (Mouse C3H/HeJ)
    "ENSTGU",  # Taeniopygia guttata (Zebra Finch)
    "ENSSCE",  # Saccharomyces cerevisiae (Saccharomyces cerevisiae)
    "ENSOGA",  # Otolemur garnettii (Bushbaby)
    "ENSACA",  # Anolis carolinensis (Anole lizard)
    "ENSTSY",  # Carlito syrichta (Tarsier)
    "ENSTBE",  # Tupaia belangeri (Tree Shrew)
    "MGP_AKRJ_",  # Mus musculus (Mouse AKR/J)
    "ENSDAR",  # Danio rerio (Zebrafish)
    "ENSMUS",  # Mus musculus (Mouse)
    "ENSETE",  # Echinops telfairi (Lesser hedgehog tenrec)
    "ENSSBO",  # Saimiri boliviensis boliviensis (Bolivian squirrel monkey)
    "ENS",  # Homo sapiens (Human)
    "ENSCGR",  # Cricetulus griseus (Chinese hamster CHOK1GS)
    "ENSFCA",  # Felis catus (Cat)
    "MGP_BALBcJ_",  # Mus musculus (Mouse BALB/cJ)
    "MGP_PahariEiJ_",  # Mus pahari (Shrew mouse)
    "ENSCSA",  # Chlorocebus sabaeus (Vervet-AGM)
    "ENSCCA",  # Cebus capucinus imitator (Capuchin)
    "ENSOAR",  # Ovis aries (Sheep)
    "ENSCHI",  # Capra hircus (Goat)
    "ENSDOR",  # Dipodomys ordii (Kangaroo rat)
    "ENSCHO",  # Choloepus hoffmanni (Sloth)
    "ENSSHA",  # Sarcophilus harrisii (Tasmanian devil)
    "ENSMPU",  # Mustela putorius furo (Ferret)
    "ENSNLE",  # Nomascus leucogenys (Gibbon)
    "ENSXMA",  # Xiphophorus maculatus (Platyfish)
    "ENSSSC",  # Sus scrofa (Pig)
    "ENSEEU",  # Erinaceus europaeus (Hedgehog)
    "ENSPSI",  # Pelodiscus sinensis (Chinese softshell turtle)
    "MGP_DBA2J_",  # Mus musculus (Mouse DBA/2J)
    "ENSAMX",  # Astyanax mexicanus (Cave fish)
    "MGP_WSBEiJ_",  # Mus musculus domesticus (Mouse WSB/EiJ)
    "ENSJJA",  # Jaculus jaculus (Lesser Egyptian jerboa)
    "ENSCIN",  # Ciona intestinalis
    "ENSPPA",  # Pan paniscus (Bonobo)
    "MGP_SPRETEiJ_",  # Mus spretus (Algerian mouse)
    "ENSCAN",  # Colobus angolensis palliatus (Angola colobus)
    "MGP_NODShiLtJ_",  # Mus musculus (Mouse NOD/ShiLtJ)
    "ENSCLA",  # Chinchilla lanigera (Long-tailed chinchilla)
    "ENSCPO",  # Cavia porcellus (Guinea Pig)
    "ENSDNO",  # Dasypus novemcinctus (Armadillo)
    "ENSPFO",  # Poecilia formosa (Amazon molly)
    "ENSMIC",  # Microcebus murinus (Mouse Lemur)
    "MGP_FVBNJ_",  # Mus musculus (Mouse FVB/NJ)
    "MGP_CBAJ_",  # Mus musculus (Mouse CBA/J)
    "ENSSTO",  # Ictidomys tridecemlineatus (Squirrel)
    "ENSRNO",  # Rattus norvegicus (Rat)
    "ENSMOC",  # Microtus ochrogaster (Prairie vole)
    "ENSTNI",  # Tetraodon nigroviridis (Tetraodon)
    "ENSPPY",  # Pongo abelii (Orangutan)
    "ENSGAC",  # Gasterosteus aculeatus (Stickleback)
    "ENSLOC",  # Lepisosteus oculatus (Spotted gar)
    "ENSODE",  # Octodon degus (Degu)
    "ENSPCA",  # Procavia capensis (Hyrax)
    "ENSECA",  # Equus caballus (Horse)
    "ENSOAN",  # Ornithorhynchus anatinus (Platypus)
    "MGP_CAROLIEiJ_",  # Mus caroli (Ryukyu mouse)
    "ENSHGLM",  # Heterocephalus glaber (Naked mole-rat male)
    "MGP_129S1SvImJ_",  # Mus musculus (Mouse 129S1/SvImJ)
    "ENSRBI",  # Rhinopithecus bieti (Black snub-nosed monkey)
    "ENSMLU",  # Myotis lucifugus (Microbat)
    "ENSMLE",  # Mandrillus leucophaeus (Drill)
    "ENSMFA",  # Macaca fascicularis (Crab-eating macaque)
)
"""List of species-specific prefixes for Ensembl accession numbers."""

doi_regexp = re.compile(
    "(doi:\s*|(?:https?://)?(?:dx\.)?doi\.org/)?(10\.\d+(.\d+)*/.+)$",
    flags=re.I
)
"""See http://en.wikipedia.org/wiki/Digital_object_identifier."""

handle_regexp = re.compile(
    "(hdl:\s*|(?:https?://)?hdl\.handle\.net/)?"
    "([^/\.]+(\.[^/\.]+)*/.*)$",
    flags=re.I
)
"""See http://handle.net/rfc/rfc3651.html.

<Handle>          = <NamingAuthority> "/" <LocalName>
<NamingAuthority> = *(<NamingAuthority>  ".") <NAsegment>
<NAsegment>       = Any UTF8 char except "/" and "."
<LocalName>       = Any UTF8 char
"""

arxiv_post_2007_regexp = re.compile(
    "(arxiv:)?(\d{4})\.(\d{4,5})(v\d+)?$",
    flags=re.I
)
"""See http://arxiv.org/help/arxiv_identifier and
       http://arxiv.org/help/arxiv_identifier_for_services."""

arxiv_pre_2007_regexp = re.compile(
    "(arxiv:)?([a-z\-]+)(\.[a-z]{2})?(/\d{4})(\d+)(v\d+)?$",
    flags=re.I
)
"""See http://arxiv.org/help/arxiv_identifier and
       http://arxiv.org/help/arxiv_identifier_for_services."""

arxiv_post_2007_with_class_regexp = re.compile(
    "(arxiv:)?(?:[a-z\-]+)(?:\.[a-z]{2})?/(\d{4})\.(\d{4,5})(v\d+)?$",
    flags=re.I
)
"""Matches new style arXiv ID, with an old-style class specification;
    technically malformed, however appears in real data."""

hal_regexp = re.compile(
    "(hal:|HAL:)?([a-z]{3}[a-z]*-|(sic|mem|ijn)_)\d{8}(v\d+)?$"
    )
"""Matches HAL identifiers (sic mem and ijn are old identifiers form)."""

ads_regexp = re.compile("(ads:|ADS:)?(\d{4}[A-Za-z]\S{13}[A-Za-z.:])$")
"""See http://adsabs.harvard.edu/abs_doc/help_pages/data.html"""

pmcid_regexp = re.compile("PMC\d+$", flags=re.I)
"""PubMed Central ID regular expression."""

pmid_regexp = re.compile("(pmid:)?(\d+)$", flags=re.I)
"""PubMed ID regular expression."""

ark_suffix_regexp = re.compile("ark:/\d+/.+$")
"""See http://en.wikipedia.org/wiki/Archival_Resource_Key and
       https://confluence.ucop.edu/display/Curation/ARK."""

lsid_regexp = re.compile("urn:lsid:[^:]+(:[^:]+){2,3}$", flags=re.I)
"""See http://en.wikipedia.org/wiki/LSID."""

orcid_urls = ["http://orcid.org/", "https://orcid.org/"]

gnd_regexp = re.compile(
    "(gnd:|GND:)?("
    "(1|10)\d{7}[0-9X]|"
    "[47]\d{6}-\d|"
    "[1-9]\d{0,7}-[0-9X]|"
    "3\d{7}[0-9X]"
    ")")
"""See https://www.wikidata.org/wiki/Property:P227."""

gnd_resolver_url = "http://d-nb.info/gnd/"

sra_regexp = re.compile("[SED]R[APRSXZ]\d+$")
"""Sequence Read Archive regular expression."""

bioproject_regexp = re.compile("PRJ(NA|EA|EB|DB)\d+$")
"""BioProject regular expression."""

biosample_regexp = re.compile("SAM(N|EA|D)\d+$")
"""BioSample regular expression."""

ensembl_regexp = re.compile("({prefixes})(E|FM|G|GT|P|R|T)\d{{11}}$".format(
    prefixes="|".join(ENSEMBL_PREFIXES)))
"""Ensembl regular expression."""

uniprot_regexp = re.compile("([A-N,R-Z][0-9]([A-Z][A-Z,0-9]{2}[0-9]){1,2})|"
                            "([O,P,Q][0-9][A-Z,0-9]{3}[0-9])(\.\d+)?$")
"""UniProt regular expression."""

refseq_regexp = re.compile("((AC|NC|NG|NT|NW|NM|NR|XM|XR|AP|NP|YP|XP|WP)_|"
                           "NZ_[A-Z]{4})\d+(\.\d+)?$")
"""RefSeq regular expression."""

genome_regexp = re.compile("GC[AF]_\d+\.\d+$")
"""GenBank or RefSeq genome assembly accession."""

ascl_regexp = re.compile("^ascl:[0-9]{4}\.[0-9]{3,4}$", flags=re.I)
"""ASCL regular expression."""


def _convert_x_to_10(x):
    """Convert char to int with X being converted to 10."""
    return int(x) if x != 'X' else 10


def is_isbn10(val):
    """Test if argument is an ISBN-10 number.

    Courtesy Wikipedia:
    http://en.wikipedia.org/wiki/International_Standard_Book_Number
    """
    val = val.replace("-", "").replace(" ", "").upper()
    if len(val) != 10:
        return False
    try:
        r = sum([(10 - i) * (_convert_x_to_10(x)) for i, x in enumerate(val)])
        return not (r % 11)
    except ValueError:
        return False


def is_isbn13(val):
    """Test if argument is an ISBN-13 number.

    Courtesy Wikipedia:
    http://en.wikipedia.org/wiki/International_Standard_Book_Number
    """
    val = val.replace("-", "").replace(" ", "").upper()
    if len(val) != 13:
        return False
    try:
        total = sum([
            int(num) * weight for num, weight in zip(val, (1, 3) * 6)
        ])
        ck = (10 - total) % 10
        return ck == int(val[-1])
    except ValueError:
        return False


def is_isbn(val):
    """Test if argument is an ISBN-10 or ISBN-13 number."""
    if is_isbn10(val) or is_isbn13(val):
        if val[0:3] in ["978", "979"] or not is_ean13(val):
            return True
    return False


def is_issn(val):
    """Test if argument is an ISSN number."""
    try:
        val = val.replace("-", "").replace(" ", "").upper()
        if len(val) != 8:
            return False
        r = sum([(8 - i) * (_convert_x_to_10(x)) for i, x in enumerate(val)])
        return not (r % 11)
    except ValueError:
        return False


def is_istc(val):
    """Test if argument is a International Standard Text Code.

    See http://www.istc-international.org/html/about_structure_syntax.aspx
    """
    val = val.replace("-", "").replace(" ", "").upper()
    if len(val) != 16:
        return False
    sequence = [11, 9, 3, 1]
    try:
        r = sum([int(x, 16)*sequence[i % 4] for i, x in enumerate(val[:-1])])
        ck = hex(r % 16)[2:].upper()
        return ck == val[-1]
    except ValueError:
        return False


def is_doi(val):
    """Test if argument is a DOI."""
    return doi_regexp.match(val)


def is_handle(val):
    """Test if argument is a Handle.

    Note, DOIs are also handles, and handle are very generic so they will also
    match e.g. any URL your parse.
    """
    return handle_regexp.match(val)


def is_ean8(val):
    """Test if argument is a International Article Number (EAN-8)."""
    if len(val) != 8:
        return False
    sequence = [3, 1]
    try:
        r = sum([int(x)*sequence[i % 2] for i, x in enumerate(val[:-1])])
        ck = (10 - r % 10) % 10
        return ck == int(val[-1])
    except ValueError:
        return False


def is_ean13(val):
    """Test if argument is a International Article Number (EAN-13)."""
    if len(val) != 13:
        return False
    sequence = [1, 3]
    try:
        r = sum([int(x)*sequence[i % 2] for i, x in enumerate(val[:-1])])
        ck = (10 - r % 10) % 10
        return ck == int(val[-1])
    except ValueError:
        return False


def is_ean(val):
    """Test if argument is a International Article Number (EAN-13 or EAN-8).

    See http://en.wikipedia.org/wiki/International_Article_Number_(EAN).
    """
    return is_ean13(val) or is_ean8(val)


def is_isni(val):
    """Test if argument is an International Standard Name Identifier."""
    val = val.replace("-", "").replace(" ", "").upper()
    if len(val) != 16:
        return False
    try:
        r = 0
        for x in val[:-1]:
            r = (r + int(x))*2
        ck = (12 - r % 11) % 11
        return ck == _convert_x_to_10(val[-1])
    except ValueError:
        return False


def is_orcid(val):
    """Test if argument is an ORCID ID.

    See http://support.orcid.org/knowledgebase/
        articles/116780-structure-of-the-orcid-identifier
    """
    for orcid_url in orcid_urls:
        if val.startswith(orcid_url):
            val = val[len(orcid_url):]
            break

    val = val.replace("-", "").replace(" ", "")
    if is_isni(val):
        val = int(val[:-1], 10)  # Remove check digit and convert to int.
        return val >= 15000000 and val <= 35000000
    return False


def is_ark(val):
    """Test if argument is an ARK."""
    res = urlparse(val)
    return ark_suffix_regexp.match(val) or (
        res.scheme == 'http' and
        res.netloc != '' and
        # Note res.path includes leading slash, hence [1:] to use same reexp
        ark_suffix_regexp.match(res.path[1:]) and
        res.params == ''
    )


def is_purl(val):
    """Test if argument is a PURL."""
    res = urlparse(val)
    return (res.scheme == 'http' and
            res.netloc in ['purl.org', 'purl.oclc.org', 'purl.net',
                           'purl.com'] and
            res.path != '')


def is_url(val):
    """Test if argument is a URL."""
    res = urlparse(val)
    return bool(res.scheme and res.netloc and res.params == '')


def is_lsid(val):
    """Test if argument is a LSID."""
    return is_urn(val) and lsid_regexp.match(val)


def is_urn(val):
    """Test if argument is an URN."""
    res = urlparse(val)
    return bool(res.scheme == 'urn' and res.netloc == '' and res.path != '')


def is_ads(val):
    """Test if argument is an ADS bibliographic code."""
    return ads_regexp.match(val)


def is_arxiv_post_2007(val):
    """Test if argument is a post-2007 arXiv ID."""
    return arxiv_post_2007_regexp.match(val) \
        or arxiv_post_2007_with_class_regexp.match(val)


def is_arxiv_pre_2007(val):
    """Test if argument is a pre-2007 arXiv ID."""
    return arxiv_pre_2007_regexp.match(val)


def is_arxiv(val):
    """Test if argument is an arXiv ID.

    See http://arxiv.org/help/arxiv_identifier and
        http://arxiv.org/help/arxiv_identifier_for_services.
    """
    return is_arxiv_post_2007(val) or is_arxiv_pre_2007(val)


def is_hal(val):
    """Test if argument is a HAL identifier.

    See (https://hal.archives-ouvertes.fr)
    """
    return hal_regexp.match(val)


def is_pmid(val):
    """Test if argument is a PubMed ID.

    Warning: PMID are just integers, with no structure, so this function will
    say any integer is a PubMed ID
    """
    return pmid_regexp.match(val)


def is_pmcid(val):
    """Test if argument is a PubMed Central ID."""
    return pmcid_regexp.match(val)


def is_gnd(val):
    """Test if argument is a GND Identifier."""
    if val.startswith(gnd_resolver_url):
        val = val[len(gnd_resolver_url):]

    return gnd_regexp.match(val)


def is_sra(val):
    """Test if argument is an SRA accession."""
    return sra_regexp.match(val)


def is_bioproject(val):
    """Test if argument is a BioProject accession."""
    return bioproject_regexp.match(val)


def is_biosample(val):
    """Test if argument is a BioSample accession."""
    return biosample_regexp.match(val)


def is_ensembl(val):
    """Test if argument is an Ensembl accession."""
    return ensembl_regexp.match(val)


def is_uniprot(val):
    """Test if argument is a UniProt accession."""
    return uniprot_regexp.match(val)


def is_refseq(val):
    """Test if argument is a RefSeq accession."""
    return refseq_regexp.match(val)


def is_genome(val):
    """Test if argument is a GenBank or RefSeq genome assembly accession."""
    return genome_regexp.match(val)


def is_ascl(val):
    """Test if argument is a ASCL accession."""
    return ascl_regexp.match(val)


PID_SCHEMES = [
    ('doi', is_doi),
    ('ark', is_ark),
    ('handle', is_handle),
    ('purl', is_purl),
    ('lsid', is_lsid),
    ('urn', is_urn),
    ('ads', is_ads),
    ('arxiv', is_arxiv),
    ('ascl', is_ascl),
    ('hal', is_hal),
    ('pmcid', is_pmcid),
    ('isbn', is_isbn),
    ('issn', is_issn),
    ('orcid', is_orcid),
    ('isni', is_isni),
    ('ean13', is_ean13),
    ('ean8', is_ean8),
    ('istc', is_istc),
    ('gnd', is_gnd),
    ('url', is_url),
    ('pmid', is_pmid),
    ('sra', is_sra),
    ('bioproject', is_bioproject),
    ('biosample', is_biosample),
    ('ensembl', is_ensembl),
    ('uniprot', is_uniprot),
    ('refseq', is_refseq),
    ('genome', is_genome),
]
"""Definition of scheme name and associated test function.

Order of list is important, as identifier scheme detection will test in the
order given by this list."""

SCHEME_FILTER = [
    ('ean8', ['gnd', 'pmid']),
    ('ean13', ['gnd', 'pmid']),
    ('isbn', ['gnd', 'pmid']),
    ('orcid', ['gnd', 'pmid']),
    ('isni', ['gnd', 'pmid']),
    ('issn', ['gnd', ]),
]


def detect_identifier_schemes(val):
    """Detect persistent identifier scheme for a given value.

    .. note:: Some schemes like PMID are very generic.
    """
    schemes = []
    for scheme, test in PID_SCHEMES:
        if test(val):
            schemes.append(scheme)

    for first, remove_schemes in SCHEME_FILTER:
        if first in schemes:
            schemes = list(filter(lambda x: x not in remove_schemes, schemes))

    if 'handle' in schemes and 'url' in schemes \
       and not val.startswith("http://hdl.handle.net/") \
       and not val.startswith("https://hdl.handle.net/"):
        schemes = list(filter(lambda x: x != 'handle', schemes))
    elif 'handle' in schemes and ('ark' in schemes or 'arxiv' in schemes):
        schemes = list(filter(lambda x: x != 'handle', schemes))

    return schemes


def normalize_doi(val):
    """Normalize a DOI."""
    m = doi_regexp.match(val)
    return m.group(2)


def normalize_handle(val):
    """Normalize a Handle identifier."""
    m = handle_regexp.match(val)
    return m.group(2)


def normalize_ads(val):
    """Normalize an ADS bibliographic code."""
    m = ads_regexp.match(val)
    return m.group(2)


def normalize_orcid(val):
    """Normalize an ORCID identifier."""
    for orcid_url in orcid_urls:
        if val.startswith(orcid_url):
            val = val[len(orcid_url):]
            break
    val = val.replace("-", "").replace(" ", "")

    return "-".join([val[0:4], val[4:8], val[8:12], val[12:16]])


def normalize_gnd(val):
    """Normalize a GND identifier."""
    if val.startswith(gnd_resolver_url):
        val = val[len(gnd_resolver_url):]
    if val.lower().startswith("gnd:"):
        val = val[len("gnd:"):]
    return "gnd:{0}".format(val)


def normalize_pmid(val):
    """Normalize an PubMed ID."""
    m = pmid_regexp.match(val)
    return m.group(2)


def normalize_arxiv(val):
    """Normalize an arXiv identifier."""
    if not val.lower().startswith("arxiv:"):
        val = "arXiv:{0}".format(val)
    elif val[:6] != "arXiv:":
        val = "arXiv:{0}".format(val[6:])

    # Normalize old identifiers to preferred scheme as specified by
    # http://arxiv.org/help/arxiv_identifier_for_services
    # (i.e. arXiv:math.GT/0309136 -> arXiv:math/0309136)
    m = is_arxiv_pre_2007(val)
    if m and m.group(3):
        val = "".join(m.group(1, 2, 4, 5))
        if m.group(6):
            val += m.group(6)

    m = is_arxiv_post_2007(val)
    if m:
        val = 'arXiv:' + '.'.join(m.group(2, 3))
        if m.group(4):
            val += m.group(4)
    return val


def normalize_hal(val):
    """Normalize a HAL identifier."""
    val = val.replace(' ', '').lower().replace('hal:', '')
    return val


def normalize_isbn(val):
    """Normalize an ISBN identifier."""
    val = val.replace(' ', '').replace('-', '').strip().upper()
    return ISBN(val).hyphen()


def normalize_issn(val):
    """Normalize an ISSN identifier."""
    val = val.replace(' ', '').replace('-', '').strip().upper()
    return '{0}-{1}'.format(val[:4], val[4:])


def normalize_pid(val, scheme):
    """Normalize an identifier.

    E.g. doi:10.1234/foo and http://dx.doi.org/10.1234/foo and 10.1234/foo
    will all be normalized to 10.1234/foo.
    """
    if not val:
        return val

    if scheme == 'doi':
        return normalize_doi(val)
    elif scheme == 'handle':
        return normalize_handle(val)
    elif scheme == 'ads':
        return normalize_ads(val)
    elif scheme == 'pmid':
        return normalize_pmid(val)
    elif scheme == 'arxiv':
        return normalize_arxiv(val)
    elif scheme == 'orcid':
        return normalize_orcid(val)
    elif scheme == 'gnd':
        return normalize_gnd(val)
    elif scheme == 'isbn':
        return normalize_isbn(val)
    elif scheme == 'issn':
        return normalize_issn(val)
    elif scheme == 'hal':
        return normalize_hal(val)
    return val


LANDING_URLS = {
    'doi': u'{scheme}://doi.org/{pid}',
    'handle': u'{scheme}://hdl.handle.net/{pid}',
    'arxiv': u'{scheme}://arxiv.org/abs/{pid}',
    'ascl': u'{scheme}://ascl.net/{pid}',
    'orcid': u'{scheme}://orcid.org/{pid}',
    'pmid': u'{scheme}://www.ncbi.nlm.nih.gov/pubmed/{pid}',
    'ads': u'{scheme}://ui.adsabs.harvard.edu/#abs/{pid}',
    'pmcid': u'{scheme}://www.ncbi.nlm.nih.gov/pmc/{pid}',
    'gnd': u'{scheme}://d-nb.info/gnd/{pid}',
    'urn': u'{scheme}://nbn-resolving.org/{pid}',
    'sra': u'{scheme}://www.ebi.ac.uk/ena/data/view/{pid}',
    'bioproject': u'{scheme}://www.ebi.ac.uk/ena/data/view/{pid}',
    'biosample': u'{scheme}://www.ebi.ac.uk/ena/data/view/{pid}',
    'ensembl': u'{scheme}://www.ensembl.org/id/{pid}',
    'uniprot': u'{scheme}://purl.uniprot.org/uniprot/{pid}',
    'refseq': u'{scheme}://www.ncbi.nlm.nih.gov/entrez/viewer.fcgi?val={pid}',
    'genome': u'{scheme}://www.ncbi.nlm.nih.gov/assembly/{pid}',
    'hal': u'{scheme}://hal.archives-ouvertes.fr/{pid}',
}
"""URL generation configuration for the supported PID providers."""


def to_url(val, scheme, url_scheme='http'):
    """Convert a resolvable identifier into a URL for a landing page.

    :param val: The identifier's value.
    :param scheme: The identifier's scheme.
    :param url_scheme: Scheme to use for URL generation, 'http' or 'https'.
    :returns: URL for the identifier.

    .. versionadded:: 0.3.0
       ``url_scheme`` used for URL generation.
    """
    pid = normalize_pid(val, scheme)
    if scheme in LANDING_URLS:
        if scheme == 'gnd' and pid.startswith('gnd:'):
            pid = pid[len('gnd:'):]
        if scheme == 'urn' and not pid.lower().startswith('urn:nbn:'):
            return ''
        if scheme == 'ascl':
            pid = val.split(':')[1]
        return LANDING_URLS[scheme].format(scheme=url_scheme, pid=pid)
    elif scheme in ['purl', 'url']:
        return pid
    return ''
