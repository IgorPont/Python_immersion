def char_to_ord(text: str) -> list[int]:
    """Converts and sorts characters in text into Unicode code"""
    res = list(map(ord, sorted(set(text), reverse=True)))
    return res


print(char_to_ord(input("Enter text: ")))
