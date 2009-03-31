#!/usr/bin/env python

import os
import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext.webapp.util import login_required

class IndexHandler(webapp.RequestHandler):

  @login_required
  def get(self):
    template_values = {
      "name" : users.get_current_user().nickname(),
      "logout": users.create_logout_url(self.request.uri)
      }
    template_file = os.path.join(os.path.dirname(__file__), "index.html")
    self.response.out.write(template.render(template_file, template_values))


def main():
  application = webapp.WSGIApplication([('/', IndexHandler)], debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
  

