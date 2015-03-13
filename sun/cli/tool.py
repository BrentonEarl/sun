#!/usr/bin/python
# -*- coding: utf-8 -*-

# sun is a path of sun.

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

import sys
import time
import getpass
import commands
import subprocess
from sun.utils import fetch
from sun.__metadata__ import __version__


def su():
    """ display message when sun execute as root """
    if getpass.getuser() == "root":
        print("sun: Message: running as root ...")
        time.sleep(2)


def usage():
    """ sun arguments """
    args = [
        "Slackware Update Notifier - Version: {0}\n".format(__version__),
        "Usage: sun [OPTION]\n",
        "Optional  arguments:",
        "help      display this help and exit",
        "start     start sun daemon",
        "stop      stop sun daemon",
        "restart   restart sun daemon",
        "check     check for software updates",
        "status    sun daemon status"
    ]
    for opt in args:
        print opt


def check():
    """ check and display upgraded packages """
    upgraded, packages = fetch()[2:]
    if upgraded > 0:
        print("{0} software updates are available !".format(upgraded))
        for pkg in packages:
            print pkg
    else:
        print("No news is good news !")


def status():
    """ display sun daemon status """
    out = commands.getoutput("ps -A")
    if "sun_daemon" in out:
        print("sun is running ...")
    else:
        print("sun not running")


def init():
    """ Initialization , all begin from here """
    su()
    args = sys.argv
    args.pop(0)
    cmd = "/etc/rc.d/rc.sun"
    if len(args) == 1:
        if args[0] == "start":
            subprocess.call("{0} {1}".format(cmd, "start"), shell=True)
        elif args[0] == "stop":
            subprocess.call("{0} {1}".format(cmd, "stop"), shell=True)
        elif args[0] == "restart":
            subprocess.call("{0} {1}".format(cmd, "restart"), shell=True)
        elif args[0] == "check":
            check()
        elif args[0] == "status":
            status()
        elif args[0] == "help":
            usage()
        else:
            print("try: sun help")
    else:
        print("try: sun help")
