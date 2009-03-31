#!/usr/bin/env python

import os
import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db

class ToDoModel(db.Model):
  description = db.StringProperty()  
  created = db.DateTimeProperty(auto_now_add=True)  

class ItemCount(db.Model):
  total = db.IntegerProperty(default=0)

class IndexHandler(webapp.RequestHandler):

  def get(self):
    items = ToDoModel.all().order("-created").fetch(100)
    count = ItemCount.get_or_insert("created_items")
    template_values = {"items": items, "total": count.total }
    template_file = os.path.join(os.path.dirname(__file__), "index.html")
    self.response.out.write(template.render(template_file, template_values))    
  
  def post(self):
    description = self.request.get("description")
    todo = ToDoModel(description = description)
    todo.put()    
    def txn():
      count = ItemCount.get_by_key_name("created_items")
      count.total += 1
      count.put()
    db.run_in_transaction(txn)
    self.redirect("/")

def main():
  application = webapp.WSGIApplication([('/', IndexHandler)], debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
  

