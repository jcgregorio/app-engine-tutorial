#!/usr/bin/env python

import os
import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class IndexHandler(webapp.RequestHandler):

  def get(self):
    template_values = {"foo" : 1}
    
    template_file = os.path.join(os.path.dirname(__file__), "index.html")
    self.response.out.write(template.render(template_file, template_values))


def main():
  application = webapp.WSGIApplication([('/', IndexHandler)], debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
  

