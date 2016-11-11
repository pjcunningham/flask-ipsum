# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2016, Paul Cunningham'

from flask import Flask
from flask_appconfig import AppConfig

from .blueprints.frontend.views import frontend
from .ext import nav, bootstrap, debug


def create_app(configfile=None):
    # We are using the "Application Factory"-pattern here, which is described
    # in detail inside the Flask docs:
    # http://flask.pocoo.org/docs/patterns/appfactories/

    app = Flask(__name__)

    # We use Flask-Appconfig here, but this is not a requirement
    AppConfig(app, configfile)

    # Install our Bootstrap extension
    bootstrap.init_app(app)

    debug.init_app(app)

    # Our application uses blueprints as well; these go well with the
    # application factory. We already imported the blueprint, now we just need
    # to register it:
    app.register_blueprint(frontend)

    # Because we're security-conscious developers, we also hard-code disabling
    # the CDN support (this might become a default in later versions):
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True

    # We initialize the navigation as well
    nav.init_app(app)

    # REST V1
    from app.blueprints.api_v1.views import api_v1_bp
    app.register_blueprint(api_v1_bp, url_prefix='/api/v1')

    return app