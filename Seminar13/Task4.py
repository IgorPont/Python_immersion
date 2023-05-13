import json


class User:
    def __init__(self, name: str, user_id: int, level: int) -> None:
        self.name = name
        self.user_id = user_id
        self.level = level

    def __str__(self) -> str:
        return f'user: {self.name}, id: {self.user_id}, level: {self.level}'


def get_users(file_json: str) -> set[User]:
    with open(file_json, mode='r', encoding='utf-8') as f:
        user_data = json.load(f)
    users = [User(user['name'], user['id'], user['level']) for user in user_data]
    return set(users)


if __name__ == '__main__':
    for user in get_users('users.json'):
        print(user)
