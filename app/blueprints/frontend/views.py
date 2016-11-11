# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2016, Paul Cunningham'

# This contains our frontend; since it is a bit messy to use the @app.route
# decorator style when using application factories, all of our routes are
# inside blueprints. This is the front-facing blueprint.
#
# You can find out more about blueprints at
# http://flask.pocoo.org/docs/blueprints/

from flask import Blueprint, render_template, flash, redirect, url_for
from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from markupsafe import escape

# from .forms import SignupForm
from app.ext import nav

frontend = Blueprint('frontend', __name__)

nav.register_element('frontend_top', Navbar(View('Lorem Ipsum', '.index'), View('Home', '.index')))


@frontend.route('/')
def index():
    return render_template('index.html')


# # Shows a long signup form, demonstrating form rendering.
# @frontend.route('/example-form/', methods=('GET', 'POST'))
# def example_form():
#     form = SignupForm()
#
#     if form.validate_on_submit():
#         # We don't have anything fancy in our application, so we are just
#         # flashing a message when a user completes the form successfully.
#         #
#         # Note that the default flashed messages rendering allows HTML, so
#         # we need to escape things if we input user values:
#         flash('Hello, {}. You have successfully signed up'
#               .format(escape(form.name.data)))
#
#         # In a real application, you may wish to avoid this tedious redirect.
#         return redirect(url_for('.index'))
#
#     return render_template('signup.html', form=form)