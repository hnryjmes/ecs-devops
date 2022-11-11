"""Main application file"""
from flask import Flask

app = Flask(__name__)


@app.route("/<the_string>")
def return_backwards_string(the_string):
    """Reverse and return the provided URI"""
    return "".join(reversed(the_string))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
