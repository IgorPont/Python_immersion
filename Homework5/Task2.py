"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем словарь с именем
в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии.
"""


def worker_bonus(name_lst: list[str],
           salary_lst: list[int],
           award_lst: list[str]
           ) -> dict[str, float]:
    """A function that calculates the premium depending on the percentage"""
    award_lst = list(map(lambda x: float(x.replace('%', '')) / 100, award_lst))

    return {name: round(salary * award, 2) for
            name, salary, award in
            zip(name_lst, salary_lst, award_lst)}


name_lst: list[str] = ['Ivan', 'Fedor', 'Igor']
salary_lst: list[int] = [120, 100, 140]
award_lst: list[str] = ['10.25%', '7.75%', '9.45%']

print(worker_bonus(name_lst, salary_lst, award_lst))
