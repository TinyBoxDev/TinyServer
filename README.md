Tiny Server
===========

If you like Rails.. you'll love it!

The idea
--------

Tiny Server is a very little application server based on the python's WSGI libs that will allow you to write powerful and well formed web based applications.

It is based on the MVC and the "Convention over Configuration" patters: you have to write only the necessary.

### The controller

To write a controller, simply you have to create a python class into the `app/controllers` folder that extends TinyController. For example, look at this `test.py` class:

	#!/usr/bin/env python
	# encoding: utf-8

	from tiny_server.TinyController import TinyController;

	class test(TinyController):
		def dosomething(self):
			pass;

To call the `dosomething()` method you have to redirect your browser to

	http://localhost:5000/test/dosomething

Thats all! Smart, not you think?
