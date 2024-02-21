#!/usr/bin/python3
"""Compresses web static package"""
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ["54.157.160.208", "54.160.121.210"]
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_deploy(archive_path):
    """ Deploys achive to server"""
     try:
         if not (path.exists(archive_path)):
             return False
         #path exists, upload
         put(archive_path, '/tmp/')

         # create target directory if it does not exist
         run('sudo mkdir -p /data/web_static/releases/')

         # extract archive to releases directory
         timestamp = archive_path[-18:-4]
         run('sudo tar -xzf /tmp/web_static_{}.tgz -C /data/web_static/releases/'.format(timestamp))

         # rename extracted directory
         run('sudo mv /data/web_static/releases/web_static /data/web_static/releases/web_static_{}/'.format(timestamp))
         # remove archive
         run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

         # delete pre-existing sym link
         run('sudo rm -rf /data/web_static/current')

         # re-establish symbolic link
         run('sudo ln -s /data/web_static/releases/web_static_{}/ /data/web_static/current'.format(timestamp))

     except Exception as e:
         print(e)
         return False
     # return True on success
     return True
