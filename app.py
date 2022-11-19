from flask import Flask, render_template, request, redirect
import surveys as s
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "secretkeysaredumb12345"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def home_page():
    title = s.satisfaction_survey.title
    instructions = s.satisfaction_survey.instructions
    return render_template('home.html', title=title, instructions=instructions)

@app.route('/questions/<int:num>')
def display_question(num):
    title = s.satisfaction_survey.title
    question = s.satisfaction_survey.questions[num].question
    choices = s.satisfaction_survey.questions[num].choices
    return render_template('questions.html', title=title, question=question, \
        choices=choices, num=num)


