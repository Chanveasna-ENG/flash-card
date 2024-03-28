import csv
from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # replace with your secret key

# Read questions from CSV file
questions = []
with open('question_answer.csv', 'r') as file:
    reader = csv.reader(file, delimiter='|')
    next(reader)
    for row in reader:
        questions.append({row[0]: row[1].replace(' \\n', '<br>')})

@app.route('/')
def quiz():
    q, a = list(random.choice(questions).items())[0]
    return render_template('quiz.html', question=q, answer=a)

@app.route('/next')
def next_question():
    q, a = list(random.choice(questions).items())[0]
    return render_template('quiz.html', question=q, answer=a)

# @app.route('/')
# def quiz():
#     session['question_index'] = 0
#     q, a = list(questions[session['question_index']].items())[0]
#     return render_template('quiz.html', question=q, answer=a)

# @app.route('/next')
# def next_question():
#     session['question_index'] += 1
#     if session['question_index'] >= len(questions):
#         return redirect(url_for('end'))
#     q, a = list(questions[session['question_index']].items())[0]
#     return render_template('quiz.html', question=q, answer=a)

# @app.route('/end')
# def end():
#     return "End of questions."

if __name__ == '__main__':
    app.run(debug=True)