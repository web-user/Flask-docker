from flask import Flask, render_template, session, redirect, url_for
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('base.html', title='Home')


if __name__ == "__main__":
    # Only for debugging while developing
    app.run()