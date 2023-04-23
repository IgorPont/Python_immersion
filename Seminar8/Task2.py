import json


def get_user_info(json_file: str) -> None:
    used_ids = set()
    levels = set(range(1, 8))
    users = {}

    # with open(json_file, 'r', encoding='utf-8') as f:
    #     users = json.load(f)

    # for _, val in users.items():
    #     for _, id in val.items():
    #         used_ids.add(id)

    while True:
        user_name, user_id, user_level = input(
            'Enter the name, ID, access level, separated by a space > ').split()
        user_id = int(user_id)

        while user_id in used_ids:
            print('A user with this name already exists')
            user_name, user_id, user_level = input(
                'Enter the name, ID, access level, separated by a space > ').split()
        else:
            used_ids.add(user_id)

        user_level = int(user_level)
        while user_level not in levels:
            print(f'Access level {user_level} does not exist')
            user_name, user_id, user_level = input(
                'Enter the name, ID, access level, separated by a space > ').split()

        users.setdefault(user_level, {})[user_name] = user_id
        print(users)
        with open(json_file, 'w', encoding='utf-8') as f_json:
            json.dump(users, f_json, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    get_user_info('test2.json')
