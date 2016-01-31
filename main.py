import os
import urllib
import operator

from operator import itemgetter
from google.appengine.api import users
from google.appengine.ext import ndb

import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render())

class Landing(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('landing.html')
        self.response.write(template.render())
class CreateParty(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('create_party.html')
        self.response.write(template.render())
class JoinParty(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('join_party.html')
        self.response.write(template.render())

class Party(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('party.html')
        self.response.write(template.render())
        
app = webapp2.WSGIApplication([
        ('/', MainPage),
        ('/landing', Landing),
        ('/create', CreateParty),
        ('/join', JoinParty),
        ('/party' Party),
], debug=True)
