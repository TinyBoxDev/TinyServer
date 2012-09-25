#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-
"""
router.py

Created by Pasquale Boemio on 2012-09-09.
Copyright (c) 2012. All rights reserved.
"""

import imp;
import os;
import sys;
from wsgiref.simple_server import make_server;
from tiny_server import Constants, logMessage, BadRequestException;
from mimetypes import guess_type;
from cgi import FieldStorage as read_request_vars;
from jinja2 import Environment, FileSystemLoader, TemplateNotFound;

def _route(environ, start_response):
	try:
		logMessage('Received a request');
		calledItem = environ[Constants.HTTP_REQUEST_ADDRESS].split('/')[1:];
		logMessage('parsed address:', str(calledItem));
		# Static request
		if calledItem[Constants.REQUESTED_FUNCTION] == Constants.GET_STATIC_ITEM:
			status, headers, view = _provideAResource(Constants.STUFFS_FOLDER + calledItem[Constants.REQUESTED_ITEM_TYPE] + "/" + calledItem[Constants.REQUESTED_ITEM]);
		# Active request
		elif len(calledItem)==2 and calledItem[Constants.REQUESTED_FUNCTION]!='' and calledItem[Constants.REQUESTED_ACTION]!='': 
			logMessage('Recognized an active request');
			status, headers, view = _executeAction(calledItem[Constants.REQUESTED_FUNCTION], calledItem[Constants.REQUESTED_ACTION], environ);
		# Requesting home page
		elif calledItem[Constants.REQUESTED_FUNCTION] == '':
			logMessage('Let\'s go to the homepage!' );
			status, headers, view = _provideAResource(Constants.STUFFS_FOLDER + Constants.HOME_PAGE);
		# Requesting favicon
		elif calledItem[Constants.REQUESTED_FUNCTION] == 'favicon.ico':
			logMessage('Providing favicon');
			status, headers, view = _provideAResource(Constants.STUFFS_FOLDER + 'images/favicon.ico');
		else:
			raise(BadRequestException('invalid arguments'));
	except BadRequestException as e:
		logMessage('ERROR: ' + str(e));
		status, headers, view = _provideAResource(Constants.STUFFS_FOLDER + Constants.ERROR_PAGE);
		status = Constants.STATUS_BAD_REQUEST;
		
	start_response(status, headers);
	return [view];

def _provideAResource(itemLocation):
	try:
		objectLoaded = open(itemLocation).read();
		status = Constants.STATUS_OK;
	except IOError as e:
		logMessage('ERROR: ' + str(e));
		status = Constants.STATUS_NOT_FOUND;
		objectLoaded = open(Constants.STUFFS_FOLDER + Constants.ERROR_PAGE).read();
		
	headers = [('Content-type', guess_type(itemLocation)[0])];
	
	return status, headers, objectLoaded;

def _executeAction(controllerName, action, session):
	method = session[Constants.HTTP_METHOD];
	
	
	if method == Constants.HTTP_METHOD_GET:
		params = read_request_vars(fp=session[Constants.GET_REQUEST_CONTENT], environ=session, keep_blank_values=True);
	elif method == Constants.HTTP_METHOD_POST:
		params = read_request_vars(fp=session[Constants.POST_REQUEST_CONTENT], environ=session, keep_blank_values=True);
	else:
		raise BadRequestException('Wrong method provided!');
	
	try:
		controllerModule = imp.load_source(controllerName, Constants.CONTROLLERS_FOLDER + controllerName + ".py");
		controller = getattr(controllerModule, controllerName)(params);
		getattr(controller, action)();
	
		loader = FileSystemLoader(Constants.VIEWS_FOLDER + "/" + controllerName);
		env = Environment(loader=loader);
		template = env.select_template([action + '.html', action + '.xml', action + '.json']);
		page = template.render(controller.__dict__);
		headers = [('Content-type', guess_type(template.name)[0])];
	
	except TemplateNotFound:
		raise BadRequestException('Unable to find a view');
	except IOError:
		raise BadRequestException('Unable to find the controller');
		
	return Constants.STATUS_OK, headers, page.encode('utf-8');		

if __name__ == "__main__":
	Constants.setFolders(os.path.realpath(os.path.dirname(__file__)));
	port = int(os.environ.get('PORT', 5000));
	httpd = make_server('0.0.0.0', port, _route);
	print "TinyServer is serving on port " + str(port) + "...";
	httpd.serve_forever();
