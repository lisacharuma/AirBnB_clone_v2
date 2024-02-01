#!/usr/bin/python3
"""
    abric script that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """
        generates a .tgz archive
    """
    try:
        local("mkdir -p versions")

        time_format = "%Y%m%d%H%M%S"
        archive_name = "web_static_{}.tgz".format(
                datetime.utcnow().strftime(time_format)
        )
        local("tar -cvzf versions/{} web_static".format(archive_name))
        return os.path.join("versions", archive_name)
    except Exception as e:
        return None
