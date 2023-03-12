rows = int(input('Enter rows quantity:\n'))
spruce = ''
for i in range(rows):
    spruce += (rows - 1 - i) * ' ' + (2 * i + 1) * '*' + (rows - 1 - i) * ' ' + '\n'
print(spruce)
