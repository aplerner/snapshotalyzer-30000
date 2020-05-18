#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 11:28:54 2020

@author: aaronlerner
"""

from setuptools import setup

setup(
    name='snapshotalyzer-30000',
    version='0.1',
    author="Aaron Lerner",
    author_email="aplerner@mac.com",
    description="Snapshotalyzer-30000 is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/aplerner/snapshotalyzer-30000",
    install_requires=[
            'click',
            'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
      )