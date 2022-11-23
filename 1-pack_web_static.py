#!/usr/bin/env python3
"""this is the creation of a tar file ie creation using fabric"""
from datetime import datetime
import os.path
from fabric.api import local


def do_pack():
    """to compress the webstatic"""
    dt = datetime.utcnow()
    year = dt.year
    month = dt.month
    day = dt.day
    hour = dt.hour
    minute = dt.minute
    second = dt.second
    file_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(year,
                                                              month,
                                                              day,
                                                              hour,
                                                              minute,
                                                              second)

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file_name)).failed is True:
        return None
    return file_name
