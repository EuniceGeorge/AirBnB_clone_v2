#!/usr/bin/python3
# -*- coding: utf-8 -*-

from fabric.api import local
from datetime import datetime
import os

"""A python script that uses fabric for running command locally"""
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
