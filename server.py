# System Modules
import re
from datetime import date

# Third-party Modules
from flask import Flask, request, json, redirect
from flask import render_template, url_for

# User-defined Modules
from db import Database

# connection to database
dbx = Database(hostname='192.168.12.136')

# app of this application
app = Flask(__name__)


# function to fetch the resource as string
def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)


# app configurations
app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string


@app.after_request
def add_header(r):

    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'

    return r


@app.route('/')
def index():

    data = dbx.get()
    return render_template('index.html', view=True, tasks=data)


@app.route('/task', methods=['POST'])
def create():

    # form details
    name = re.escape(request.form['task_name'])
    name = request.form['task_name']
    desc = re.escape(request.form['task_desc'])
    desc = request.form['task_desc']

    dbx.create(name, desc)
    
    return redirect('/')


@app.route('/task', methods=['DELETE'])
def delete():

    data = dbx.get()
    return render_template('index.html', view=True, tasks=data)


# run the app
app.run(host='0.0.0.0', port=8080, debug=False, use_reloader=False)

