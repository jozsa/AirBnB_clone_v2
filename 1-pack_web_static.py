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
    filename = now.strftime('%Y%m%d%H%S')
    exitcode = local("tar -cpvf versions/web_static{}.tgz\
                     web_static".format(filename))
    if exitcode == 0:
        return filename
    else:
        return None
