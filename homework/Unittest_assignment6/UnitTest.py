import unittest
from BalancedAB import balancedAB

class TestStringMethod(unittest.TestCase):

  def test0(self):
    self.assertEqual(balancedAB('AABB'), True)

  def test1(self):
    self.assertEqual(balancedAB('AAZZBB'), True)   
  
  def test2(self):
    self.assertEqual(balancedAB('AAAXXXXXYB'), True)

  def test3(self):
    self.assertEqual(balancedAB(''), True)
  
  def test4(self):
    self.assertEqual(balancedAB('XXXXXXXYYYYZZZZB'), True)

  def test5(self):
    self.assertEqual(balancedAB('XXXXXXXYYYYZZZZB'), True)

  def test6(self):
    self.assertEqual(balancedAB('AAAXXXXXYB'), True)

  def test7(self):
    self.assertEqual(balancedAB('AAAXXXXXYB'), True)


if __name__ == '__main__':
  unittest.main()