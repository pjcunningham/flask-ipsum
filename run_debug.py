# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright = 'Copyright 2016, Paul Cunningham'

from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(host='localhost', port=5000, debug=True)
