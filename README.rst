.. image:: https://img.shields.io/github/release/dslackw/sun.svg
    :target: https://github.com/dslackw/sun/releases
.. image:: https://travis-ci.org/dslackw/sun.svg?branch=master
    :target: https://travis-ci.org/dslackw/sun
.. image:: https://landscape.io/github/dslackw/sun/master/landscape.png
    :target: https://landscape.io/github/dslackw/sun/master
.. image:: https://img.shields.io/codacy/6464ba0bd1e342e28388c71a34b3a5e8.svg
    :target: https://www.codacy.com/public/dzlatanidis/slpkg/dashboard
.. image:: https://img.shields.io/pypi/dm/sun.svg
    :target: https://pypi.python.org/pypi/sun
.. image:: https://img.shields.io/badge/license-GPLv3-blue.svg
    :target: https://github.com/dslackw/sun
.. image:: https://img.shields.io/github/stars/dslackw/sun.svg
    :target: https://github.com/dslackw/sun
.. image:: https://img.shields.io/github/forks/dslackw/sun.svg
    :target: https://github.com/dslackw/sun
.. image:: https://img.shields.io/github/issues/dslackw/sun.svg
    :target: https://github.com/dslackw/sun/issues

.. contents:: Table of Contents:

About
-----

Slackware Update Notifier is a tray notification applet for informing about
package updates in Slackware and CLI tool for monitoring upgraded packages.

.. image:: https://raw.githubusercontent.com/dslackw/sun/master/icon/sun.png
    :target: https://github.com/dslackw/sun

How works
---------
In fact comparing the two ChangeLog.txt files to a server and a local by countng how 
many packages have rebuilt or upgraded.

 
Installing
----------

.. code-block:: bash

    Use SlackBuild script or:

    $ pip install sun --upgrade

Usage
-----

.. code-block:: bash

    Add sun in your windows manager session startup.
    
    As for xfce:
    Settings Manager --> Session and Startup --> Application Autostart --> +Add
    
    Name: sun
    Description: Slackware Update Notifier
    Command: /usr/bin/sun start
    [Ok]


CLI
---

.. code-block:: bash

    $ sun help
    Slackware Update Notifier - Version: 1.0.1

    Usage: sun [OPTION]

    Optional  arguments:
    help      display this help and exit
    start     start sun daemon
    stop      stop sun daemon
    restart   restart sun daemon
    check     check for software updates
    status    sun daemon status

    $ sun start
    Starting sun daemon:  /usr/bin/sun_daemon

    $ sun stop
    Stoping sun daemon:  /usr/bin/sun_daemon

    $ sun status
    sun is not running
    
    $ sun check
    3 software updates are available !
    samba-4.1.17-x86_64-1_slack14.1.txz:  Upgraded.
    mozilla-firefox-31.5.0esr-x86_64-1_slack14.1.txz:  Upgraded.
    mozilla-thunderbird-31.5.0-x86_64-1_slack14.1.txz:  Upgraded.


Configuration files
-------------------

.. code-block:: bash

    /etc/sun/sun.conf
        General configuration of sun

    /etc/sun/mirrors
        List of Slackware ChangeLog.txt Mirrors

    /etc/rc.d/rc.sun
        Runtime configuration file

    
Screenshot
---------

.. image:: https://raw.githubusercontent.com/dslackw/images/master/sun/sun_screenshot.png
    :target: https://github.com/dslackw/sun

Donate
------
If you feel satisfied with this project and want to thank me go
to `Slackware <https://store.slackware.com/cgi-bin/store/slackdonation>`_ and make a donation or visit the `store <https://store.slackware.com/cgi-bin/store>`_.


Copyright 
---------

- Copyright © Dimitris Zlatanidis
- Slackware® is a Registered Trademark of Slackware Linux, Inc.
- Linux is a Registered Trademark of Linus Torvalds.
