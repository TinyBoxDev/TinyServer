#!/usr/bin/env python
# encoding: utf-8
"""
TinyController.py

Created by Pasquale Boemio on 2012-09-09.
Copyright (c) 2012. All rights reserved.
"""

import unittest


class TinyController:
	
	data_bundle;
	
	def __init__(self, vars):
		self.data_bundle = vars;


class TinyControllerTests(unittest.TestCase):
	def setUp(self):
		pass


if __name__ == '__main__':
	unittest.main()