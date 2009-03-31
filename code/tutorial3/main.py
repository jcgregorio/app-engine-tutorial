#!/usr/bin/env python

import os
from wsgiref.handlers import CGIHandler
from google.appengine.ext.webapp import template
from wsgidispatcher import Dispatcher

def index(environ, start_response):
    template_values = {"foo" : 1}    
    template_file = os.path.join(
		  os.path.dirname(__file__), "index.html")
    body = template.render(
      template_file, template_values)
    start_response("200 OK", [('content-type', 'text/html')])
    return [body]

urls = Dispatcher()
urls.add('/', GET=index)

def main():
    CGIHandler().run(urls)

if __name__ == '__main__':
  main()

