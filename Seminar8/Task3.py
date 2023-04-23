import json
import csv


def reader(json_name: str) -> dict[str, str, str]:
    with open(json_name, 'r', encoding='utf-8') as f_in:
        new_dict = json.load(f_in)
    return new_dict


def write_to_csv(user_dict: dict, csv_name: str) -> None:
    users_data = [[i_lvl, u_id, u_nm]
                  for i_lvl, i_usr in user_dict.items()
                  for u_id, u_nm in i_usr.items()]
    print(users_data)
    with open(csv_name, 'w', encoding='utf-8') as f_out:
        csv_writer = csv.writer(f_out, dialect='excel', delimiter=';')
        csv_writer.writerows(users_data)


if __name__ == '__main__':
    write_to_csv(reader('test2.json'), 'test3.csv')
