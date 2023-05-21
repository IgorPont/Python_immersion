"""
Тестирование с помощью pytest
"""
import pytest
from Task1 import convert_string


def test_without_chnges():
    assert ('this is the test string' == convert_string('this is the test string'))


def test_fix_case():
    assert ('this is the test string' == convert_string('This Is The TEST STRING'))


def test_fix_punctuation():
    assert ('this is the test string' == convert_string('.,,,thiS iS ,,the test string'))


def test_fix_all():
    assert ('this is the test string' == convert_string('thiфвыафВЫs is ваАthe test ЫФВЫstring'))


def test_error(capfd):
    with pytest.raises(TypeError, match='Argument is to be a string'):
        convert_string(1000)


if __name__ == '__main__':
    pytest.main(['-v'])
