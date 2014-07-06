# -*- coding: utf-8 -*-
import unittest
from mock import patch, Mock
from crunner.config import ConfigLoader


CONFIG_DATA = {
    'notifier': {
        'cmd': '/tmp/notify-send',
        'img_arg': '-i',
        'msg_arg': '-m',
        'add_args': '--hint=int:transient:1'
    },
    'tester': {
        'cmd': '/tmp/py.test',
        'args': '-s'
    },
    'projects': {
        'A': {
            'active': True,
            'test_path': '/tmp',
            'watch_path': '/tmp'
        }
    }
}


class TestConfig(unittest.TestCase):
    def test_config_loader_allows_to_specify_config_path(self):
        ConfigLoader(path='/tmp/config')

    @patch('__builtin__.open', Mock())
    @patch('crunner.config.json.loads')
    @patch('crunner.config.os.path.exists', Mock(return_value=True))
    def test__load__returns_notify_and_pytest_path_and_projects(self, fake_loads):
        fake_loads.return_value = CONFIG_DATA
        notifier, pytest, projects = ConfigLoader().load()
        self.assertEqual(notifier['cmd'], '/tmp/notify-send')
        self.assertEqual(notifier['msg_arg'], '-m')
        self.assertEqual(notifier['img_arg'], '-i')
        self.assertEqual(notifier['add_args'], '--hint=int:transient:1')
        self.assertEqual(pytest['cmd'], '/tmp/py.test')
        self.assertEqual(pytest['args'], '-s')
        self.assertIn('A', projects)


if __name__ == '__main__':
    unittest.main()
