#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from wordconv_app.app import create_app
from wordconv_app import settings
from werkzeug import DebuggedApplication

flask_app = create_app()

if flask_app.config['DEBUG']:
    flask_app.debug = True
    flask_app = DebuggedApplication(flask_app, evalex=True)

app = flask_app
