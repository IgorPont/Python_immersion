def decoretor(count: int):
    def decoretor_2(func):
        counter = []

        def wrapper(*args, **kwargs):
            for _ in range(count):
                res = func(*args, **kwargs)
                counter.append(res)
            return counter

        return wrapper

    return decoretor_2


@decoretor(10)
def fun():
    return 1


print(fun())
