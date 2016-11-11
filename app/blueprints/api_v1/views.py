# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2016, Paul Cunningham'

from .resources import Sentences, Paragraphs
from flask import Blueprint
import flask_restful

API_VERSION_V1 = 1
API_VERSION = API_VERSION_V1

api_v1_bp = Blueprint('api', __name__)
api_v1 = flask_restful.Api(api_v1_bp)

api_v1.add_resource(Sentences, '/sentences/<int:count>/<string:response_format>')
api_v1.add_resource(Paragraphs, '/paragraphs/<int:count>/<string:response_format>')