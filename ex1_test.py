# lab №1 ex. 1(test) | Var 9 Sergey Zubrilin 9/21/18


from ex1 import ex1
import unittest


class TestEx1(unittest.TestCase):

    def test_eps1(self):
        self.assertEqual(ex1(0.001), 0.35802469135802484)

    def test_eps2(self):
        self.assertEqual(ex1(0.0001), 0.3413654618473896)


if __name__ == '__main__':
    unittest.main()
