#!/usr/bin/python3
"""this distribute the archieve of the web static"""
from fabric.api import run, put, env, local
from os.path import exists
from datetime import datetime


env.hosts = ['52.23.213.229', '100.25.220.47']


def deploy():
    """
    Full deployment
    """

    archive = do_pack()
    if not archive:
        return False
    result = do_deploy(archive)
    return result


def do_pack():
    """
    packing webstatic files
    """

    try:
        dateT = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        file_dir = "versions/web_static_{}.tgz".format(dateT)
        local("tar -cvzf {} web_static".format(file_dir))
        return file_dir

    except Exception:
        return None


def do_deploy(archive_path):
    """
    deploys webstatic files
    """

    if not exists(archive_path):
        return False

    try:
        archive = archive_path.split("/")[-1]

        tmp_path = '/tmp/' + archive
        release_path = '/data/web_static/releases/{}/'.format(
            archive.partition('.')[0])

        put(archive_path, tmp_path)
        run('mkdir -p {}'.format(release_path))
        run('tar -xzf {} -C {}'.format(tmp_path, release_path))
        run('rm {}'.format(tmp_path))
        run('mv {}web_static/* {}'.format(release_path, release_path))
        run('rm -rf {}web_static/'.format(release_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(release_path))

        # Task carried out successfully
        print('New version deployed!')
        return True
    except Exception:
        return False
