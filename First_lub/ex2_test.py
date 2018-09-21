# lab №1 ex. 2(test) | Var 9 Sergey Zubrilin 9/21/18


from First_lub.ex2 import first_odd, is_prime, ex2
import unittest


class TestEx2(unittest.TestCase):

    def test_first_odd(self):
        """ Найдите первую с конца нечётную цифру числа. «Зачеркните» все цифры, следующие за найденной."""

        self.assertEqual(first_odd(12345672), 1234567)
        self.assertEqual(first_odd(124), None)

    def test_is_prime(self):
        """Верно ли, что оставшееся число – простое?"""

        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(15))
        with self.assertRaises(AttributeError):
            is_prime(None)

    def test_ex2(self):
        """Суммарная проверка скрипта"""

        self.assertTrue(ex2())
        self.assertFalse(ex2(3339))


if __name__ == '__main__':
    unittest.main()
