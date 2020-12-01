def get_keys(listed_dicts):
    return listed_dicts.keys()


def get_new_id(listed_dicts):
    current_ids = [question['id'] for question in listed_dicts]
    return max(current_ids)+1


def add_to_data(listed_dicts, question):
    listed_dicts.append(question)
