import os
from bottle import route, run

@route('/')
def index():
    return "<a href='/section_a'>Liður A</a>" \
            "<a href='/section_b'>Liður B</a>" \

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

@route('/section_a')
def a():
    return "a"

@route('/section_b')
def b():
    return "b"
