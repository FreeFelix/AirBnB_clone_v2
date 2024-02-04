#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes an archive
to my web servers, using the function do_deploy. 
Prototype: def do_deploy(archive_path):
Returns False if the file at the path archive_path doesn’t exist
"""

from fabric.api import put, run, env
from os.path import exists
"""
All remote commands must be executed on my both web servers
(using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)

"""
env.hosts = ['54.227.199.4', '100.25.203.163']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False
