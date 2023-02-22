#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .parser.run import run_cluster, run_local
# from .edit_files import edit_tools, create_config, create_cluster_config
from .parser.install import install_cluster, install_local, test_install
from .parser.usefull_function import get_version, get_last_version
from .parser.global_variables import *

NAME = "DNAnnot"
logo = DNANNOT_PATH.joinpath('dnannot_logo.png').as_posix()

__version__ = get_version()

__doc__ = """BLABLA"""

description_tools = """
    Welcome to DNAnnot version: """+__version__+""" ! Created on November 2019
    @author: Florian Charriat (INRAE), Sebastien Ravel (CIRAD), ,
    @email: florian.charriat@cirad.fr

    Please cite our github """+DOCS+"""
    Licencied under CeCill-C (http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html)
    and GPLv3 Intellectual property belongs to INRAE, CIRAD and authors.
    Documentation avail at: """+DOCS+"""
    """+get_last_version(url=DOCS, current_version=__version__)
