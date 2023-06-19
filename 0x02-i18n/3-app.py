#!/usr/bin/env python3

"""Module instantiates babel object"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """configures language """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/", strict_slashes=False)
def welcome():
    """renders 3-index.html"""
    return render_template("3-index.html")


@babel.localeselector
def get_locale():
    """get best match"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


"""babel.init_app(app, locale_selector=get_locale)"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
