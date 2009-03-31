#!/usr/bin/env python

import os
import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db

class ToDoModel(db.Model):
  description = db.StringProperty()  
  created = db.DateTimeProperty(auto_now_add=True)  


class ItemHandler(webapp.RequestHandler):

  def get(self, itemid):
    item = ToDoModel.get_by_id(int(itemid))
    template_values = {"item": item}
    template_file = os.path.join(os.path.dirname(__file__), "item.html")
    self.response.out.write(template.render(template_file, template_values))    

class IndexHandler(webapp.RequestHandler):

  def get(self):
    items = ToDoModel.all().order("-created").fetch(100)
    template_values = {"items": items}
    template_file = os.path.join(os.path.dirname(__file__), "index.html")
    self.response.out.write(template.render(template_file, template_values))    
  
  def post(self):
    description = self.request.get("description")
    todo = ToDoModel(description = description)
    todo.put()
    self.redirect("/")

def main():
  application = webapp.WSGIApplication(
     [
       ('/', IndexHandler),
       ('/item/(.*)', ItemHandler)
     ], debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
  

