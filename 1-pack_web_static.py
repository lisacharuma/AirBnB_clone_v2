#!/usr/bin/python3
from fabric.api import local
from time import strftime

def do_pack():
    """Archives the contents of web_static folder"""
    fname = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/".format(fname))
        return "versions/web_static_{}.tgz".format(fname)
    except Exception as e:
        return None
