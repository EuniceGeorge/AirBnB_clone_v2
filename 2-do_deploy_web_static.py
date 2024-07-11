#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from datetime import datetime
from fabric.api import sudo, env

"""
    #################################################################################
    # 2-do_deploy_web_static.py: is a python script that distributes an             #
    # archive to your a web server(s), using the function do_deploy                 #
    # REQUIREMENTS:                                                                 #
    # -> Prototype: def do_deploy(archive_path):                                    #
    #-> Returns False if the file at the path archive_path doesn’t exist            #
    #-> The script should take the following steps:                                 #
    #   * Upload the archive to the /tmp/ directory of the web server               # 
    #   * Uncompress the archive to the folder                                      #
    #        /data/web_static/releases/<archive filename without extension>         #
    #        on the web server                                                      #
    #   * Delete the archive from the web server                                    #
    #   * Delete the symbolic link /data/web_static/current from the web server     #
    #   * Create a new the symbolic link /data/web_static/current on the web        #
    #       server, linked to the new version of your code                          #
    #       (/data/web_static/releases/<archive filename without extension>)        #
    #-> All remote commands must be executed on your both web servers               #
    #     (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)  #
    #-> Returns True if all operations have been done correctly,                    #
    #    otherwise returns False                                                    #
    #-> You must use this script to deploy it on your servers:                      #
    #    xx-web-01 and xx-web-02                                                    #
    #################################################################################
"""

env.user = 'ubuntu'
env.hosts = ['100.25.29.153', '54.197.46.53']

def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False
    sudo(f"mkdir -p ~/ok")
    return True
