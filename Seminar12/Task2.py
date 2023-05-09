class Generator:
    def __init__(self, start, stop, step):
        self.fct_range = [*range(start, stop, step)]
        # print(self.fct_range)

    @staticmethod
    def calc(limit):
        if limit < 0:
            raise ValueError('Incompatible value')
        if limit in (0, 1):
            return 1
        result = 1
        for i in range(1, limit + 1):
            result *= i
        return result

    def __iter__(self):
        return self

    def __next__(self):
        if self.fct_range:
            return self.calc(self.fct_range.pop(0))
        raise StopIteration

    def __str__(self):
        return f'Factorials range: {self.fct_range}'


if __name__ == '__main__':
    factorials = Generator(5, 10, 1)
    print(factorials)
    for i in factorials:
        print(i)
