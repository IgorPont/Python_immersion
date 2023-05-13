class BaseExeption(Exception):
    pass


class LevelError(BaseExeption):
    def __str__(self):
        return f'Ошибка уровня'


class AccesError(BaseExeption):
    def __str__(self):
        return f'Ошибка доступа'