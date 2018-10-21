# lab №1 ex. 5(test) | Var 9 Sergey Zubrilin 9/24/18


from lab_1.ex5 import MyFloat
import unittest


class TestEx5(unittest.TestCase):

    def test_sub(self):
        """проверка операции вычитания, и сохранения атрибутов после операции"""

        fl = MyFloat('-', 12345, 17)
        fl1 = MyFloat('', 54321, 17)
        fl2 = MyFloat('-', 12345, 5)
        fl3 = MyFloat('-', 765432, 45)

        res1 = fl - fl1
        res2 = fl2 - fl
        res3 = fl3 - fl1

        # тут я пересчитал на калькуляторе
        self.assertEqual(str(res1), '-0.66666E+17')
        self.assertEqual(str(res2), '0.12345E+17')
        self.assertEqual(str(res3), '-0.765432E+45')

        self.assertEqual(res1.mantissa, 66666)
        self.assertEqual(res1.exponent, 17)
        self.assertEqual(res1.sign, '-')

    def test_ne(self):
        """проверка операции 'не равен'"""

        fl = MyFloat('-', 12345, 17)
        fl1 = MyFloat('-', 12345, 17)
        fl2 = MyFloat('-', 0, 15)

        self.assertFalse(fl != fl1)
        self.assertTrue(fl != fl2)

    def test_ge(self):
        """проверка операции 'больше или равно'"""

        fl = MyFloat('-', 12345, 17)
        fl1 = MyFloat('-', 12345, 19)
        fl2 = MyFloat('-', 0, 15)
        fl3 = MyFloat('-', 0, 15)

        self.assertFalse(fl >= fl1)
        self.assertTrue(fl >= fl2)
        self.assertTrue(fl3 >= fl2)

    def test_gt(self):
        """проверка операции 'больше'"""

        fl = MyFloat('-', 12345, 17)
        fl1 = MyFloat('-', 12345, 19)
        fl2 = MyFloat('-', 0, 15)
        fl3 = MyFloat('-', 0, 15)

        self.assertFalse(fl > fl1)
        self.assertTrue(fl > fl2)
        self.assertFalse(fl3 > fl2)


if __name__ == '__main__':
    unittest.main()
