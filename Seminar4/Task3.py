def get_numbers_unicode(num: str) -> dict[str, int]:
    """Converts a string of numbers into a Unicode dictionary of character codes"""
    num1, num2 = map(int, sorted(num.split()))
    res = {}
    for i in range(num1, num2 + 1):
        # res.setdefault(chr(i), i)
        res[chr(i)] = i
    return res


print(get_numbers_unicode('100 200'))
