# ----------------------------------------------
# * import block * # :
# ----------------------------------------------
import unittest
import sys
# from unittest.mock import MagicMock, patch
# sys.modules['micropython'] = MagicMock()
from bitman import *


# ----------------------------------------------
# * class Test_Init * # : 
# ** class :
# ----------------------------------------------:
class Test_Init(unittest.TestCase):


# ----------------------------------------------:
# ** def test_init1 : 
# ----------------------------------------------:
    def test_init1(self):# {{{
      pass
      test = Bitman(8) 
      self.assertEqual(len(test), 8)
      self.assertEqual(test(), 0)
      self.assertFalse(test[0])
      test[0] = 1
      self.assertTrue(test[0])
      self.assertEqual(test(), 1)
      self.assertFalse(test[1])
      test[1] = True
      self.assertTrue(test[1])
      self.assertEqual( test(), 3)
      test[0] = False
      self.assertFalse(test[0])
      self.assertEqual( test(), 2)
      test[1] = False
      self.assertFalse(test[7])
      test[7] = True
      self.assertTrue(test[7])
      test2 = test
      self.assertEqual( test2(), 128)
      self.assertFalse(test2[0])
      test2[0] = True
      self.assertTrue(test2[0])
      self.assertEqual( test2(), 129)
      self.assertEqual( test(), 129)
      # mw = None
      # self.assertIsNone( mw)
      # mw = Port_drv_rpi( i2c_device(13, 1))
      # self.assertIsNotNone( mw)
      # self.assertIsNotNone( mw._i2c)
      # self.assertEqual( mw.pin, 'PC13')

            				
# ----------------------------------------------
# ** ------------------------------------ ** # :


# * class Test_Fun(unittest.TestCase) * # : 
# ** class ----------------------------------------:
class Test_Fun(unittest.TestCase):


# ----------------------------------------------
# ** @classmethod #setUpClass#  : 
# ----------------------------------------------
    @classmethod #setUpClass# {{{
    def setUpClass(self):
        print("*"*33,"*"*33)
        self.test = Bitman(8)
        # print("*"*33,"*"*33)
        
        
# ----------------------------------------------
# ** @classmethod #tearDownClass# : 
# ----------------------------------------------
    @classmethod #tearDownClass# {{{
    def tearDownClass(self):
        print("*"*33,"*"*33)
        print("tear down module")
        self.test = None
        print("*"*33,"*"*33)


# ----------------------------------------------
# ** ------------------------------------ ** # :


# ----------------------------------------------
# ** def test_bits(self): : 
# ----------------------------------------------
    def test_bits(self):
        self.assertEqual( self.test._valueA, 0)
        # self.test.biton(self.test._valueA, 0)
        self.assertTrue( self.test.getbit(self.test._value, 1))
        # print(self.test._valueA)
        # self.test._valueA = self.test.setbit(self.test._valueA, 1, 1)
        # self.assertFalse( self.test.getbit(self.test._valueA, 1))


# ----------------------------------------------
# * suite_Init(self) : 
# ----------------------------------------------
def suite_Init():
    suite = unittest.TestSuite()
    suite.addTest(Test_Init('test_init1'))
    # suite.addTest(Test_Fun('test_set'))
    # suite.addTest(Test_Fun('test_bits'))
    return suite
		

# ----------------------------------------------
# * Test runer : 
# ----------------------------------------------
# (compile " D:/Development/version-control/GitHub/Vadim/Tochil/main_test.py -k init")
# (compile " python -m unittest D:/Development/version-control/GitHub/Vadim/Tochil/main_test.py ")
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    runner = unittest.TextTestRunner()
    runner.run(suite_Init())
    # unittest.main()


# -------------------------------------------- #
# * ------------------------------------------ :
