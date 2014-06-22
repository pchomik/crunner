# -*- coding: utf-8 -*-
"""
:author: Pawel Chomicki
"""
import time
import unittest

from mock import Mock, call
from crunner.event import FileEvent


class TestFileEvent(unittest.TestCase):
    def test__on_modified__executes_each_runner(self):
        runner = ['Test1', Mock(), '/test1']
        event = FileEvent(runner=runner)
        event.last_executed = time.time() - 5
        event.on_modified(Mock())
        runner[1].assert_has_calls(call.test('Test1', '/test1'))


if __name__ == '__main__':
    unittest.main()
