#!/usr/bin/env python

import os
import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db

class ToDoModel(db.Model):
  description = db.StringProperty()  
  created = db.DateTimeProperty(auto_now_add=True)
  foo = db.FloatProperty(default=3.14)
  bar = db.IntegerProperty()
  baz = db.BooleanProperty(default=False)  
  N = db.IntegerProperty()
  l = db.ListProperty(str, default=["foo", "bar"])
  

class IndexHandler(webapp.RequestHandler):

  def get(self):
    todo = ToDoModel(description = "Hello World", bar=1, baz=True)
    todo.put()

def main():
  application = webapp.WSGIApplication([('/', IndexHandler)], debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
  

