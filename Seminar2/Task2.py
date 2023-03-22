import sys

data = [11, 11.11, 'Hello', True]
for count, i in enumerate(data, start=1):
    if isinstance(i, str):
        print("It's a string")
    elif isinstance(i, int):
        print("It's an integer")
    print(f"{count=}, entity {i}, addres {id(i)}, size in memmory {sys.getsizeof(i)}, hash {hash(i)}")
