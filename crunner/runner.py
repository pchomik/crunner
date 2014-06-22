# -*- coding: utf-8 -*-
"""
:author: Pawel Chomicki
"""

# TODO: Handle the py.test execution better (clean screen)
# TODO: Move command builder to separate method/class

import os
import pkg_resources

from subprocess import Popen, PIPE


class Runner(object):
    def __init__(self, pytest_path, notify_path):
        self.pytest_path = pytest_path
        self.notify_path = notify_path
        self.ok = pkg_resources.resource_filename(__name__, 'images/ok.png')
        self.nok = pkg_resources.resource_filename(__name__, 'images/nok.png')

    def test(self, name, path):
        print("\n\n\n")
        print("".ljust(40, '-').rjust(80, '-'))
        print("\n{}\n".format('PYTEST EXECUTION'.ljust(40).rjust(80)))
        print("".ljust(40, '-').rjust(80, '-'))
        print("\n\n\n")
        os.chdir('/tmp')
        cmd = "cd /tmp; {} {}".format(self.pytest_path, path)
        proc = Popen(cmd, shell=True)
        result = None
        while True:
            result = proc.poll()
            if result is not None:
                break

        if result == 0:
            cmd = '{} -i "{}" --hint=int:transient:1 {}'.format(self.notify_path, self.ok, name)
        else:
            cmd = '{} -i "{}" --hint=int:transient:1 {}'.format(self.notify_path, self.nok, name)
        Popen(cmd, shell=True)
        return result


