#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################
#    nikw Copyright (C) 2021 suizokukan
#    Contact: suizokukan _A.T._ orange dot fr
#
#    This file is part of nikw.
#    nikw is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    nikw is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with nikw.  If not, see <http://www.gnu.org/licenses/>.
################################################################################
"""
        nikw project : hashfuncs.py
"""
import base64
import hashlib


def hashfunction():
    return hashlib.sha3_512()


def hash__str_to_binhash(string):
    return hashlib.sha3_512(string.encode()).digest()


def strb85_to_binhash(string):
    """
        pimydoc:modified base85
        “ Default Ascii85 specifications:
        “ https://fr.wikipedia.org/wiki/Ascii85
        “
        “ Default Ascii85 characters: 0–9, A–Z, a–z, !#$%&()*+-;<=>?@^_`{|}~
        “ Modified base85 characters: 0–9, A–Z, a–z, !#.%&()*+-,<=>?@^_/{|}~
        “
        “ NB : ';' is replaced by ',' due to a problem with StrQuasiDictCommandString strings
        “ NB : '$' is replaced by '.' due to a problem with command line options
        “ NB : '`' is replaced by '/' due to a problem with command line options
        “
    """
    string = string.replace(",", ";")
    string = string.replace(".", "$")
    string = string.replace("/", "`")
    return base64.b85decode(string.encode())


def binhash_to_strb85(_bytes, maxlen=None):
    """
    TODO
    la chaîne en sortie doit pouvoir être utilisée sur la ligne de commande comme option
    ET comme nom de fichier.

        pimydoc:modified base85
        “ Default Ascii85 specifications:
        “ https://fr.wikipedia.org/wiki/Ascii85
        “
        “ Default Ascii85 characters: 0–9, A–Z, a–z, !#$%&()*+-;<=>?@^_`{|}~
        “ Modified base85 characters: 0–9, A–Z, a–z, !#æ%&()ë+-,<=>?@^_°{|}~
        “
        “ NB : ';' is replaced by ',' due to a problem with StrQuasiDictCommandString strings
        “ NB : '$' is replaced by 'æ' due to a problem with command line options
        “ NB : '`' is replaced by '°' due to a problem with command line options
        “ NB : '*' is replaced by 'ë' due to a problem with filenames
        “
    """
    string = base64.b85encode(_bytes).decode()
    string = string.replace(";", ",")
    string = string.replace("$", "æ")
    string = string.replace("`", "°")
    string = string.replace("*", "ë")

    if maxlen is None:
        return string

    return string[:maxlen]+"…"
