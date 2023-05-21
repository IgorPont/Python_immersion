"""
Тестирование с помощью unittest
"""
from Task1 import convert_string
import unittest


class TestConvertString(unittest.TestCase):

    def test_without_chnges(self):
        self.assertEqual(convert_string('this is the test string'), 'this is the test string')

    def test_fix_case(self):
        self.assertEqual(convert_string('This Is The TEST STRING'), 'this is the test string')

    def test_fix_punctuation(self):
        self.assertEqual(convert_string('.,,,thiS iS ,,the test string'), 'this is the test string')

    def test_fix_all(self):
        self.assertEqual(convert_string('thiфвыафВЫs is ваАthe test ЫФВЫstring'), 'this is the test string')


if __name__ == '__main__':
    unittest.main(verbosity=2)
