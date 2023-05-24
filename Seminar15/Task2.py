import logging
from typing import Callable

logging.basicConfig(
    filename='Task2.log',
    filemode='w',
    encoding='utf-8',
    level=logging.INFO,
    style='{',
    format='{levelname:<3} - {asctime}. {msg}'
)
logger = logging.getLogger(__name__)


def data_to_log(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> None:
        result = func(args, kwargs)

        data = []
        for i, arg in enumerate(args):
            data.append({f'arg.{i}': arg})
        for key, val in kwargs.items():
            data.append({key: val})
        data.append({'result': result})
        msg = f'Function: {func.__name__}, {data}'
        logging.info(msg)
        return result

    return wrapper


@data_to_log
def show(*args, **kwargs):
    print(*args, **kwargs)


if __name__ == '__main__':
    show(1, 3, k=4)
