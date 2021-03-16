import unittest
from PyQt5 import QtCore,QtGui,QtWidgets
from main import *
#Test cases to test Calulator methods
#You always create  a child class derived from unittest.TestCase
class TestCalculator(unittest.TestCase):
  #setUp method is overridden from the parent class TestCase
  def setUp(self):
    import sys
    self.app = QtWidgets.QApplication(sys.argv)
    self.w = MWidget()
  #Each test method starts with the keyword test_
  def test_1(self):
    self.assertEqual(10, 11)
  def test_2(self):
    self.assertEqual(4, 5)
  def test_3(self):
    self.assertEqual(20, 21)
  def test_4(self):
    self.assertEqual(5, 5)
# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()