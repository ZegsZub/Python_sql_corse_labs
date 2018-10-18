# lab №1 ex. 5(test) | Var 9 Sergey Zubrilin 9/24/18


from lab_1.ex5 import MyFloat
import unittest


class TestEx5(unittest.TestCase):

    def test_convert_to_float(self):
        """Проверка корректности конвертации"""

        fl = MyFloat('-', 12345, 17)
        fl1 = MyFloat('', 54321, 17)
        fl2 = MyFloat('-', 12345, 5)
        fl3 = MyFloat('-', 0, 15)

        self.assertEqual(str(fl.convert_to_float()), '-1.2345e+16')
        self.assertEqual(str(fl1.convert_to_float()), '5.4321e+16')
        self.assertEqual(str(fl2.convert_to_float()), '-12345.0')
        self.assertEqual(str(fl3.convert_to_float()), '-0.0')

    def test_convert_from_float(self):
        """Проверка корректности конвертации"""

        fl = MyFloat('-', 12345, 17)
        fl1 = MyFloat('', 54321, 17)
        fl2 = MyFloat('-', 12345, 5)
        fl3 = MyFloat('-', 0, 15)

        self.assertEqual(str(fl.convert_from_float(fl.convert_to_float())), '-0.12345E+17')
        self.assertEqual(str(fl.convert_from_float(fl1.convert_to_float())), '0.54321E+17')
        self.assertEqual(str(fl.convert_from_float(fl2.convert_to_float())), '-0.12345E+5')
        self.assertEqual(str(fl.convert_from_float(fl3.convert_to_float())), '-0.0')

    def test_sub(self):
        """проверка операции вычитания, и сохранения атрибутов после операции"""

        fl = MyFloat('-', 12345, 17)
        fl1 = MyFloat('', 54321, 17)
        fl2 = MyFloat('-', 12345, 5)
        fl3 = MyFloat('-', 0, 15)

        res1 = fl - fl1
        res2 = fl2 - fl
        res3 = fl3 - fl1

        self.assertEqual(str(res1), '-0.66666E+17')
        self.assertEqual(str(res2), '0.12344999999987656E+17')
        self.assertEqual(str(res3), '-0.54321E+17')

        self.assertEqual(res1.mantissa, '66666')
        self.assertEqual(res1.exponent, 17)
        self.assertEqual(res1.sign, '-')

    def test_ne(self):
        """проверка операции 'не равен'"""

        fl = MyFloat('-', 12345, 17)
        fl1 = MyFloat('-', 12345, 17)
        fl2 = MyFloat('-', 0, 15)

        self.assertFalse(fl != fl1)
        self.assertTrue(fl != fl2)


if __name__ == '__main__':
    unittest.main()
