from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World from Flask in a uWSGI Nginx Docker container with \
     Python 3.6 (from the example template) 123"


if __name__ == "__main__":
    # Only for debugging while developing
    app.run()