# -*- coding: utf-8 -*-
# TODO: Handle the py.test execution better (clean screen)
# TODO: Move command builder to separate method/class

import os
import pkg_resources

from subprocess import Popen
from .logger import log


class Runner(object):

    NOTIFIER_BASE_CMD = '{cmd} {img_arg} "{img}" {add_args} {msg_arg} {msg}'

    def __init__(self, tester_args, notifier_args):
        self._dispatch_args(tester_args, notifier_args)
        self._ok_img = pkg_resources.resource_filename(__name__, 'images/ok.png')
        self._nok_img = pkg_resources.resource_filename(__name__, 'images/nok.png')

    def test(self, name, path):
        log.info(
            "\n\n\n" +
            "".ljust(40, '-').rjust(80, '-') +
            "\n{}\n".format('PYTEST EXECUTION'.ljust(40).rjust(80)) +
            "".ljust(40, '-').rjust(80, '-') +
            "\n\n\n"
        )
        os.chdir('/tmp')
        cmd = "cd /tmp; {} {} {}".format(self._tester_cmd, self._tester_args, path)
        proc = Popen(cmd, shell=True)
        result = None
        while True:
            result = proc.poll()
            if result is not None:
                break

        if result == 0:
            cmd = self.NOTIFIER_BASE_CMD.format(cmd=self._notifier_cmd,
                                                img_arg=self._notifier_img_arg,
                                                img=self._ok_img,
                                                add_args=self._notifier_add_args,
                                                msg_arg=self._notifier_msg_arg,
                                                msg=name)
        else:
            cmd = self.NOTIFIER_BASE_CMD.format(cmd=self._notifier_cmd,
                                                img_arg=self._notifier_img_arg,
                                                img=self._nok_img,
                                                add_args=self._notifier_add_args,
                                                msg_arg=self._notifier_msg_arg,
                                                msg=name)
        Popen(cmd, shell=True)
        return result

    def _dispatch_args(self, tester_args, notifier_args):
        self._tester_cmd = tester_args.get('cmd')
        self._tester_args = tester_args.get('args')
        self._notifier_cmd = notifier_args.get('cmd')
        self._notifier_img_arg = notifier_args.get('img_arg')
        if self._notifier_img_arg == '':
            self._disable_images()
        self._notifier_msg_arg = notifier_args.get('msg_arg')
        self._notifier_add_args = notifier_args.get('add_args')

    def _disable_images(self):
        self._nok_img = ''
        self._ok_img = ''


