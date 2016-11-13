# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2016, Paul Cunningham'

from flask import Blueprint, render_template, flash, redirect, url_for, request, session
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator

from app.ext import nav
from app.blueprints.frontend.forms import IpsumV1Form

frontend = Blueprint('frontend', __name__)

nav.register_element('frontend_top', Navbar(View('Lorem Ipsum', '.index'), View('Home', '.index')))


@frontend.route('/', methods=['GET', 'POST'])
def index():

    # setup a default form with its equivalent REST url

    kwargs = {
        'resource': session.get('resource') or 'api_v1.paragraphs',
        'count': session.get('count') or 5,
        'response_format': session.get('response_format') or 'html'
    }

    form = IpsumV1Form(**kwargs)
    resource = kwargs.pop('resource')
    rest_url = url_for(resource, **kwargs)
    external_rest_url = url_for(resource, _external=True, **kwargs)

    if form.validate_on_submit():

        session['resource'] = form.resource.data
        session['count'] = form.count.data
        session['response_format'] = form.response_format.data

        return redirect(url_for('frontend.index'), code=303)

    # session['resource'] = None
    # session['count'] = None
    # session['response_format'] = None

    return render_template('index.html', form=form, iframe_source_url=rest_url, external_rest_url=external_rest_url)


@frontend.route('/about/', )
def about():
    return render_template('about.html')

