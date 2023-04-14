import calendar
from sys import argv


def _user_input() -> str:
    """A function that asks the user for the date"""
    us_input = input("Enter the date in the format 'dd.mm.yyyyy':\n")
    return us_input


def _leap_year(year: str) -> bool:
    """Checking the year for leap years"""
    return calendar.isleap(int(year))


def check_the_date(string: str) -> bool:
    """The function that checks the date for existence in Gregorian calendar"""
    day, month, year = string.split('.')
    if _leap_year(year) is True and int(month) == 2 and int(day) > 28:
        return False
    elif int(day) < 32 and int(month) < 13 and int(year) < 9999:
        return True
    else:
        return False


if __name__ == "__main__":
    # print(check_the_date(_user_input()))
    file_name, *date = argv
    print(check_the_date(''.join(date)))
