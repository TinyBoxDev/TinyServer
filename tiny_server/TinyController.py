#!/usr/bin/env python
# encoding: utf-8
"""
TinyController.py

Created by Pasquale Boemio on 2012-09-09.
Copyright (c) 2012. All rights reserved.
"""

import unittest


class TinyController(object):
	
	_paramsBundle = {};
	
	def __init__(self, vars):
		self._paramsBundle = vars;
	
	def getDataBundle(self):
		return self._paramsBundle;
	
	