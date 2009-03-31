#!/usr/bin/env python

import os
import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import memcache
import logging

class ToDoModel(db.Model):
  description = db.StringProperty()  
  created = db.DateTimeProperty(auto_now_add=True)  

class ItemCount(db.Model):
  total = db.IntegerProperty(default=0)

class IndexHandler(webapp.RequestHandler):

  def get(self):
    body = memcache.get("index")
    if body is None:
      items = ToDoModel.all().order("-created").fetch(100)
      count = ItemCount.get_or_insert("created_items")
      template_values = {"items": items, "total": count.total }
      template_file = os.path.join(os.path.dirname(__file__), "index.html")
      body = template.render(template_file, template_values)
      memcache.add("index", body)
    else:
      logging.info("Memcache hit!")
    self.response.out.write(body)
  
  def post(self):
    memcache.delete("index")
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
  

