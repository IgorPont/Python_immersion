from unicodedata import decimal


def joiner(name_lst: list[str],
           salary_lst: list[int],
           award_lst: list[str]
           ) -> dict[str, float]:
    award_lst = list(map(lambda x: float(x.replace('%', '')) / 100, award_lst))

    return {name: round(salary * award, 2) for
            name, salary, award in
            zip(name_lst, salary_lst, award_lst)}


def main() -> None:
    name_lst: list[str] = ['First', 'Second', 'Third']
    salary_lst: list[int] = [120, 100, 140]
    award_lst: list[str] = ['10.25%', '7.75%', '9.45%']

    print(joiner(name_lst, salary_lst, award_lst))


if __name__ == '__main__':
    main()
