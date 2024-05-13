import unittest
from main import fibonacci, salute, isDuck

class TestFibonacci(unittest.TestCase):
  def test_fibonnaci_with_negative_value(self):
    with self.assertRaises(ValueError):
      fibonacci(-1)

  def test_fibonnaci_with_zero(self):
    self.assertEqual(fibonacci(0), 0)

  def test_fibonnaci_with_one(self):
    self.assertEqual(fibonacci(1), 1)

  def test_fibonnaci_with_three(self):
    self.assertEqual(fibonacci(3), 2)

  def test_fibonacci_with_thousand(self):
    self.assertEqual(fibonacci(10), 55)

class TestSalute(unittest.TestCase):
  def test_salute_with_empty_name(self):
    with self.assertRaises(ValueError):
      salute(10, "")
  
  def test_salute_with_none_name(self):
    with self.assertRaises(ValueError):
      salute(10, None)

  # def test_salute_with_negative_hour(self):
  #   with self.assertRaises(ValueError):
  #     salute(-1, "John")

  # def test_salute_with_hour_greater_than_24(self):
  #   with self.assertRaises(ValueError):
  #     salute(25, "John")

  def test_salute_with_hour_10(self):
    self.assertEqual(salute(10, "John"), "Good Morning, John!")

  def test_salute_with_hour_15(self):
    self.assertEqual(salute(15, "John"), "Good Afternoon, John!")
  
  def test_salute_with_hour_20(self):
    self.assertEqual(salute(20, "John"), "Good Night, John!")

class TestIsDuck(unittest.TestCase):
  def test_is_duck(self):
    self.assertEqual(isDuck(True, True, True, True), 'is a duck')

  def test_is_goose(self):
    self.assertEqual(isDuck(False, True, True, False), 'probably a goose')

  def test_is_steve(self):
    self.assertEqual(isDuck(False, False, True, True), 'Steve, for sure')

  def test_have_no_idea(self):
    self.assertEqual(isDuck(False, False, False, False), 'Have no idea')


if __name__ == "__main__":
  unittest.main()