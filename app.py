from flask import Flask, render_template, request, redirect
import surveys as s
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "secretkeysaredumb12345"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

responses = []
q_num = [1, len(s.satisfaction_survey.questions)]

@app.route('/')
def home_page():
    """Provide survey title and instructions to home page template"""
    responses.clear()
    q_num[0] = 1
    title = s.satisfaction_survey.title
    instructions = s.satisfaction_survey.instructions
    print(f'new session: responses {responses}, q_num {q_num}')
    return render_template('home.html', title=title, instructions=instructions)

@app.route('/questions/<int:num>')
def display_question(num):
    """Provide question/choices based on number"""
    idx = num - 1
    title = s.satisfaction_survey.title
    question = s.satisfaction_survey.questions[idx].question
    choices = s.satisfaction_survey.questions[idx].choices
    print(f'displaying question {num}')
    print(f'{responses} {q_num}')
    return render_template('questions.html', title=title, question=question, \
        choices=choices, num=num)

@app.route('/answer', methods=["POST"])
def record_answer():
    """Append user's posted answer to list of responses and figure out next page"""
    answer = request.form['question']
    print(f'question {q_num[0]} of {q_num[1]} response: {answer}')
    responses.append(answer)
    q_num[0] += 1
    print(f'{responses} {q_num}')
    
    url = f'/questions/{q_num[0]}'

    if q_num[0] <= q_num[1]:
        return redirect(url)
    else:
        return redirect('/thanks')

@app.route('/thanks')
def say_thanks():
    return render_template('thanks.html')
    



