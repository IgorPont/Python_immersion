import logging
import datetime

logging.basicConfig(
    filename='Task3.log',
    filemode='w',
    encoding='utf-8',
    level=logging.ERROR,
    style='{',
    format='{levelname:<3} - {asctime}. {msg}'
)
logger = logging.getLogger(__name__)


def parse_data(data: str) -> str:
    months = [
        'янв',
        'фев',
        'мар',
        'апр',
        'мая',
        'июн',
        'июл',
        'авг',
        'сен',
        'окт',
        'ноя',
        'дек',
    ]

    days = ['пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос']

    try:
        week_num, day, month = data.split()
        week_num = int(week_num.split('-')[0])
    except ValueError as e:
        logger.error(e)
        return None

    year = datetime.datetime.now().year
    month_num = months.index(month[:3]) + 1
    day_num = days.index(day[:3])

    counter = 0
    for i in range(1, 32):
        dat = datetime.datetime(day=i, month=month_num, year=year)
        if dat.weekday() == day_num:
            counter += 1
            if counter == week_num:
                return dat


if __name__ == '__main__':
    dt = '2-й четверг сентября'
    print(parse_data(dt))
