#!/usr/bin/python3
"""do_pack()

One function: Compresses/archives a folder
and stores it in another folder.
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """
    Archives web_static folder and stores it
    in a folder called 'versions'.

    Returns archive path if correctly generated,
    otherwise None.
    """
    local("mkdir -p versions")
    now = datetime.now()
    filename = "versions/web_static_{}.tgz".format(now.strftime('%Y%m%d%H%M%S'))
    with settings(warn_only=True):
        exitstatus = local("tar -cpvf {} web_static".format(filename))
        if exitstatus.return_code == 0:
            return filename
        else:
            return None
