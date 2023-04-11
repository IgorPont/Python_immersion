"""
Создайте функцию генератор чисел Фибоначчи (см. Википедию)
"""


def fib(num: [int]) -> str:
    """Fibonacci number generator"""
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b, a + b


gen_fib = list(fib(20))
print(gen_fib)
