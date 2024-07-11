#!/usr/bin/python3
# -*- coding: utf-8 -*-

from fabric.api import local
from datetime import datetime
import os

"""
    ##########################################################################
    # 1-pack_web_static.py: is a python script that                          #
    # tires to merge the two beautiful words of fabric                       #
    # and python, with the main of create a backup for                       #
    # the folder stated below.                                               #
    # REQUIREMENTS:                                                          #
    #-> Prototype: def do_pack():                                            #
    #-> All files in the folder web_static must be added to d final archive  #
    #-> All archives must be stored in the folder versions                   #
    #    (your function should create this folder if it doesn’t exist)       #
    #-> The name of the archive created must be                              #
    #   web_static_<year><month><day><hour><minute><second>.tgz              #
    #-> The function do_pack must return the archive path if the             #
    # archive has been correctly generated. Otherwise, it should return None #
    ##########################################################################
"""


def do_pack():
    # Creates a dir on the local machine
    local("mkdir -p versions")

    # Using python datime module one can retrieve the current
    # Date time object, finally a conversion is made
    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Using string subtitution the format is used
    file_name = "versions/web_static_{}.tgz".format(time_stamp)

    # A compressed file is generated on the local machine
    local("tar -cvzf {} ./web_static".format(file_name))

    # A try and except is used here for, when working with files
    # there's the possiblity that the file does not exist.
    try:
        print("web_static packed: {} -> {}Bytes".format(
            file_name, os.stat(file_name).st_size))
    except Exception as bugfixdotexe:
        return None
