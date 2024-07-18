#!/usr/bin/python3
# -*- coding: utf-8 -*-

from fabric.api import *
import os

env.hosts = ['35.153.98.214', '18.204.13.20']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if not os.path.exists(archive_path):
        return False

    # Get the archive file name and its base name
    archive_file = os.path.basename(archive_path)
    base_name = os.path.splitext(archive_file)[0]

     # Define the target directory and path
    remote_tmp_path = "/tmp/{}".format(archive_file)
    remote_release_dir = "/data/web_static/releases/{}".format(base_name)

    try:
        # Upload the archive to the /tmp/ directory on the web server
        # put('path/to/your/archive.tar.gz', '/tmp/')
        put(archive_path, remote_tmp_path)

        # create the target directory if it doesn't exist
        sudo("mkdir -p {}".format(remote_release_dir))

        # Uncompress the archive to the folder
        # run('tar -xzvf /tmp/archive.tar.gz -C /path/to/destination/folder/')
        sudo("tar -xzf {} -C {}".format(remote_tmp_path, remote_release_dir))

        # Delete the archive from the web server
        # ('rm /path/to/your/archive.tar.gz')
        sudo("rm -rf {}".format(archive_path))

        # Create a new the symbolic link
        # remove the previous link and create a new one
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {} /data/web_static/current".format(remote_release_dir))

        return True
    except Exception as e:
        return False
