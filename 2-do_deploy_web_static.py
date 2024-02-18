#!/usr/bin/python3
"""
    Fabric script that distributes an archive to your web servers using the
    function do_deploy.
"""
from fabric.api import env, put, run, local
from os.path import exists, isfile
from datetime import datetime

env.hosts = ['52.87.3.107', '52.87.219.206']

if __name__ == "__main__":
    def do_deploy(archive_path):
        """ distributes an archive to your web servers """

        try:
            archive_name = archive_path.split('/')[-1]
            remote_path = '/tmp/{}'.format(archive_name)
            put(archive_path, remote_path)


