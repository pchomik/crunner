# -*- coding: utf-8 -*-
"""
:author: Pawel Chomicki
"""
import unittest

from mock import patch, call, Mock
from crunner.config import ConfigLoader


CONFIG_DATA = {
    'notify_path': '/tmp/notify-send',
    'pytest_path': '/tmp/py.test',
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
        notify, pytest, projects = ConfigLoader().load()
        self.assertEqual(notify, '/tmp/notify-send')
        self.assertEqual(pytest, '/tmp/py.test')
        self.assertIn('A', projects)


if __name__ == '__main__':
    unittest.main()
