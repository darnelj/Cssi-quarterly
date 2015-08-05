#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
import json
from google.appengine.ext import ndb
from google.appengine.api import users

# from oauth2client import client

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Goals(ndb.Model):
    goal = ndb.StringProperty()
    time_frame = ndb.IntegerProperty()
    q1 = ndb.StringProperty()
    q2 = ndb.StringProperty()
    q3 = ndb.StringProperty()
    q4 = ndb.StringProperty()
    user_id = ndb.StringProperty()

class Login(ndb.Model):
    user = ndb.StringProperty()
    password = ndb.StringProperty()
    goal_key = ndb.KeyProperty(Goals)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'test' : 'working'
        }
        template = JINJA_ENVIRONMENT.get_template('html/index.html')
        self.response.write(template.render(template_values))

class LoginHandler(webapp2.RequestHandler):
  def get(self):
    print "hello, world"
    user = users.get_current_user()
    if user:
        greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                    (user.nickname(), users.create_logout_url('/')))
        self.response.write('<html><body>%s</body></html>' % greeting)
    else:
        greeting = ('<a href="%s">Sign in or register</a>.' %
                    users.create_login_url('/'))
        self.response.write('<html><body>%s</body></html>' % greeting)
class GoalHandler(webapp2.RequestHandler):
    def get(self):
        namegoal = self.request.get('namegoal')
        items = ['Set up task for Q1', 'Set up task for Q2', 'Set up task for Q3', 'Set up task for Q4']
        template_values = {
            'items': items,
            'namegoal': namegoal
        }
        template = JINJA_ENVIRONMENT.get_template('html/ind_goal.html')
        # Put in Giacomo's page line 41 from test to whatever he's named it
        self.response.write(template.render(template_values))
    # put underneath the creation of goal records in datastore
    def post(self):
        # put here the creation of goal records in datastore
        pass
class Goal_pageHandler(webapp2.RequestHandler):
    def get(self):
        namegoal = self.request.get('namegoal')
        template_values = {
            'test' : 'working',
            'namegoal': namegoal
        }
        template = JINJA_ENVIRONMENT.get_template('html/goal_page.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/goal', GoalHandler),
    ('/list', Goal_pageHandler),
    ('/login', LoginHandler)
], debug=True)
