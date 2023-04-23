import json


def entry_txt_to_json(txt_file: str, json_file: str) -> None:
    """..."""
    with(
        open(txt_file, 'r', encoding='utf-8') as f_txt,
        open(json_file, 'w', encoding='utf-8') as f_json
    ):
        all_data = {}
        while data := f_txt.readline():
            name, number = data[:-1].split()
            all_data[name.capitalize()] = float(number)
        json.dump(all_data, f_json, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    entry_txt_to_json('test1.txt', 'test1.json')
