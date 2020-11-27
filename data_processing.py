def get_keys(dict_data):
    return dict_data.keys()


def get_new_id(dict_data):
    current_ids = [question['id'] for question in dict_data]
    return max(current_ids)+1


def add_question(dict_data, question):
    dict_data.append(question)
