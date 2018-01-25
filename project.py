import os
from bottle import route, run

@route('/')
def index():
    return "<a href='/sectiona'>Liður A</a>" \
            "<a href='/sectionb'>Liður B</a>"

@route('/sectiona')
def a():
    return "Liður A"

@route('/sectionb')
def b():
    return "Liður B"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
