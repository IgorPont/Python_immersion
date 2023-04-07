def get_list_from_string(text: str) -> str:
    """Numerates and sorts text words by age"""
    res = ''
    world_list = sorted(text.split())
    max_len = len(max(world_list, key=len))

    for i, el in enumerate(world_list, start=1):
        res += f'{i} {el:>{max_len}}\n'

    return res


user_input = input("Enter text: ")
print(get_list_from_string(user_input))
