from time import time


class MyStr(str):
    def __new__(cls, autor, value):
        instance = super().__new__(cls, value)
        instance.autor = autor
        instance.time = time()
        return instance

    # def __str__(self):
    #     return f'{self = } autor{self.autor = } time{self.time = }'


autor_1 = MyStr('Igot', 'text')
print(autor_1)
print(autor_1.split())
print(autor_1.upper())
