#!/usr/bin/python3
"""script to pack and deploy code"""
from fabric.api import run, local, env, put, sudo
from datetime import datetime
from os import path

# env.user = 'ubuntu'
# env.key_filename = "~/.ssh/macbook_id_rsa"


def do_pack():
    """ This function packs files to get ready to deploy"""
    dt = datetime.now()
    tgt = "versions/web_static_" + str(dt.year) + '{:02d}'.format(dt.month) +\
          '{:02d}'.format(dt.day) + '{:02d}'.format(dt.hour) +\
          '{:02d}'.format(dt.minute) + '{:02d}'.format(dt.second) + ".tgz"
    src = "web_static"
    local("mkdir -p versions")
    res = local("tar -cvzf {} {}".format(tgt, src), capture=True)
    if res.failed:
        return None
    else:
        return tgt


def do_deploy(archive_path):
    """This function deploys packed code to the servers"""
    env.hosts = [ "35.237.46.15", "34.73.216.247"]
    if not isfile(archive_path):
        return False
    try:
        fonly = archive_path[archive_path.find("/"):]
        ffolder = fonly[:fonly.find(".")]
        dest_path = "/data/web_static/releases"
        result = put(archive_path, "/tmp" + fonly)
        result = sudo("rm -rf " + dest_path + ffolder + "/")
        result = sudo("mkdir -p " + dest_path + ffolder + "/")
        result = sudo("tar -xzf /tmp" + fonly + " -C " +
                     dest_path + ffolder + "/")
        result = sudo("rm /tmp" + fonly)
        result = sudo("mv " + dest_path + ffolder + "/web_static/* " +
                     dest_path + ffolder + "/")
        result = sudo("rm -rf " + dest_path + ffolder + "/web_static")
        result = sudo("rm -rf /data/web_static/current")
        result = sudo("ln -s " + dest_path + ffolder + "/ " +
                     "/data/web_static/current")
        print("New version deployed!")
        return True
    except:
        return False
    return True
