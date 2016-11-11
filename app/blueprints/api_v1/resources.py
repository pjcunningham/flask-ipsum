# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2016, Paul Cunningham'

from flask import Flask, render_template_string, Response
from flask_restful import Resource, Api, reqparse
from loremipsum import get_sentences, get_paragraphs

HTML_TEMPLATE = '''
<!doctype html>
<html lang=en>
<head>
<meta charset=utf-8>
<title>Lorum Ipsum</title>
</head>
<body>
    {% for item in items %}
        <p>{{item | safe }}</p>
    {% endfor %}
</body>
</html>
'''


TEXT_TEMPLATE = '''
{%- for item in items %}
{{item}} {{'\n'}}
{% endfor %}
'''


def output_html(data, code, headers=None):
    resp = Response(render_template_string(HTML_TEMPLATE, items=data), mimetype='text/html', headers=headers)
    resp.status_code = code
    return resp


def output_text(data, code, headers=None):
    resp = Response(render_template_string(TEXT_TEMPLATE, items=data), mimetype='text/plain', headers=headers)
    resp.status_code = code
    return resp


class Sentences(Resource):

    def get(self, count, response_format=None):
        count = min(count, 100)
        items = get_sentences(count)
        if response_format.lower() == 'html':
            return output_html(items, 200)
        elif response_format.lower() == 'text':
            return output_text(items, 200)
        return {'sentences': items}


class Paragraphs(Resource):

    def get(self, count, response_format=None):
        count = min(count, 100)
        items = get_paragraphs(count)
        if response_format.lower() == 'html':
            return output_html(items, 200)
        elif response_format.lower() == 'text':
            return output_text(items, 200)
        return {'paragraphs': items}