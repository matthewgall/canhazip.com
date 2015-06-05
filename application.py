#!/usr/bin/env python

import os
import sys
import json
from bottle import route, request, response, run, template, error, default_app, HTTPResponse
from pprint import pprint

@error(404)
def error404(error):
    response.status = 404
    response.content_type = 'text/plain'
    return 'Nothing here, sorry'

@route('/headers')
def asheaders():
    headers = {}
    for key in request.headers.keys():
        headers[key] = request.headers.get(key)

    response.content_type = 'application/json'
    return json.dumps(headers)

@route('/json')
def asjson():
    response.content_type = 'application/json'
    content = {
        'ip': request.get('REMOTE_ADDR')
    }
    return json.dumps(content)

@route('/')
def index():
    ip = request.get('REMOTE_ADDR')
    response.content_type = 'text/plain'
    return ip

if __name__ == '__main__':

    application = default_app()

    serverHost = os.getenv('SERVER_HOST', 'localhost')
    serverPort = os.getenv('PORT', '5000')

    # Now we're ready, so start the server
    try:
        application.run(host=serverHost, port=serverPort)
    finally:
        exit()
