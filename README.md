Tiny Server
===========

If you like Rails.. you'll love it!

The idea
--------

Tiny Server is a very little application server based on the python's WSGI libs that will allow you to write powerful and well formed web based applications.

It is based on the MVC and the "Convention over Configuration" patters: you have to write only the necessary.

The application structure
-------------------------

As mentioned above, Tiny Server is based on the Model-View-Controller pattern. In this section you'll learn how to create this three components to build your own applications.

### The Controller

To write a controller, simply you hate to create a python class into the `app/controllers` folder that extends TinyController. For example, look at this `test.py` class:

	#!/usr/bin/env python
	# encoding: utf-8

	from tiny_server.TinyController import TinyController;

	class test(TinyController):
		def dosomething(self):
			pass;

To call the `dosomething()` method you have to redirect your browser to

	http://localhost:5000/test/dosomething

Thats all! Smart, not you think?

### The View

And here comes the best! The add a view, simply create an `html` page or an `xml - json` file into `app/views/` using the conventional structure `class_name/method.(html|xml|json)`. At the end of the esecution of the controller, automatically the corresponding view where called and sent to the client. 

You can embed some python code using the `Jinja2` convention. Every class variable of the controller meybe evaluated into the view body:

	<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
	<html lang="en">
	<head>
		<title>login</title>
	</head>
	<body>
		Ciao<br>
		Controller var: {{ var_name }}
	</body>
	</html>

Remember: for every action you can associate only one view. If in the folder there is more than one view, were applicated this priority convention:

* action.html
* action.xml
* action.json

### The Model

Actually Tiny Server doesn't provide a smart method to add model. You can use, for instance, [SqlAlchemy](http://www.sqlalchemy.org/) to add data support. Look at `Developing` section to know how to give some help.
