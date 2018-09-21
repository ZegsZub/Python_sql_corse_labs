# lab №1 ex. 5 | Var 9 (b) Sergey Zubrilin 9/20/18


from tools import sign_init


class DigitByFloat:
    def __init__(self, sign='', mantissa=1, exponent=1):
        if sign != '' and sign != '-':
            raise AttributeError("wrong format data, attr 'sign'")
        if not isinstance(mantissa, int):
            raise AttributeError("wrong format data, attr 'mantissa'")
        if not isinstance(exponent, int):
            raise AttributeError("wrong format data, attr 'mantissa'")

        self.sign = sign
        self.mantissa = str(mantissa)

        if self.mantissa[0] != '0':
            self.exponent = exponent
        else:
            self.exponent = 0

        while self.mantissa[-1] == '0' and len(self.mantissa) > 1:
            self.mantissa = self.mantissa[:-1]
            self.exponent += 1

    def convert_to_float(self):
        sign = sign_init(self.sign)
        return float(self.mantissa)*(10 ** int(self.exponent - len(self.mantissa)))*sign

    # @classmethod
    # def convert_from_float(cls, fl):
    #     str_fl = str(fl)
    #     sign = ''
    #     exponent = 1
    #
    #     if str_fl[0] == '-':
    #         sign = '-'
    #         str_fl = str_fl[1:]
    #
    #     if '+' in str_fl:
    #         exponent = int(str_fl[str_fl.find('+') + 1:])
    #         mantissa = int(str_fl[:str_fl.find('+')-1].replace('.', ''))
    #     else:
    #         mantissa = int(str_fl.replace('.', ''))
    #
    #     return cls(sign, mantissa, exponent)

    def __str__(self):
        if self.mantissa == '0':
            return f'{self.sign}0.0'
        return f'{self.sign}0.{self.mantissa}E+{self.exponent}'

    def __gt__(self, other):
        sign1 = sign_init(self.sign)
        sign2 = sign_init(other.sign)

        if sign1 > sign2:
            return True

        if sign1 == sign2 == 1:
            if self.exponent > other.exponent:
                return True
            if self.mantissa > other.mantissa:
                return True

        if sign1 == sign2 == -1:
            if self.exponent < other.exponent:
                return True
            if self.mantissa < other.mantissa:
                return True

        return False

    def __ge__(self, other):
        sign1 = sign_init(self.sign)
        sign2 = sign_init(other.sign)

        if sign1 > sign2:
            return True

        if sign1 == sign2 == 1:
            if self.exponent >= other.exponent:
                return True
            if self.mantissa >= other.mantissa:
                return True

        if sign1 == sign2 == -1:
            if self.exponent <= other.exponent:
                return True
            if self.mantissa <= other.mantissa:
                return True

        return False

    def __sub__(self, other):
        fl1 = self.convert_to_float()
        fl2 = other.convert_to_float()
        fl = fl1 - fl2
        # res = self.convert_from_float(fl)

        # print(f'{fl} - test 1 with out convert')
        return fl


fl1 = DigitByFloat(sign='-', mantissa=12341, exponent=17)
fl2 = DigitByFloat(sign='-', mantissa=123, exponent=17)
print(fl1)
# print(fl1.convert_to_float())

print(fl2)

fl3 = fl1 - fl2
print(fl3)

