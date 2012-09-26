Tiny Server
===========

If you like Rails.. you'll love it!

The idea
--------

Tiny Server is a very little application server based on the python's WSGI libs that will allow you to write powerful and well formed web based applications.

It is based on the MVC and the "Convention over Configuration" patters: you have to write only the necessary.

Let's start
-----------

To start using Tiny Server, simply clone the code in a folder using the command

	git clone https://github.com/helloIAmPau/TinyServer.git

The best way to install python dependancies, is to build a virtual environment into the root folder of the project. You can use `virtualenv` command into the root folder

	virtual --distribute PythonEnv
	source PythonEnv/bin/activate 

Now you can install dependencies using pip

	pip install Jinja2

If you use foreman, you can run Tiny Server typing
	
	foreman start

otherwise you ca use a more classical 
	
	python router.py

The application structure
-------------------------

As mentioned above, Tiny Server is based on the Model-View-Controller pattern. In this section you'll learn how to create this three components in order to build your own applications.

### The Controller

To write a controller, simply you have to create a python class into the `app/controllers` folder that extends TinyController. For example, look at this `test.py` class:

	#!/usr/bin/env python
	# encoding: utf-8

	from tiny_server.TinyController import TinyController;

	class test(TinyController):
		def dosomething(self):
			pass;

To call the `dosomething()` method you have to redirect your browser to

	http://localhost:5000/test/dosomething

Thats all! Smart, don't you think so?

### The View

And here comes the best! To add a view, simply create an `html` page or an `xml - json` file into `app/views/` using the structure `class_name/method.(html|xml|json)`. At the end of the esecution of the controller, automatically the corresponding view where called and sent to the client. 

You can embed some python code using the `Jinja2` convention and read all the "class" variables of the controller:

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

Remember: for every action can be associate only one view, so if in the folder there are more than one view, will loaded only one view in accordance with the following priority list:

* action.html
* action.xml
* action.json

### The Model

Actually Tiny Server doesn't provide a smart method to add models, but you can use, for instance, [SqlAlchemy](http://www.sqlalchemy.org/). Look at `Development` section to know how you can give us some help.

Development
----------

Tiny Server want to be a social and an "always in beta" application.
Everyone can collaborates with Tiny Server project adding some code, proposing some ideas, testing the current version.. Every thing that comes in your head, every minute that you can spend, can be useful to make this project bigger. So we encurage you to fork this code ad give us a feedback. 
Right now there are some opened issues:

* Adding a smart method to manage models
* Refactoring of the current version
* Testing

If someone want to collaborate.. can contact personally us by mail: 
[Pasquale Boemio](mailto:boemianrapsodi@gmail.com) 
[Antonio Bevilacqua](mailto:b3by.in.th3.sky@gmail.com)

Thanks for your support!
