# -*- coding: utf-8 -*-
import os
import json


class ConfigLoader(object):
    def __init__(self, path='~/.crunner.json'):
        self.path = path.replace('~', os.path.expanduser('~'))

    def load(self):
        if not os.path.exists(self.path):
            return None, None, {}
        config_data = self._read_config_file()
        notifier, tester = self._parse_config_data(config_data)
        projects = config_data.get('projects', {})
        return notifier, tester, projects

    def _read_config_file(self):
        try:
            return json.loads(open(self.path, 'r').read())
        except ValueError as e:
            raise ValueError("Cannot read configuration.\nReturned error is:\n    {}".format(e.message))

    def _parse_config_data(self, config_data):
        notifier = config_data.get('notifier')
        tester = config_data.get('tester')
        if notifier is None or tester is None:
            raise SyntaxError("Wrong configuration.")
        return notifier, tester
