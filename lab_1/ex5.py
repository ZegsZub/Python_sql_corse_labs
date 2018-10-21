# lab №1 ex. 5 | Var 9 (b) Sergey Zubrilin 9/20/18


from lab_1.tools import sign_init


class MyFloat:
    def __init__(self, sign='', mantissa=1, exponent=1):
        if sign != '' and sign != '-':
                raise AttributeError("wrong format data, attr 'sign'")
        if not isinstance(mantissa, int):
            raise AttributeError("wrong format data, attr 'mantissa'")
        if not isinstance(exponent, int):
            raise AttributeError("wrong format data, attr 'mantissa'")

        self.sign = sign
        self.mantissa = mantissa
        self.exponent = exponent

    def __repr__(self):
        if self.mantissa == '0':
            return f'{self.sign}0.0'
        return f'{self.sign}0.{self.mantissa}E+{self.exponent}'

    def __gt__(self, other):
        if sign_init(self.sign) > sign_init(other.sign):
            return True
        if self.exponent > other.exponent:
            return True
        if self.mantissa > other.mantissa:
            return True
        return False

    def __ge__(self, other):
        if sign_init(self.sign) > sign_init(other.sign):
            return True
        if self.exponent > other.exponent:
            return True
        if self.mantissa > other.mantissa:
            return True
        if (self.mantissa == other.mantissa) and (self.exponent == other.exponent)\
                                            and (sign_init(self.sign) == sign_init(other.sign)):
            return True
        return False

    def __ne__(self, other):
        if (self.mantissa != other.mantissa) or (self.exponent != other.exponent)\
                                            or (sign_init(self.sign) != sign_init(other.sign)):
            return True
        return False

    @staticmethod
    def to_int(my_float):
        return sign_init(my_float.sign)*my_float.mantissa*(10**(my_float.exponent-len(str(my_float.mantissa))))

    @staticmethod
    def my_round(number, ndigits):

        s = str(number)
        sign = 1
        if '-' in s:
            s = s.replace('-', '')
            sign = -1

        if len(s) > ndigits:

            for i in range(ndigits, len(s)):
                if int(s[i]) >= 4:
                    if int(s[i]) >= 5:
                        return f'{(int(s[:ndigits])+1) * sign}'+'0'*(len(s)-ndigits)
                    else:
                        continue
                else:
                    return f'{int(s[:ndigits])* sign}'+'0'*(len(s)-ndigits)

        return str(number)

    def __sub__(self, other):
        res_exponent = 0
        res_sign = ''
        int_value = int(self.my_round(self.to_int(self) - self.to_int(other),
                                  max(len(str(self.mantissa)), len(str(other.mantissa)))))
        str_value = str(int_value)

        if int_value < 0:
            res_sign = '-'

        for i in range(str_value.count('0')):
            if str_value[-(i+1)] == '0':
                res_exponent += 1
            else:
                break

        res_mantissa = int(str_value[:len(str_value)-res_exponent].replace('-', ''))
        res_exponent += len(str(res_mantissa))
        return MyFloat(res_sign, res_mantissa, res_exponent)


