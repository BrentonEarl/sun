#!/usr/bin/python
# -*- coding: utf-8 -*-

# utils.py is a part of sun.

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
import re
import urllib2
from __metadata__ import (
    arch,
    pkg_path,
    conf_path,
    etc_slackpkg,
    changelog_txt,
    var_lib_slackpkg
)


def urlopen(link):
    """ Return urllib2 urlopen """
    try:
        return urllib2.urlopen(link)
    except urllib2.URLError:
        pass


def read_file(registry):
    """ Return reading file """
    with open(registry, "r") as file_txt:
        read_file = file_txt.read()
        file_txt.close()
        return read_file


def slack_ver():
    """ Open file and read Slackware version """
    sv = read_file("/etc/slackware-version")
    return sv.split()[0], (".".join(re.findall(r"\d+", sv)))


def ins_packages():
    """ Count installed Slackware packages """
    count = 0
    for pkg in os.listdir(pkg_path):
        if not pkg.startswith("."):
            count += 1
    return count


def read_config(config):
    """ Read config file and return uncomment line """
    for line in config.splitlines():
        line = line.lstrip()
        if line and not line.startswith('#'):
            return line


def mirror():
    """ Grab Slackware ChangeLog.txt mirror """
    slackpkg_mirror = read_config(read_file("{0}{1}".format(etc_slackpkg,
                                                            "mirrors")))
    slackware_mirror = read_config(read_file("{0}{1}".format(conf_path,
                                                             "mirrors")))
    if slackpkg_mirror and "current" in slackpkg_mirror:
        return "{0}slackware{1}-current/{2}".format(slackware_mirror, arch,
                                                    changelog_txt)
    else:
        return "{0}slackware{1}-{2}/{3}".format(slackware_mirror, arch,
                                                slack_ver()[1], changelog_txt)


def fetch():
    """ Get ChangeLog.txt file size and count upgraded packages"""
    tar = urlopen(mirror())
    r = tar.read()
    count = 0
    slackpkg_last_date = read_file("{0}{1}".format(
        var_lib_slackpkg, changelog_txt)).split("\n", 1)[0].strip()
    packages = []
    for line in r.splitlines():
        if slackpkg_last_date == line.strip():
            break
        if line.endswith("Upgraded.") or line.endswith("Rebuilt."):
            packages.append(line.split("/")[-1])
            count += 1
    return [count, packages]


def config():
    """ Reaturn sun configuration values """
    conf_args = {
        "INTERVAL": 60,
        "STANDBY": 3
    }
    config_file = read_file("{0}{1}".format(conf_path, "sun.conf"))
    for line in config_file.splitlines():
        line = line.lstrip()
        if line and not line.startswith('#'):
            conf_args[line.split('=')[0]] = line.split('=')[1]
    return conf_args


def os_info():
    """ Get OS info """
    slack, ver = slack_ver()
    stype = "Stable"
    if "current" in mirror():
        stype = "Current"
    info = ("OS: {0}\n"
            "Version: {1}\n"
            "Type: {2}\n"
            "Arch: {3}\n"
            "Kernel: {4}\n"
            "Packages: {5}".format(slack, ver, stype, os.uname()[4],
                                   os.uname()[2], ins_packages()))
    return info
