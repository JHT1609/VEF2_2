from bottle import route, run

@route('/')
def index():
    return "Hello"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
