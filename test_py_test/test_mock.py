"""测试和mock使用."""
class Calculator(object):
    def add(self, a, b):
        return a+b

    def add2(self, a, b):
        a = self.add(a, b)
        return self.add(a, b)

def go_add(a, b):
    return Calculator().add2(a, b)

def multiple(a, b):
    return a*b

def go_multiple(a, b):
    return multiple(a, b)

import unittest
from unittest import mock
class TestProducer(unittest.TestCase):
    def setUp(self):
        pass
        self.calculator = Calculator()

    def test_add(self):
        # 非mock
        self.calculator = Calculator()
        self.assertEqual(self.calculator.add(2, 1), 3)
        #self.assertEqual(self.calculator.add(2, 2), 3) # 报错函数

    @mock.patch.object(Calculator, 'add')
    def test_add_by_mock(self, mock_add):
        # mock 用来指定add返回值(并不实际调用).
        mock_add.return_value = 3
        self.assertEqual(self.calculator.add(2, 12), 3)

    @mock.patch.object(Calculator, 'add')
    def test_add2(self, mock_add):
        # mock 用来指定add返回值(并不实际调用). 换个入的方法试试
        mock_add.return_value = 3
        #self.assertEqual(go_add(2, 12), 4)
        self.assertEqual(go_add(2, 12), 3)


class TestProducer(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    @mock.patch('test_mock.multiple')
    def test_multiple(self, mock_multiple):
        mock_multiple.return_value = 3
        #self.assertEqual(multiple(8, 14), 3) #并没有被mock
        self.assertEqual(go_multiple(8, 14), 3)

    @mock.patch('hey.hey.print_hey')
    def test_hey(self, mock_hey):
        from hey.hey import print_hey
        mock_hey.return_value = 2
        #self.assertEqual(multiple(8, 14), 3) #并没有被mock
        self.assertEqual(print_hey(), 3)

if __name__ == '__main__':unittest.main()
