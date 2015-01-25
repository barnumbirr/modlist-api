#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib2
from modlist_utils import entrypoint

__title__ = 'modlist'
__version__ = '0.1'
__author__ = '@c0ding'
__repo__ = 'https://github.com/c0ding/modlist-api'
__license__ = 'Apache v2.0 License'


def about():
	"""Returns some information about the modlist module."""

	return '{} v.{} is maintained by {} and available at {}.'.format(__title__, __version__, __author__, __repo__)


def mods(VERSION):
	"""
	Returns a list of mods on the selected [VERSION].
	[ALL] is an acceptable request for [VERSION].
	"""

	d = urllib2.urlopen(entrypoint(str(VERSION)) + '.json')
	e = json.loads(d.read())
	return e


def md5hash(VERSION):
	"""
	Returns the md5 hash of the selected [VERSION].
	[ALL] is an acceptable request for [VERSION].
	Hash request is returned in plain text, not JSON.
	This is an md5 hash of the requested json file.
	"""

	d = urllib2.urlopen(entrypoint(str(VERSION)) + '.md5')
	return d.read()


def recent():
	"""
	Returns a dict of recent changes.
	It is the most recent partial piece of the
	changelog of all supported versions.
	"""

	d = urllib2.urlopen(entrypoint('recent.json'))
	e = json.loads(d.read())
	return e
