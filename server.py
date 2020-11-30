from flask import Flask, render_template, url_for
from data_example import questions
import data_processing

app = Flask(__name__)


@app.route('/')
def index():
    headers = ['User ID', 'Time of a submission', 'number of views', 'number of votes', 'type of a question',
               'question message', 'question image']
    question_keys = data_processing.get_keys(questions[0])
    return render_template('index.html', questions=questions, headers=headers, question_keys=question_keys)

@app.route('/list')
def list_of_question():
    headers = ['User ID', 'Time of a submission', 'number of views', 'number of votes', 'type of a question',
               'question message', 'question image']
    question_keys = data_processing.get_keys(questions[0])
    return render_template('list.html',questions=questions,headers=headers,question_keys=question_keys)

@app.route("/question")
def question():
    headers = ['User ID','type of a question','question message', 'question image']
    question_keys = ["id","type","message","image"]


    return render_template('question.html', questions=questions,headers=headers,question_keys=question_keys)

if __name__ == '__main__':
    app.run()
