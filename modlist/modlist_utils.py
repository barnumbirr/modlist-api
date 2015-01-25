#!/usr/bin/env python
# -*- coding: utf-8 -*-

__title__ = 'modlist'
__version__ = '0.1'
__author__ = '@c0ding'
__repo__ = 'https://github.com/c0ding/modlist-api'
__license__ = 'Apache v2.0 License'

MODLIST_ENTRYPOINT = 'http://modlist.mcf.li/api/v3/'

def entrypoint(*suffix):
	"""
	Returns the entrypoint URL for the MCF Modlist.
	All data provided by modlist.mcf.li.
	http://modlist.mcf.li/
	"""

	return MODLIST_ENTRYPOINT + '/'.join(suffix)
