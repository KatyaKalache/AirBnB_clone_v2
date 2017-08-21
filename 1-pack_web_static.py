#!/usr/bin/python3
"""
Compress Directory with Fabric3 from python
"""
from fabric import operations
from datetime import datetime


def do_pack():
    """creates a .tgz file using the tar command in the local server with
    fabric python library.  Returns relative path or None on error"""
    time_now = str(datetime.utcnow())
    time_now = time_now.split('.')[0]
    errors = ''
    for c in [' ', ':', '-']:
        time_now = time_now.replace(c, '')
    file_name = "versions/web_static_{}.tgz".format(time_now)
    errors += operations.local("mkdir -p ./versions")
    errors += operations.local("tar -czvf {} ./web_static".format(file_name))
    return file_name if errors == '' else None

if __name__ == "__main__":
    do_pack()
