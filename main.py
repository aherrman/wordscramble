#!/usr/bin/env python

import scrambler
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util


class MainHandler(webapp.RequestHandler):
  def get(self):
    template_values = {
      'original': '',
      'scrambled': ''
    }
    path = os.path.join(os.path.dirname(__file__), 'scrambler.html')
    self.response.out.write(template.render(path, template_values))

  def post(self):
    contents = self.request.get('content')
    template_values = {
      'original': contents,
      'scrambled': scrambler.text_scramble(contents)
    }
    path = os.path.join(os.path.dirname(__file__), 'scrambler.html')
    self.response.out.write(template.render(path, template_values))


def main():
  application = webapp.WSGIApplication([('/', MainHandler)],
                                       debug=True)
  util.run_wsgi_app(application)


if __name__ == '__main__':
  main()
