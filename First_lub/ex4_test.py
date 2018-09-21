# lab №1 ex. 4(test) | Var 9 Sergey Zubrilin 9/21/18


from First_lub.ex4 import text_analysis, update_output_log
import unittest


class TestEx4(unittest.TestCase):
    def setUp(self):
        with open('test_logs/output_log_test.txt', 'w') as file:
            file.write('')
        with open('test_logs/log_for_test.txt', 'w') as file:
            file.write('aaaaavvvvv')

    def test_text_analysis(self):
        """Анализ текста во входном файле, должен возврашать словарь, вида {'символ':'частота символа в процентах'}"""

        self.assertEqual(text_analysis(file='test_logs/log_for_test.txt'), {'a': '50.0%', 'v': '50.0%'})

    def test_update_output_log(self):
        """Проверка записи аналиированных данных в output log file"""

        dic = text_analysis(file='test_logs/log_for_test.txt')
        update_output_log(dic, 'test_logs/output_log_test.txt')

        with open('test_logs/output_log_test.txt', 'r') as file:
            first_symbol = file.readline()
            second_symbol = file.readline()

        self.assertEqual(first_symbol, 'a --> 50.0% |\n')
        self.assertEqual(second_symbol, 'v --> 50.0% |\n')


if __name__ == '__main__':
    unittest.main()
