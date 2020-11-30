questions = [{'id': 0, 'submission_time': 'today', 'view_number': 10, 'vote_number': 5, 'type': 'general',
             'message': 'to be or not to be?', 'image': 'None'},
             {'id': 1, 'submission_time': 'yesterday', 'view_number': 8, 'vote_number': 5, 'type': 'general',
              'message': 'you talkin to me?', 'image': 'None'},
             {'id': 2, 'submission_time': 'tomorrow', 'view_number': 7, 'vote_number': 5, 'type': 'unknown',
              'message': 'wasssup?', 'image': 'None'}]
HEADERS = ['User ID', 'Time of a submission', 'number of views', 'number of votes', 'type of a question',
           'question message', 'question image']

for i in range(len(questions)):
    print(questions[i]["message"])
