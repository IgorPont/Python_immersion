import json


class Factorial:
    storage = {}
    JSON_FILE = 'factorial.json'

    def __init__(self, k):
        self.k = k

    def __call__(self, n):
        if n not in self.storage:
            faktorial = 1
            for i in range(1, n + 1):
                faktorial *= i
            if len(self.storage) >= self.k:
                self.storage.pop(list(self.storage.keys())[0])
            self.storage[n] = faktorial
            return faktorial
        return self.storage[n]

    def __str__(self):
        return '\n'.join([f'{n}! = {storage}' for n, storage in self.storage.items()])

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.storage, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    with Factorial(4) as f:
        print(f(3))
        print(f(5))
        print(f(4))
        print(f(6))
        print(f.storage)