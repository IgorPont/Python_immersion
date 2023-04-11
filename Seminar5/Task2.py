text = "Привет!"

dict_ = {i: ord(i) for i in text}
print(dict_)

iter_ = iter(dict_.items())
print(next(iter_))
print(next(iter_))
print(next(iter_))
