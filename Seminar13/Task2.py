def get_dict_value(my_dict, my_key, default_value=None):
    try:
        res = my_dict[my_key]
    except KeyError as e:
        print(f'There is no such key {2} in dictionary')
        res = default_value
    return res


if __name__ == '__main__':
    dict_ = {1: 2, 3: 4}
    print(get_dict_value(dict_, 2))
