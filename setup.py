#!/usr/bin/env python
from setuptools import setup

setup(
        name='Tigger',
        version='0.1.0',
        packages=['tigger',],
        license='MIT',
        description="Command-line tagging tool.",
        long_description="Tigger is a command-line tagging tool written in " +
            "python, intended for tracking tags on files in a form which can " +
            "be transferred with the files while remaining out of sight " +
            "normally (much like git's metadata, except not so clever).",
        entry_points={
            "console_scripts": [
                "tigger = tigger.app:main",
                ],
            },
        )
