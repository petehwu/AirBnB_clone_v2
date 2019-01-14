#!/usr/bin/python3
from fabric.api import run, local
from datetime import datetime


def do_pack():
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
