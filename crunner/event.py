# -*- coding: utf-8 -*-
import time

from watchdog.events import RegexMatchingEventHandler


class FileEvent(RegexMatchingEventHandler):
    def __init__(self, runner, *args, **kwargs):
        super(FileEvent, self).__init__(*args, **kwargs)
        self.name, self.runner, self.path = runner
        self.last_executed = time.time()

    def on_modified(self, event):
        if time.time() - self.last_executed > 5:
            self.last_executed = time.time()
            self.runner.test(self.name, self.path)
