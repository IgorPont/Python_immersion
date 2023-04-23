import csv
import json


def new_users(csv_file: str, json_file: str) -> None:
    with (
        open(csv_file, mode='r', newline='', encoding='utf-8') as f_csv,
        open(json_file, mode='w', encoding='utf-8') as f_json
    ):
        csv_read = csv.reader(f_csv, dialect='excel', delimiter=';')
        # print(*csv_read)
        all_data = []
        for row in csv_read:
            print(row)
            user = dict()
            user['id'] = f'{row[0]:0>10}'
            user['name'] = row[1].capitalize()
            user['level'] = row[2]
            user['hash'] = hash(f"{user['id']}{user['name']}")
            print(user)
            all_data.append(user)
        json.dump(all_data, f_json, indent=2)


if __name__ == '__main__':
    new_users('test3.csv', 'test4.json')
