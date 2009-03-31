#!/usr/bin/env python

import os
from google.appengine.ext.webapp import template

def main():
    template_values = {"foo" : [1,2,3]}    
    template_file = os.path.join(
		 os.path.dirname(__file__), "index.html")
    body = template.render(
      template_file, template_values)
    print "Status: 200 OK"
    print "Content-type: text/html"
    print
    print body

if __name__ == '__main__':
  main()
