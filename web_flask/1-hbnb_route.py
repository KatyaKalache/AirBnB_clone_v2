#!/usr/bin/python3
# starts a Flask web application
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_1():
    return "HBNB"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
