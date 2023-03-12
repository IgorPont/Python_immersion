"""
1.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны
с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других,
то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним.
"""


def triangle_check(a, b, c):
    res = None
    if a + b > c and a + c > b and b + c > a:
        if a == b and a == c and b == c:
            res = f'This is an equilateral triangle'
        elif a != b and a != c and b != c:
            res = f'This is an irregular triangle'
        elif a == b or a == c or b == c:
            res = f'This is an isosceles triangle'
    else:
        res = f'The triangle is invalid'
    return res


# Test
print(triangle_check(6, 3, 4))
