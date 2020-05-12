import unittest #importing the unittest framework

from fizzbuzz import fizzbuzz # calling the fizzbuzz function from the fizzbuzz script

class FizzBuzzTest(unittest.TestCase):
    def test_returns_int_if_1(self):
        self.assertEqual(fizzbuzz(1), "1")

    def test_returns_fizz_if_3(self):
        self.assertEqual(fizzbuzz(3), "Fizz")

    def test_returns_buzz_if_5(self):
        self.assertEqual(fizzbuzz(5), "Buzz")

    def test_returns_boop_if_7(self):
        self.assertEqual(fizzbuzz(7), "Boop")

    def test_returns_fizzbuzz_if_15(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")

    def test_returns_fizzboop_if_21(self):
        self.assertEqual(fizzbuzz(21), "FizzBoop")

    def test_return_buzzboop_if_35(self):
        self.assertEqual(fizzbuzz(35), "BuzzBoop")

    def test_returns_int_53(self):
        self.assertEqual(fizzbuzz(53), "53")

    def test_returns_fizzbuzzboop_if_105(self):
        self.assertEqual(fizzbuzz(105), "FizzBuzzBoop")

if __name__ == "__main__":
    unittest.main()
