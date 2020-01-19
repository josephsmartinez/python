# from unittest import TestCase
# from calculator import Calculator
# from unittest.mock import patch

# # class TestCalcultor(TestCase):
# #   def setUp(self):
# #     self.calc = Calculator()

# #   def test_sum(self):
# #     answer = self.calc.sum(2, 4)
# #     self.assertEqual(answer, 6)

# class TestCalcultor(TestCase):
#   @patch('Calculator.sum', return_value=9)
#   def test_sum(self, sum):
#     self.assertEqual(sum(2,3), 9)