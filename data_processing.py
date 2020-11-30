def get_keys(dict_data):
    return dict_data.keys()


def import_file(filename, mode, separator):
    with open(filename, mode) as file:
        file = file.readlines()
        data = [elem.strip("\n").split(separator) for elem in file]

    return data


def get_list_of_dict(keys_list, key_arguments):
    dict_list = []

    for elem in key_arguments:
        tmp = dict(zip(keys_list, elem))
        dict_list.append(tmp)

    return dict_list


def get_dict_from_list(keys, values):
    result = dict(zip(keys, values))
    return result


# data - dictionary data, key = value from header as string, order - string 'ascending' or 'descending'
def sort_data(data, key, order):
    if order == "ascending":
        return sorted(data, key=lambda x: x[key], reverse=False)
    elif order == "descending":
        return sorted(data, key=lambda x: x[key], reverse=True)


def verify_lists_for_dict(keys_list, key_arguments):
    incorrect_tmp = [key_arguments[i] for i in range(len(key_arguments)) if len(keys_list) != len(key_arguments[i])]

    if len(incorrect_tmp) != 0:
        print("\nIncorrect data lenght/number:\n")
        for elem in incorrect_tmp:
            print(len(elem), elem)
        print("\nCorrect data lenght/number is: ", len(keys_list))
        return False
