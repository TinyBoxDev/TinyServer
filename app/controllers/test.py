#!/usr/bin/env python
# encoding: utf-8
"""
test.py

Created by Pasquale Boemio on 2012-09-23.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import unittest;
from tiny_server.TinyController import TinyController;

class test(TinyController):
	
	def login(self):
		data = self.getDataBundle();
		print str(data);
		self.cacca = "ciao";


class testTests(unittest.TestCase):
	
	def setUp(self):
		self.dummy_data = { 'username': 'cacca', 'pass': 'piscio' };
	
	def test_login(self):
		# creating an instance of the controller
		t = test(self.dummy_data);
		# trying to call the method
		t.login();


if __name__ == '__main__':
	unittest.main()