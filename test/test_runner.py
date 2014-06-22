# -*- coding: utf-8 -*-
"""
:author: Pawel Chomicki
"""
import os
import unittest

from mock import patch, call, Mock
from crunner.runner import Runner


def fake_pkg_resource(*args, **kwargs):
    if '{}ok.png'.format(os.sep) in args[1]:
        return '/tmp/ok.png'
    elif '{}nok.png'.format(os.sep) in args[1]:
        return '/tmp/nok.png'


class TestRunner(unittest.TestCase):
    def setUp(self):
        with patch('pkg_resources.resource_filename', Mock(side_effect=fake_pkg_resource)):
            self.runner = Runner(pytest_path='/usr/bin/py.test', notify_path="/usr/local/bin/notify-send")

    @patch('crunner.runner.Popen')
    def test__test__requires_path(self, fake_popen):
        self.runner.test(name="Project", path='/tmp')
        fake_popen.assert_has_calls(call('cd /tmp; /usr/bin/py.test /tmp', shell=True))

    @patch('crunner.runner.Popen')
    def test__test__returns_exit_code(self, fake_popen):
        fake_popen.return_value.poll.return_value = 0
        result = self.runner.test(name="Project", path='/tmp')
        self.assertEqual(result, 0)

    def test__test__executes_notify_with_ok_result_for_positive_code(self):
        with patch('crunner.runner.Popen') as fake:
            fake.return_value.poll.return_value = 0
            self.runner.test(name="Project", path='/tmp')
            fake.assert_has_calls(call('/usr/local/bin/notify-send -i "/tmp/ok.png" --hint=int:transient:1 Project', shell=True))


if __name__ == '__main__':
    unittest.main()
