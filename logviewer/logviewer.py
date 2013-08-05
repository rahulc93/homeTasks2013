#!/usr/bin/env python

import flask


APP = flask.Flask(__name__)

@APP.route('/')
def index():
    return.flask.render_template('index.html')

@APP.route('/posts/<log_id>')
def view_log(log_id):
    return flask.render_template('log.html', name = log_id)


if __name__ == '__main__':
    APP.debug = True
    APP.run()
