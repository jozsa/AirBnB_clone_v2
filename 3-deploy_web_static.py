#!/usr/bin/python3
"""deploy()

Calls do_pack and do_deploy
and returns the result from both
"""
import os.path
from fabric.api import *
from datetime import datetime
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

env.hosts = ['35.196.140.92',
             '35.237.19.12']


def deploy():
    """
    Archives a folder, deploys it to a server
    and returns either True or False depending
    on the result of do_deploy()
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    result = do_deploy(archive_path)
    return result
