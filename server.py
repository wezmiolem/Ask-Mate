from flask import Flask, render_template, url_for, request, redirect
from data_example import questions
import data_processing

app = Flask(__name__)


@app.route('/')
def index():
    headers = ['Question ID', 'Time of a submission', 'number of views', 'number of votes', 'type of a question',
               'question message', 'question image']
    question_keys = data_processing.get_keys(questions[0])
    return render_template('index.html', questions=questions, headers=headers, question_keys=question_keys)


@app.route('/add_update')
def add_update():
    return render_template('add_update.html')


@app.route('/add_update/post', methods=['POST'])
def add_question():
    new_question = dict(request.form)
    new_question['id'] = data_processing.get_new_id(questions)
    new_question['submission_time'] = 'now'
    new_question['view_number'] = 0
    new_question['vote_number'] = 0
    data_processing.add_to_data(questions, new_question)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
