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
    Welcome to Annotator version: """+__version__+""" ! Created on November 2019
    @author: Florian Charriat (INRAE), Sebastien Ravel (CIRAD), ,
    @email: florian.charriat@inrae.fr; sebastien.ravel@cirad.fr

    Please cite our github """+DOCS+"""
    Licencied under CeCill-C (http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html)
    and GPLv3 Intellectual property belongs to INRAE, CIRAD and authors.
    Documentation avail at: """+DOCS+"""
    """+get_last_version(url=DOCS, current_version=__version__)

MODULE_FILE = f"""
#%Module1.0
##

## Required internal variables
set     prefix       {DNANNOT_PATH.as_posix()}
set     version      {__version__}

# check if install directory exist
if {{![file exists $prefix]}} {{
    puts stderr "\t[module-info name] Load Error: $prefix does not exist"
    break
    exit 1
}}

## List conflicting modules here
conflict {NAME}

## List prerequisite modules here
module load graphviz/2.40.1

set		fullname	{NAME}-{__version__}
set		externalurl	"\n\t{DOCS}\n"
set		description	"\n\t{__doc__}"

## Required for "module help ..."
proc ModulesHelp {{}} {{
  global description externalurl
  puts stderr "Description - $description"
  puts stderr "More Docs   - $externalurl"
}}

## Required for "module display ..." and SWDB
module-whatis   "loads the [module-info name] environment"

## Software-specific settings exported to user environment

prepend-path PATH $prefix

"""
