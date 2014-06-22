#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:author: Pawel Chomicki
"""
import time

from crunner.config import ConfigLoader
from crunner.runner import Runner
from crunner.event import FileEvent
from crunner.watcher import FileWatcher


notify_path, pytest_path, projects = ConfigLoader().load()
runner = Runner(pytest_path, notify_path)
watchers = []
for name, settings in projects.items():
    if settings['active']:
        event = FileEvent([name, runner, settings['test_path']], ignore_regexes=['.*/\..*', '.*\.pyc'])
        watcher = FileWatcher(settings['watch_path'], event)
        watcher.start()
        watchers.append(watcher)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    for each in watchers:
        each.stop()
