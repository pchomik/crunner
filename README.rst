crunner
=======
crunner is small application to run test continuously and notify about every change

Main features:
* continuously watch directories
* execute proper tests after every change
* send graphics notification about test result

requirements
============

* Python 2.7.x (not tested with Python 3.x)
* notify-send  (linux application)
* py.test      (test framework)
* watchdog     (python package)
* mock         (for testing)

Continues Integration
=====================
.. image:: https://drone.io/github.com/pchomik/crunner/status.png
     :target: https://drone.io/github.com/pchomik/crunner/latest

Download
========
Latest version of plugin is available in `drone.io project artifacts <https://drone.io/github.com/pchomik/crunner/files>`_.

Install
=======
TBD

Contribution
============
Please feel free to present your idea by code example (pull request) or reported issues.

Future plans
============
* Handle test execution without py.test
* Support for nose and other unittest frameworks
* Provide working directory settings
* Provide custom arguments settings

License
=======
crunner - Application to run test continuously and notify about every change

Copyright (C) 2014 Pawel Chomicki

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.


