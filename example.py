# -*- coding=utf-8 -*-
import os
import imp
import sys
import time
import gzip
from io import StringIO
from Cheetah.Template import Template

def tt(request,response_head):
	#print request.form
	#print request.getdic
	#print request.postdic
	return "ccb"+request.path

def getdata(request,response_head):
	f=open("a.txt")
	content = f.read()
	f.close()
	response_head["Content-Encoding"] = "gzip"
	return content

def template(request,response_head):
	t = Template(file="template.html")
	t.title = "my title"
	t.contents = "my contents"
	reaponse_head["Content-Encoding"] = "gzip"
	return str(t)
