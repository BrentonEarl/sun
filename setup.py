#!/usr/bin/python
# -*- coding: utf-8 -*-

# setup.py file is part of sun.

# Copyright 2015 Dimitris Zlatanidis <d.zlatanidis@gmail.com>
# All rights reserved.

# sun is a tray notification applet for informing about
# package updates in Slackware.

# https://github.com/dslackw/sun

# sun is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import shutil

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from sun.__metadata__ import (
    __all__,
    __version__,
    __email__,
    __author__,
    conf_path,
    icon_path,
    bin_path,
    rc_path
)

setup(
    name=__all__,
    packages=["sun"],
    scripts=["bin/sun_daemon", "bin/sun", "bin/sun_gtk"],
    version=__version__,
    description="Tray notification applet for informing about package updates "
                "in Slackware",
    keywords=["tray", "notify", "slackware", "desktop"],
    author=__author__,
    author_email=__email__,
    url="https://github.com/dslackw/sun",
    package_data={"": ["LICENSE", "README.rst", "ChangeLog.txt"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Classifier: Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 or later "
        "(GPLv3+)",
        "Classifier: Operating System :: Unix",
        "Classifier: Programming Language :: Python",
        "Classifier: Programming Language :: Python :: 2.5",
        "Classifier: Programming Language :: Python :: 2.6",
        "Classifier: Programming Language :: Python :: 2.7",
        ],
    long_description=open("README.rst").read()
)

if "install" in sys.argv:
    dirs = [bin_path, conf_path, icon_path, rc_path]
    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)

    print("Install sun.conf --> {0}".format(conf_path))
    shutil.copy2("conf/{0}.conf".format(__all__), conf_path)
    print("Install mirrors --> {0}".format(conf_path))
    shutil.copy2("conf/mirrors", conf_path)
    print("Install rc.sun --> {0}".format(rc_path))
    shutil.copy2("conf/rc.{0}".format(__all__), rc_path)
    os.chmod(rc_path + "rc.sun", 0755)
    print("Install sun.png --> {0}".format(icon_path))
    shutil.copy2("icon/{0}.png".format(__all__), icon_path)
