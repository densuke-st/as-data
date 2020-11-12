#!/usr/bin/env python

from bottle import route, run, response
import json
import socket

@route("/")
def index():
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    ret =  {
        "path": "/",
        "message": "index",
    }
    return json.dumps(ret)

@route("/host")
def get_myhost():
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    ret =  {
        "path": "/host",
        "message": socket.gethostname(),
    }
    return json.dumps(ret)


if __name__ == "__main__":
    run(host="0.0.0.0", port=80)