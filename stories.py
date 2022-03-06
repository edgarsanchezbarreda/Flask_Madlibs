from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbar


app = Flask(__name__)
app.config['SECRET_KEY'] = 'helloworld'

debug = DebugToolbar(app)



class Story:
    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

@app.route('/')
def home():
    prompts = story.prompts

    return render_template('home.html', prompts=prompts)

@app.route('/story')
def story():
    place = request.args['place']
    noun = request.args['noun']
    verb = request.args['verb']
    adjective = request.args['adjective']
    plural_noun = request.args['plural_noun']
    return render_template('story.html')