import math
import unittest


def error_check(frac1, frac2):
    if not isinstance(frac1, list) or not isinstance(frac2, list):
        raise TypeError("Provided arguments must be lists.")
    if not len(frac1) == 2 or not len(frac2) == 2:
        raise ValueError("Argument lists must be length of 2.")
    if not isinstance(frac1[0], int) or not isinstance(frac1[1], int) or not isinstance(frac2[0], int) or not isinstance(
            frac2[1], int):
        raise ValueError("Elements of lists must be integers.")
    if frac1[1] == 0 or frac2[1] == 0:
        raise ValueError("Denominator value cannot equal 0.")


def error_check2(frac1):
    if not isinstance(frac1, list):
        raise TypeError("Provided argument must be list.")
    if not len(frac1) == 2:
        raise ValueError("Argument list must be length of 2.")
    if not (isinstance(frac1[0], int) and isinstance(frac1[1], int)):
        raise ValueError("Elements of list must be integers.")
    if frac1[1] == 0:
        raise ValueError("Denominator value cannot equal 0.")


def minus_unification(frac):
    if frac[0] < 0 and frac[1] < 0:
        frac[0] = abs(frac[0])
        frac[1] = abs(frac[1])
    if frac[0] > 0 > frac[1]:
        frac[1] = abs(frac[1])
        frac[0] = -frac[0]
    return frac


def add_frac(frac1, frac2):
    error_check(frac1, frac2)
    gcd = math.gcd(frac1[1], frac2[1])
    common_den = frac1[0] * frac2[0] // gcd
    frac3 = [frac1[0] * (common_den // frac1[1]) + frac2[0] * (common_den // frac2[1]), common_den]
    frac3 = minus_unification(frac3)
    return frac3


def sub_frac(frac1, frac2):
    error_check(frac1, frac2)
    gcd = math.gcd(frac1[1], frac2[1])
    common_den = frac1[0] * frac2[0] // gcd
    frac3 = [frac1[0] * common_den // frac1[1] - frac2[0] * common_den // frac2[1], common_den]
    frac3 = minus_unification(frac3)
    return frac3


def mul_frac(frac1, frac2):
    error_check(frac1, frac2)
    frac3 = [frac1[0] * frac2[0], frac1[1] * frac2[1]]
    frac3 = minus_unification(frac3)
    return frac3


def div_frac(frac1, frac2):
    error_check(frac1, frac2)
    if is_zero(frac2):
        raise ValueError("Division by 0 is forbidden.")
    frac3 = [frac1[0] * frac2[1], frac1[1] * frac2[0]]
    frac3 = minus_unification(frac3)
    return frac3


def is_positive(frac):
    error_check2(frac)
    if frac[0] == 0 or (frac[0] > 0 and frac[1] > 0):
        return True
    else:
        return False


def is_zero(frac):
    error_check2(frac)
    if frac[0] == 0:
        return True
    else:
        return False


def cmp_frac(frac1, frac2):
    error_check(frac1, frac2)
    frac1 = minus_unification(frac1)
    frac2 = minus_unification(frac2)
    number1 = frac1[0] * frac2[1]
    number2 = frac1[1] * frac2[0]
    if number1 < number2:
        return -1
    elif number1 == number2:
        return 0
    else:
        return 1


def frac2float(frac):
    error_check2(frac)
    return float(frac[0] / frac[1])


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
        self.not_a_list = "string"
        self.wrong_argument_numbers = [3, 2, 5]
        self.not_integers = ["eve", "ola"]
        self.zero_denominator = [5, 0]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([-8, 4], [2, -5]), [-12, 5])

    def test_sub_frac(self): pass

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 5], [3, 2]), [3, 10])
        self.assertEqual(mul_frac([-1, 4], [-3, 4]), [3, 16])
        self.assertEqual(mul_frac([-1, 3], [3, -4]), [3, 12])
        self.assertEqual(mul_frac([5, 12], [3, -1]), [-15, 12])
        self.assertRaises(TypeError, mul_frac, self.not_a_list, self.not_a_list )
        self.assertRaises(ValueError, mul_frac, self.wrong_argument_numbers, self.wrong_argument_numbers)
        self.assertRaises(ValueError, mul_frac, self.not_integers, self.not_integers)
        self.assertRaises(ValueError, mul_frac, self.zero_denominator, self.zero_denominator)

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 5], [3, 2]), [2, 15])
        self.assertEqual(div_frac([-1, 4], [-3, 4]), [4, 12])
        self.assertEqual(div_frac([-1, 3], [3, -4]), [4, 9])
        self.assertEqual(div_frac([5, 12], [3, -1]), [-5, 36])
        self.assertRaises(TypeError, div_frac, self.not_a_list, self.not_a_list)
        self.assertRaises(ValueError, div_frac, self.wrong_argument_numbers, self.wrong_argument_numbers)
        self.assertRaises(ValueError, div_frac, self.not_integers, self.not_integers)
        self.assertRaises(ValueError, div_frac, self.zero_denominator, self.zero_denominator)
        self.assertRaises(ValueError, div_frac, [3, 4], self.zero)

    def test_is_positive(self): pass

    def test_is_zero(self): pass

    def test_cmp_frac(self): pass

    def test_frac2float(self): pass

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
