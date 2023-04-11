str_ = input("Enter four integers ore more with separator '/': ")
a, b, c, *d = map(int, str_.split('/'))
dict_ = {b: a, c: tuple(d)}
print(dict_)
