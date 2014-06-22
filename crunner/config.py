# -*- coding: utf-8 -*-
"""
:author: Pawel Chomicki
"""
import os
import json


class ConfigLoader(object):
    def __init__(self, path='~/.crunner.json'):
        self.path = path.replace('~', os.path.expanduser('~'))

    def load(self):
        if not os.path.exists(self.path):
            return None, None, {}
        config = json.loads(open(self.path, 'r').read())
        notify_path = config.get('notify_path', None)
        pytest_path = config.get('pytest_path', None)
        projects = config.get('projects', {})
        return notify_path, pytest_path, projects
