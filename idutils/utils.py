# -*- coding: utf-8 -*-
#
# This file is part of IDUtils
# Copyright (C) 2024 CERN.
# Copyright (C) 2023 abnf-to-regexp AUTHORS
# Copyright (C) 2025 Will Riley.
#
# IDUtils is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

"""Utility file containing ID parsers."""

import re

import isbnlib

doi_regexp = re.compile(
    r"(doi:\s*|(?:https?://)?(?:dx\.)?doi\.org/)?(10\.\d+(\.\d+)*/.+)$", flags=re.I
)
"""See http://en.wikipedia.org/wiki/Digital_object_identifier."""

handle_regexp = re.compile(
    r"(hdl:\s*|(?:https?://)?hdl\.handle\.net/)?" r"([^/.]+(\.[^/.]+)*/.*)$", flags=re.I
)
"""See http://handle.net/rfc/rfc3651.html.

<Handle>          = <NamingAuthority> "/" <LocalName>
<NamingAuthority> = *(<NamingAuthority>  ".") <NAsegment>
<NAsegment>       = Any UTF8 char except "/" and "."
<LocalName>       = Any UTF8 char
"""

arxiv_post_2007_regexp = re.compile(r"(arxiv:)?(\d{4})\.(\d{4,5})(v\d+)?$", flags=re.I)
"""See http://arxiv.org/help/arxiv_identifier and
       http://arxiv.org/help/arxiv_identifier_for_services."""

arxiv_pre_2007_regexp = re.compile(
    r"(arxiv:)?([a-z\-]+)(\.[a-z]{2})?(/\d{4})(\d+)(v\d+)?$", flags=re.I
)
"""See http://arxiv.org/help/arxiv_identifier and
       http://arxiv.org/help/arxiv_identifier_for_services."""

arxiv_post_2007_with_class_regexp = re.compile(
    r"(arxiv:)?(?:[a-z\-]+)(?:\.[a-z]{2})?/(\d{4})\.(\d{4,5})(v\d+)?$", flags=re.I
)
"""Matches new style arXiv ID, with an old-style class specification;
    technically malformed, however appears in real data."""

hal_regexp = re.compile(r"(hal:|HAL:)?([a-z]{3}[a-z]*-|(sic|mem|ijn)_)\d{8}(v\d+)?$")
"""Matches HAL identifiers (sic mem and ijn are old identifiers form)."""

ads_regexp = re.compile(r"(ads:|ADS:)?(\d{4}[A-Za-z]\S{13}[A-Za-z.:])$")
"""See http://adsabs.harvard.edu/abs_doc/help_pages/data.html"""

pmcid_regexp = re.compile(r"PMC\d+$", flags=re.I)
"""PubMed Central ID regular expression."""

pmid_regexp = re.compile(
    r"(pmid:|https?://pubmed.ncbi.nlm.nih.gov/)?(\d+)/?$", flags=re.I
)
"""PubMed ID regular expression."""

ark_suffix_regexp = re.compile(r"ark:/[0-9bcdfghjkmnpqrstvwxz]+/.+$")
"""See http://en.wikipedia.org/wiki/Archival_Resource_Key and
       https://confluence.ucop.edu/display/Curation/ARK."""

lsid_regexp = re.compile(r"urn:lsid:[^:]+(:[^:]+){2,3}$", flags=re.I)
"""See http://en.wikipedia.org/wiki/LSID."""

orcid_urls = ["http://orcid.org/", "https://orcid.org/"]
orcid_isni_ranges = [
    (15_000_000, 35_000_000),
    (900_000_000_000, 900_100_000_000),
]
"""Valid ORCiD ISNI block ranges.

See
    https://support.orcid.org/hc/en-us/articles/360006897674-Structure-of-the-ORCID-Identifier
"""

gnd_regexp = re.compile(
    r"(gnd:|GND:|https?://d-nb\.info/gnd/|d-nb\.info/gnd/)?("
    r"1[012]?\d{7}[0-9X]|"
    r"[47]\d{6}-\d|"
    r"[1-9]\d{0,7}-[0-9X]|"
    r"3\d{7}[0-9X]"
    r")"
)
"""See https://www.wikidata.org/wiki/Property:P227."""


urn_resolver_url = "https://nbn-resolving.org/"

sra_regexp = re.compile(r"[SED]R[APRSXZ]\d+$")
"""Sequence Read Archive regular expression.

See
    https://www.ncbi.nlm.nih.gov/books/NBK56913/#search.what_do_the_different_sra_accessi
"""

bioproject_regexp = re.compile(r"PRJ(NA|EA|EB|DB)\d+$")
"""BioProject regular expression.

See https://www.ddbj.nig.ac.jp/bioproject/faq-e.html#project-accession
    https://www.ebi.ac.uk/ena/submit/project-format
    https://www.ncbi.nlm.nih.gov/bioproject/docs/faq/#under-what-circumstances-is-it-n
"""

biosample_regexp = re.compile(r"SAM(N|EA|D)\d+$")
"""BioSample regular expression.

See https://www.ddbj.nig.ac.jp/biosample/faq-e.html
    https://ena-docs.readthedocs.io/en/latest/submit/samples/programmatic.html#accession-numbers-in-the-receipt-xml
    https://www.ncbi.nlm.nih.gov/biosample/docs/submission/faq/
"""


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
"""List of species-specific prefixes for Ensembl accession numbers.

Used for building ensembl_regexp.

See https://asia.ensembl.org/info/genome/stable_ids/prefixes.html
"""

ensembl_regexp = re.compile(
    r"({prefixes})(E|FM|G|GT|P|R|T)\d{{11}}$".format(
        prefixes="|".join(ENSEMBL_PREFIXES)
    )
)
"""Ensembl regular expression.

See https://asia.ensembl.org/info/genome/stable_ids/prefixes.html
"""

uniprot_regexp = re.compile(
    r"([A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2})|"
    r"([OPQ][0-9][A-Z0-9]{3}[0-9])(\.\d+)?$"
)
"""UniProt regular expression.

See https://www.uniprot.org/help/accession_numbers
"""

refseq_regexp = re.compile(
    r"((AC|NC|NG|NT|NW|NM|NR|XM|XR|AP|NP|YP|XP|WP)_|" r"NZ_[A-Z]{4})\d+(\.\d+)?$"
)
"""RefSeq regular expression.

See https://academic.oup.com/nar/article/44/D1/D733/2502674 (Table 1)
"""

genome_regexp = re.compile(r"GC[AF]_\d+\.\d+$")
"""GenBank or RefSeq genome assembly accession.

See https://www.ebi.ac.uk/ena/browse/genome-assembly-database
"""

geo_regexp = re.compile(r"G(PL|SM|SE|DS)\d+$")
"""Gene Expression Omnibus (GEO) accession.

See https://www.ncbi.nlm.nih.gov/geo/info/overview.html#org
"""

ARRAYEXPRESS_CODES = (
    "AFFY",
    "AFMX",
    "AGIL",
    "ATMX",
    "BAIR",
    "BASE",
    "BIOD",
    "BUGS",
    "CAGE",
    "CBIL",
    "DKFZ",
    "DORD",
    "EMBL",
    "ERAD",
    "FLYC",
    "FPMI",
    "GEAD",
    "GEHB",
    "GEOD",
    "GEUV",
    "HGMP",
    "IPKG",
    "JCVI",
    "JJRD",
    "LGCL",
    "MANP",
    "MARS",
    "MAXD",
    "MEXP",
    "MIMR",
    "MNIA",
    "MTAB",
    "MUGN",
    "NASC",
    "NCMF",
    "NGEN",
    "RUBN",
    "RZPD",
    "SGRP",
    "SMDB",
    "SNGR",
    "SYBR",
    "TABM",
    "TIGR",
    "TOXM",
    "UCON",
    "UHNC",
    "UMCU",
    "WMIT",
)
"""List of ArrayExpress four-letter codes.

Used for building arrayexpress_array_regexp and arrayexpress_experiment_regexp.

See https://www.ebi.ac.uk/arrayexpress/help/accession_codes.html
"""

arrayexpress_array_regexp = re.compile(
    r"A-({codes})-\d+$".format(codes="|".join(ARRAYEXPRESS_CODES))
)
"""ArrayExpress array accession.

See https://www.ebi.ac.uk/arrayexpress/help/accession_codes.html
"""

arrayexpress_experiment_regexp = re.compile(
    r"E-({codes})-\d+$".format(codes="|".join(ARRAYEXPRESS_CODES))
)
"""ArrayExpress array accession.

See https://www.ebi.ac.uk/arrayexpress/help/accession_codes.html
"""

ascl_regexp = re.compile(r"^ascl:[0-9]{4}\.[0-9]{3,4}$", flags=re.I)
"""ASCL regular expression."""


# The following code is adapted from abnf-to-regexp (https://github.com/aas-core-works/abnf-to-regexp)
# Copyright (c) 2023 abnf-to-regexp AUTHORS (see https://github.com/aas-core-works/abnf-to-regexp/blob/main/AUTHORS)
# License: MIT (https://opensource.org/licenses/MIT)
def _create_rfc3987_reg_exps():
    scheme = "[a-zA-Z][a-zA-Z0-9+\\-.]*"
    ucschar = (
        "[\\xa0-\\ud7ff\\uf900-\\ufdcf\\ufdf0-\\uffef"
        "\\U00010000-\\U0001fffd\\U00020000-\\U0002fffd"
        "\\U00030000-\\U0003fffd\\U00040000-\\U0004fffd"
        "\\U00050000-\\U0005fffd\\U00060000-\\U0006fffd"
        "\\U00070000-\\U0007fffd\\U00080000-\\U0008fffd"
        "\\U00090000-\\U0009fffd\\U000a0000-\\U000afffd"
        "\\U000b0000-\\U000bfffd\\U000c0000-\\U000cfffd"
        "\\U000d0000-\\U000dfffd\\U000e1000-\\U000efffd]"
    )
    iunreserved = f"([a-zA-Z0-9\\-._~]|{ucschar})"
    pct_encoded = "%[0-9A-Fa-f][0-9A-Fa-f]"
    sub_delims = "[!$&'()*+,;=]"
    iuserinfo = f"({iunreserved}|{pct_encoded}|{sub_delims}|:)*"
    h16 = "[0-9A-Fa-f]{1,4}"
    dec_octet = "([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"
    ipv4address = f"{dec_octet}\\.{dec_octet}\\.{dec_octet}\\.{dec_octet}"
    ls32 = f"({h16}:{h16}|{ipv4address})"
    ipv6address = (
        f"(({h16}:){{6}}{ls32}|::({h16}:){{5}}{ls32}|({h16})?::({h16}:){{4}}"
        f"{ls32}|(({h16}:)?{h16})?::({h16}:){{3}}{ls32}|(({h16}:){{,2}}{h16})?::"
        f"({h16}:){{2}}{ls32}|(({h16}:){{,3}}{h16})?::{h16}:{ls32}|(({h16}:){{,4}}"
        f"{h16})?::{ls32}|(({h16}:){{,5}}{h16})?::{h16}|(({h16}:){{,6}}{h16})?"
        "::)"
    )
    unreserved = "[a-zA-Z0-9\\-._~]"
    ipvfuture = f"[vV][0-9A-Fa-f]+\\.({unreserved}|{sub_delims}|:)+"
    ip_literal = f"\\[({ipv6address}|{ipvfuture})\\]"
    ireg_name = f"({iunreserved}|{pct_encoded}|{sub_delims})*"
    ihost = f"({ip_literal}|{ipv4address}|{ireg_name})"
    port = "[0-9]*"
    iauthority = f"({iuserinfo}@)?{ihost}(:{port})?"
    ipchar = f"({iunreserved}|{pct_encoded}|{sub_delims}|[:@])"
    isegment = f"({ipchar})*"
    ipath_abempty = f"(/{isegment})*"
    isegment_nz = f"({ipchar})+"
    ipath_absolute = f"/({isegment_nz}(/{isegment})*)?"
    ipath_rootless = f"{isegment_nz}(/{isegment})*"
    ipath_empty = f"({ipchar}){{0}}"
    ihier_part = (
        f"(//{iauthority}{ipath_abempty}|{ipath_absolute}|"
        f"{ipath_rootless}|{ipath_empty})"
    )
    iprivate = "[\\ue000-\\uf8ff\\U000f0000-\\U000ffffd\\U00100000-\\U0010fffd]"
    iquery = f"({ipchar}|{iprivate}|[/?])*"
    absolute_iri = f"{scheme}:{ihier_part}(\\?{iquery})?"
    gen_delims = "[:/?#\\[\\]@]"
    ifragment = f"({ipchar}|[/?])*"
    isegment_nz_nc = f"({iunreserved}|{pct_encoded}|{sub_delims}|@)+"
    ipath_noscheme = f"{isegment_nz_nc}(/{isegment})*"
    ipath = (
        f"({ipath_abempty}|{ipath_absolute}|{ipath_noscheme}|"
        f"{ipath_rootless}|{ipath_empty})"
    )
    irelative_part = (
        f"(//{iauthority}{ipath_abempty}|{ipath_absolute}|"
        f"{ipath_noscheme}|{ipath_empty})"
    )
    irelative_ref = f"{irelative_part}(\\?{iquery})?(\\#{ifragment})?"
    iri = f"{scheme}:{ihier_part}(\\?{iquery})?(\\#{ifragment})?"
    iri_reference = f"({iri}|{irelative_ref})"
    reserved = f"({gen_delims}|{sub_delims})"
    return {
        name: re.compile(value)
        for name, value in locals().items()
        if isinstance(value, str)
    }


rfc3987_reg_exps = _create_rfc3987_reg_exps()
""" 
A dictionary of compiled regular expressions for RFC 3987. 
The key is the grammar term and the value is the compiled regular expression. 
Some are used by SWH validation.
"""

swh_before_qualifiers_regexp = re.compile(
    r"""^
    swh:                        # scheme
    1:                          # scheme_version
    (snp|rel|rev|dir|cnt):      # object_type
    [0-9a-f]{40}                # object_id
    (?P<qualifiers>;.+)?
    $
    """,
    re.VERBOSE,
)

swh_qualifier_values_regexp = re.compile(
    r"""
    ^(?:  
        origin=(?P<origin_value>[^;]+)    # origin context qualifier
        | visit=(?P<visit>swh:1:(?:snp|rel|rev|dir|cnt):[0-9a-f]{40})  # visit context qualifier
        | anchor=(?P<anchor>swh:1:(?:snp|rel|rev|dir|cnt):[0-9a-f]{40}) # anchor context qualifier
        | path=(?P<path_value>[^;]+)      # path context qualifier
        | lines=(?P<lines>\d+(?:-\d+)?)  # lines fragment qualifier
    )$
    """,
    re.VERBOSE,
)

"""Matches Software Heritage identifiers."""

ror_regexp = re.compile(r"(?:https?://)?(?:ror\.org/)?(0\w{6}\d{2})$", flags=re.I)
"""See https://ror.org/facts/#core-components."""

viaf_urls = [
    "http://viaf.org/viaf/",
    "https://viaf.org/viaf/",
    "http://www.viaf.org/viaf/",
    "https://www.viaf.org/viaf/",
]

viaf_regexp = re.compile(
    r"(viaf:|VIAF:)?([1-9]\d(?:\d{0,7}|\d{17,20}))($|\/|\?|#)",
    flags=re.I,
)
"""See https://www.wikidata.org/wiki/Property:P214."""


def _convert_x_to_10(x):
    """Convert char to int with X being converted to 10."""
    return int(x) if x != "X" else 10


is_isbn10 = isbnlib.is_isbn10
"""Test if argument is an ISBN-10 number."""

is_isbn13 = isbnlib.is_isbn13
"""Test if argument is an ISBN-13 number."""

email_regexp = re.compile(r"\S+@(\S+\.)+\S+")
"""Test to see if this looks like an email address."""

sha1_regexp = re.compile(r"^[a-fA-F0-9]{40}$")
"""See https://www.w3.org/TR/annotation-model/#agents."""
