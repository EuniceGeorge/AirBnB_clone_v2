!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Fabric script that generates a\
.tgz archive from the contents of\
the web_static folder of your AirBnB Clone repo,\
using the function do_pack."""

from fabric.api import local
from datetime import datetime

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    # Create versions folder if it doesn't exist
    local("mkdir -p versions")

    # Generate the archive name with the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(timestamp)

    # Create the archive
    result = local("tar -cvzf {} web_static".format(archive_name))

    try:
        result
        return archive_name
    except e as Exception:
        return None
