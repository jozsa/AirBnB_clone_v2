#!/usr/bin/python3
"""do_deploy()

Deploys the archived path/file to server
"""
import os.path
from fabric.api import *
from datetime import datetime

env.hosts = ['35.196.140.92',
             '35.237.19.12']


def do_deploy(archive_path):
    """
    Deploy archive_path to server
    """
    if not os.path.exists(archive_path):
        return False
    upload = put("{}".format(archive_path), "/tmp/")
    if upload.failed:
        return False
    filename = archive_path.partition('/')[2]
    createdir = run("mkdir -p /data/web_static/releases/{}/"
                    .format(filename[:-4]))
    if createdir.failed:
        return False
    extract = run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
                  .format(filename, filename[:-4]))
    if extract.failed:
        return False
    deletetmp = run("rm /tmp/{}".format(filename))
    if deletetmp.failed:
        return False
    move = run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/"
               .format(filename[:-4], filename[:-4]))
    if move.failed:
        return False
    deleteweb = run("rm -rf /data/web_static/releases/{}/web_static"
                    .format(filename[:-4]))
    if deleteweb.failed:
        return False
    deletecurrent = run("rm -rf /data/web_static/current")
    if deletecurrent.failed:
        return False
    symlink = run(
        "ln -s /data/web_static/releases/{}/ /data/web_static/current"
        .format(filename[:-4]))
    if symlink.failed:
        return False
    return True
