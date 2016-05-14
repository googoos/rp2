from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g
import sqlite3
import os

# configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORDS = 'admin'
SECRETKEY = b'\xd5r\xb1\xd6\x14\x03\xca\xb1\x1cn\xad\t\xdcj\x86:P\xdfGf\x1b\xac\r!'

app = Flask(__name__)

app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/sk')
def skey():
    return str(os.urandom(24))


if __name__ == '__main__':
    app.run(debug=True)
