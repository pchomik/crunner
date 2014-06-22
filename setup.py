# -*- coding: utf-8 -*-
"""
:author: Pawel Chomicki
"""
from setuptools import setup, find_packages


requires = [
    'mock==1.0.1',
    'watchdog==0.7.1',
    'pytest==2.5.2'
]


setup(
    name="crunner",
    packages=['crunner'],
    version="0.0.1",
    description="Continues test runner.",
    author="Pawel Chomicki",
    author_email="pawel.chomicki@gmail.com",
    install_requires=requires,
    url="https://github.com/pchomik/pytest-c-runner",
    scripts=['script/crun.py']
)
