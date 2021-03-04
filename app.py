from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def index():
    """Returns the homepage"""
    req_words = silly_story.prompts
    return render_template("questions.html", words = req_words)

@app.route('/results')
def generate_story():
    """Get the form values"""
    
    # dict = {}
    
    # for arg in request.args:
    #     dict[arg] = request.args.get(arg)
    
    # return result(silly_story.generate(dict))
    
    return render_template("story.html", story = silly_story.generate(request.args))
