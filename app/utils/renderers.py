# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2016, Paul Cunningham'

from flask_bootstrap.nav import BootstrapRenderer


class InverseRenderer(BootstrapRenderer):
    def visit_Navbar(self, node):
        nav_tag = super(InverseRenderer, self).visit_Navbar(node)
        nav_tag['class'] += 'navbar navbar-inverse navbar-fixed-top'
        return nav_tag