from requests_library.requests_setup import get_web_data


def count_user_messages(json_data, user_count):
    username = json_data['username']
    if username in user_count:
        user_count[username] += 1
    else:
        user_count[username] = 1

    if 'comments' in json_data:
        for comment in json_data['comments']:
            count_user_messages(comment, user_count)


def sort_dict_by_value(input_dict):
    sorted_dict = {
        key: value
        for key, value in sorted(
            input_dict.items(), key=lambda item: (-item[1], item[0])
        )
    }
    return sorted_dict


data = get_web_data('https://parsinger.ru/3.4/3/dialog.json', json=True)

users_count = {}
count_user_messages(data, users_count)

sorted_user_count = sort_dict_by_value(users_count)
print(sorted_user_count)
