"""flask blog app."""
from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g
import sqlite3

# configuration
DATABASE = 'blog.db'

app = Flask(__name__)

app.config.from_object(__name__)


def connect_db():
    """connecting to database."""
    return sqlite3.connect(app.config['DATABASE'])


@app.route('/')
def main():
    """main page."""
    return render_template('main.html')


@app.route('/login')
def login():
    """login page."""
    return render_template('login.html')

if __name__ == '__name__':
    app.run(debug=True)
