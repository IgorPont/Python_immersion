import json
from typing import Callable


def log_to_json(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> None:
        result = func(args, kwargs)

        json_file = f'{func.__name__}.json'
        data = []
        for i, arg in enumerate(args):
            data.append({f'arg.{i}': arg})
        for key, val in kwargs.items():
            data.append({key: val})
        data.append({'result': result})
        with open(json_file, mode='a', encoding='utf-8') as f:
            json.dump(data, f)

        return result

    return wrapper


@log_to_json
def show(*args, **kwargs):
    print(*args, **kwargs)


if __name__ == '__main__':
    show(1, 3, k=4)
