import unittest
from testing_example import calculate_credit


class NameTestCase(unittest.TestCase):
    def test_funk(self):
        b = 0.12
        calc = calculate_credit(20000, b, 36)
        self.assertTrue(int(calc))

    def test_type(self):
        self.assertRaises(Exception, calculate_credit,  '20000', '0.12', 32)

    def test_contain_lower_value(self):
        b = 0
        self.assertEqual(calculate_credit(20000, b, 36), 'Вы ввели недопустимое значение')

    def test_contain_over_value(self):
        b = 1.1
        self.assertEqual(calculate_credit(20000, b, 36), 'Вы ввели недопустимое значение')

    def test_contain_over_lower_value(self):
        b = -1
        self.assertEqual(calculate_credit(20000, b, 36), 'Вы ввели недопустимое значение')    
