#!/usr/bin/python
# -*- coding: utf-8 -*-

# main.py is a path of sun.

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


import time
import pynotify


from utils import (
    file_size,
    config,
    package_updates
)
from __metadata__ import (
    __all__,
    icon_path,
)


class Notify(object):

    def __init__(self):
        pynotify.uninit()
        pynotify.init("sun")
        self.summary = "{0}Software Updates".format(" " * 10)
        self.message = "{0} software updates are available !\n".format(
            package_updates())
        self.icon = "{0}{1}.png".format(icon_path, __all__)
        self.n = pynotify.Notification(self.summary, self.message, self.icon)
        self.n.set_timeout(60000 * int(config()['STANDBY']))

    def show(self):
        server, local = file_size()
        if server != local:
            self.n.close()    # close daemon
            self.n.update(self.summary, self.message, self.icon)
            self.n.show()     # run daemon


def main():

    while True:
        Notify().show()
        time.sleep(60 * int(config()['INTERVAL']))

if __name__ == "__main__":
    main()
