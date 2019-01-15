#!/usr/bin/python3
"""script to pack and deploy code"""
from fabric import decorators
from fabric.api import run, local, env, put, hosts
from datetime import datetime
from os import path

env.hosts = ["35.237.46.15", "34.73.216.247"]
# env.user = 'ubuntu'
# env.key_filename = "~/.ssh/macbook_id_rsa"


@decorators.runs_once
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
    if not path.isfile(archive_path):
        print('fils is bad')
        return False
    try:
        fonly = archive_path[archive_path.find("/"):]
        ffolder = fonly[:fonly.find(".")]
        dest_path = "/data/web_static/releases"
        result = put(archive_path, "/tmp" + fonly)
        result = run("rm -rf " + dest_path + ffolder + "/")
        result = run("mkdir -p " + dest_path + ffolder + "/")
        result = run("tar -xzf /tmp" + fonly + " -C " +
                     dest_path + ffolder + "/")
        result = run("rm /tmp" + fonly)
        result = run("mv " + dest_path + ffolder + "/web_static/* " +
                     dest_path + ffolder + "/")
        result = run("rm -rf " + dest_path + ffolder + "/web_static")
        result = run("rm -rf /data/web_static/current")
        result = run("ln -s " + dest_path + ffolder + "/ " +
                     "/data/web_static/current")
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """this function does end to end deployment of code"""
    archive = do_pack()
    if archive is None:
        return False
    result = do_deploy(archive)
    return(result)
