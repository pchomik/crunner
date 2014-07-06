# -*- coding: utf-8 -*-
import os
import unittest
from mock import patch, call, Mock
from crunner import runner


NOTIFIER = {
    'cmd': '/tmp/notify-send',
    'img_arg': '-i',
    'msg_arg': '-m',
    'add_args': '--hint=int:transient:1'
}

TESTER = {
    'cmd': '/tmp/py.test',
    'args': '-s'
}


def fake_pkg_resource(*args, **kwargs):
    if '{}ok.png'.format(os.sep) in args[1]:
        return '/tmp/ok.png'
    elif '{}nok.png'.format(os.sep) in args[1]:
        return '/tmp/nok.png'


class TestRunner(unittest.TestCase):
    def setUp(self):
        self._old_log = self._mock_log()
        with patch('pkg_resources.resource_filename', Mock(side_effect=fake_pkg_resource)):
            self.runner = runner.Runner(tester_args=TESTER, notifier_args=NOTIFIER)

    def tearDown(self):
        runner.log = self._old_log

    def _mock_log(self):
        old_log = runner.log
        runner.log = Mock()
        return old_log

    @patch('crunner.runner.Popen')
    def test__test__requires_path(self, fake_popen):
        self.runner.test(name="Project", path='/tmp')
        fake_popen.assert_has_calls(call('cd /tmp; /tmp/py.test -s /tmp', shell=True))

    @patch('crunner.runner.Popen')
    def test__test__returns_exit_code(self, fake_popen):
        fake_popen.return_value.poll.return_value = 0
        result = self.runner.test(name="Project", path='/tmp')
        self.assertEqual(result, 0)

    def test__test__executes_notify_with_ok_result_for_positive_code(self):
        with patch('crunner.runner.Popen') as fake:
            fake.return_value.poll.return_value = 0
            self.runner.test(name="Project", path='/tmp')
            fake.assert_has_calls(call('/tmp/notify-send -i "/tmp/ok.png" --hint=int:transient:1 -m Project', shell=True))


if __name__ == '__main__':
    unittest.main()
