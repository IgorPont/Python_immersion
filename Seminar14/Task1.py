"""
Тестирование с помощью doctest
"""
from string import ascii_letters, whitespace


def convert_string(source_string: str) -> str:
    """
    >>> convert_string('this is the test string')
    'this is the test string'
    >>> convert_string('This Is The TEST STRING')
    'this is the test string'
    >>> convert_string('.,,,thiS iS ,,the test string')
    'this is the test string'
    >>> convert_string('thiфвыафВЫs is ваАthe test ЫФВЫstring')
    'this is the test string'
    """
    if not isinstance(source_string, str):
        raise TypeError('Argument must be a string')
    true_chars = ascii_letters + whitespace
    return "".join(c for c in source_string if c in true_chars).lower()


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
