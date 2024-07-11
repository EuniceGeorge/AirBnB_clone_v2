#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" A Python script that aims to allow the compression of a file
    and uses dateandtime as a means of showing most recent backup
"""
from fabric.api import local, put, env
from datetime import datetime
import os

# Fabric commands
# Set env variables user and hosts
env.user = 'ubuntu'
env.hosts = ["100.25.29.153", "54.197.46.53"]


def do_deploy(archive_path):
    """do_deploy: a function that acomplishes the above requirements"""
    try:
        if not os.path.isfile(archive_path):
            return False
        # Upload a tar archive of an application
        put(archive_path, "/tmp/")

        # TODO: Add a check if file upload was OK

        # If 200 OK, begin uncompression
        file_path = archive_path.split(".")[0]
        archive_file_name = f'/data/web_static/releases/{file_path}'

        # --------- Fabric commands begins here -------------------
        # Create a directory on server
        sudo(f"mkdir /data/web_static/releases/{file_path}")
        # Uncompress the uploaded tar file
        sudo(f"tar -xf {archive_path} -C {archive_file_name}")
        # if OK then remove the archieve file
        sudo(f"rm {archive_path}")
        # Unlink the pervious link
        sudo("unlink {}".format("/data/web_static/current"))
        # Create a new link
        sudo(f"ln -s {archive_file_name} /data/web_static/current")
        # -----------Fabric commands ends here -------------------
    except Exception as bugfixdotexe:
        return False
