from flask import render_template, request, redirect, url_for
from database import Session, Student, Course

@app.route('/')
def index():
    return render_template('index.html')

# More view functions...
