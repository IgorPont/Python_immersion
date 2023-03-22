a, b, c = int(input('Enter a: ')), int(input('Enter b: ')), int(input('Enter c: '))
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    res = f'Roots of equation are {x1=}, {x2=}'
elif d == 0:
    x = -b / (2 * a)
    res = f'Eqations has only one root {x=}'
else:
    d: complex = complex(d, 0)
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    res = f'Complex roots of equation are {x1=}, {x2=}'
print(res)
