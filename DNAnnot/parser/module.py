#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from .global_variable import *

def get_install_mode():
    """detect install mode"""
    if DNANNOT_MODE.exists():
        return DNANNOT_MODE.open("r").readline().strip()
    else:
        return "notInstall"

def get_dir(path):
    """List of directory included on folder"""
    return [elm.name for elm in Path(path).glob("*") if elm.is_dir()]
