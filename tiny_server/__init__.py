#!/usr/bin/env python
# encoding: utf-8
"""
__init__.py

Created by Pasquale Boemio on 2012-09-09.
Copyright (c) 2012. All rights reserved.
"""

class BadRequestException(Exception):
	
	def __init__(self, message):
		Exception.__init__(self, message);
		self._value = message;
		
	def __str__(self):
		return self._value;

class Constants(object):
	# Request constants
	HTTP_METHOD = 'REQUEST_METHOD';
	HTTP_METHOD_GET = 'GET';
	HTTP_METHOD_POST = 'POST';
	HTTP_REQUEST_ADDRESS = 'PATH_INFO';
	GET_REQUEST_CONTENT = 'QUERY_STRING';
	POST_REQUEST_CONTENT = 'wsgi.input';
	REQUESTED_FUNCTION = 0;
	REQUESTED_ACTION = 1;
	REQUESTED_ITEM_TYPE = 1;
	REQUESTED_ITEM = 2;
	GET_STATIC_ITEM = 'stuffs';
	# Http status constants
	STATUS_OK = '200 OK';
	STATUS_BAD_REQUEST = '400 Bad Request';
	STATUS_NOT_FOUND = '404 Not Found';
	# Folders
	ROOT_FOLDER = None;
	STUFFS_FOLDER = None;
	CONTROLLERS_FOLDER = None;
	MODELS_FOLDER = None;
	VIEWS_FOLDER = None;
	# Default Items
	ERROR_PAGE = 'pages/errorpage.html';
	HOME_PAGE = 'pages/index.html';

	@staticmethod
	def setFolders(rootFolder):
		Constants.ROOT_FOLDER = rootFolder + '/app/';
		Constants.STUFFS_FOLDER = Constants.ROOT_FOLDER + 'stuffs/';
		Constants.CONTROLLERS_FOLDER = Constants.ROOT_FOLDER + 'controllers/';
		Constants.MODELS_FOLDER = Constants.ROOT_FOLDER + 'models/';
		Constants.VIEWS_FOLDER = Constants.ROOT_FOLDER + 'views/';
		

def logMessage(message, additional='', indent=0):
	indentation = '\n=';
	for index in range(0, indent):
		indentation += '=';
	print indentation + '> ' + message + ' ' + additional;

if __name__ == '__main__':
	print 'Don\'t run this class...' 

