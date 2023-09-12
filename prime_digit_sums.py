import unittest
from math import sqrt
import sys

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


def is_composite_prime(n):
    digits = str(n)
    for i in range(len(digits) - 2):
        number = int(digits[i]) + int(digits[i + 1]) + int(digits[i + 2])
        if number in primes:
            if i < len(digits) - 3:
                number += int(digits[i + 3])
                if number in primes:
                    if i < len(digits) - 4:
                        number += int(digits[i + 4])
                        if number not in primes:
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
        self.assertEqual(primeDigitSums(3691), 303)


if __name__ == "__main__":
    unittest.main()
