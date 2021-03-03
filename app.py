from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def index():
    """Returns the homepage"""
    getInputs()
    return render_template("questions.html")

def getInputs():
    lst = silly_story.prompts
    print(lst)
