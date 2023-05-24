import logging

logging.basicConfig(filename='Task1.log', encoding='utf-8', level=logging.WARNING)
logger = logging.getLogger(__name__)


def div(num_1: int, num_2: int) -> float:
    res = None
    try:
        res = num_1 / num_2
    except ZeroDivisionError as e:
        logger.error(e)
    return res


if __name__ == '__main__':
    print(div(2, 4))
    print(div(3, 0))
