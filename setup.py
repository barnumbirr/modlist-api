#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = 'modlist',
    version = '0.1',
    url = 'https://github.com/c0ding/modlist-api',
    download_url = 'https://github.com/c0ding/modlist-api/archive/master.zip',
    author = 'c0ding',
    author_email = 'me@martinsimon.me',
    license = 'Apache v2.0 License',
    packages = ['modlist'],
    description = 'Python API wrapper for Minecraft mods posted to MCF Modlist.',
    long_description = file('README.md','r').read(),
    keywords = ['minecraft', 'MCF Modlist', 'API', 'Craftbukkit', 'Feed The Beast', 'MCPC+', 'Cauldron'],
)
