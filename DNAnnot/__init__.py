#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from DNAnnot.global_variables import *
from pathlib import Path
from .global_variables import GIT_URL, DOCS, DATATEST_URL_FILES, SINGULARITY_URL_FILES

logo = Path(__file__).parent.resolve().joinpath('DNAnnot_logo.png').as_posix()

__version__ = Path(__file__).parent.resolve().joinpath("VERSION").open("r").readline().strip()


__doc__ = """BLABLA"""

description_tools = f"""
    Welcome to DNAnnot version: {__version__} ! Created on November 2019
    @author: Florian Charriat (INRAE), Sebastien Ravel (CIRAD)
    @email: florian.charriat@cirad.fr, Sebastien.ravel@cirad.fr

    Please cite our github: GIT_URL
    and GPLv3 Intellectual property belongs to CIRAD and authors.
    Documentation avail at: DOCS"""

dico_tool = {
    "soft_path": Path(__file__).resolve().parent.as_posix(),
    "url": GIT_URL,
    "docs": DOCS,
    "description_tool": description_tools,
    "singularity_url_files": SINGULARITY_URL_FILES,
    "datatest_url_files": DATATEST_URL_FILES
}
