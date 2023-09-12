import sys
import unittest
from math import sqrt

sys.set_int_max_str_digits(0)


# https://www.hackerrank.com/challenges/prime-digit-sums/problem


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


primes = set()
for i in range(1, 50):
    if is_prime(i):
        primes.add(i)

three_digits = set()
for i in range(1, 1000):
    digits = str(i)
    while len(digits) < 3:
        digits = "0" + digits
    number = int(digits[0]) + int(digits[1]) + int(digits[2])
    if number in primes:
        three_digits.add(digits)

four_digits = set()
for i in range(1, 10000):
    digits = str(i)
    while len(digits) < 4:
        digits = "0" + digits
    number = int(digits[0]) + int(digits[1]) + int(digits[2]) + int(digits[3])
    if number in primes:
        four_digits.add(digits)


five_digits = set()
for i in range(1, 100000):
    digits = str(i)
    while len(digits) < 5:
        digits = "0" + digits
    number = (
        int(digits[0])
        + int(digits[1])
        + int(digits[2])
        + int(digits[3])
        + int(digits[4])
    )
    if number in primes:
        five_digits.add(digits)


def is_composite_prime(n):
    digits = str(n)
    for i in range(len(digits) - 2):
        number = digits[i] + digits[i + 1] + digits[i + 2]
        if number in three_digits:
            if i < len(digits) - 3:
                number += digits[i + 3]
                if number in four_digits:
                    if i < len(digits) - 4:
                        number += digits[i + 4]
                        if number not in five_digits:
                            return False
                else:
                    return False
        else:
            return False
    return True


def primeDigitSums(n):
    mod = 10**9 + 7
    result = 0
    for number in range(10 ** (n - 1), 10**n):
        if is_composite_prime(number):
            result += 1

    return result % mod


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(primeDigitSums(6), 95)

    def test_b(self):
        self.assertEqual(is_prime(6), False)
        self.assertEqual(is_prime(7), True)
        self.assertEqual(is_prime(53982894593057), True)
        self.assertEqual(is_prime(28871271685163), True)

    def test_c(self):
        self.assertEqual(primeDigitSums(3), 303)

    def test_d(self):
        self.assertEqual(primeDigitSums(8), 295)


if __name__ == "__main__":
    unittest.main()
