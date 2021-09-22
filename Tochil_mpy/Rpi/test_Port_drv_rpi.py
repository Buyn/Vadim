# ----------------------------------------------
# * import block :
import unittest
import sys
from unittest.mock import MagicMock, patch

sys.modules['micropython'] = MagicMock()
from Port_drv_rpi import *

# ----------------------------------------------
# * class Test_Init : 
# ** ----------------------------------------------:
class Test_Init(unittest.TestCase):


    # @patch('micropython.alloc_emergency_exception_buf')
    # def test_load_image(self, imread):
    #     print('alloc_emergency_exception_buf=', imread)
    #     assert imread.called

# ** def test_init1 : 
    def test_init1(self):# {{{
        mw = None
        self.assertIsNone( mw)
        mw = Port_drv_rpi( i2c_device(13, 1))
        self.assertIsNotNone( mw)
        self.assertIsNotNone( mw._i2c)
        self.assertEqual( mw._valueA, bytearray(8))
        self.assertEqual( mw._valueB, bytearray(8))
        # self.assertEqual( mw.pin, 'PC13')

            				
# ----------------------------------------------
# ** ----------------------------------------------:
# * class Test_Fun(unittest.TestCase): : 
# ** ----------------------------------------------:
class Test_Fun(unittest.TestCase):
    @patch('micropython.alloc_emergency_exception_buf')
    def test_load_image(self, imread):
        print('alloc_emergency_exception_buf=', imread)
        assert imread.called

# ** @classmethod #setUpClass#  : 
    @classmethod #setUpClass# {{{
    def setUpClass(self):
        print("*"*33,"*"*33)
        self.test = Port_drv_rpi( i2c_device(13, 1))
        # self.mw = Main_Windows()
        #     print ("file opened")
        # print("*"*33,"*"*33)
        
        
# ----------------------------------------------
# ** @classmethod #tearDownClass# : 
    @classmethod #tearDownClass# {{{
    def tearDownClass(self):
        print("*"*33,"*"*33)
        print("tear down module")
        self.sd = None
        print("*"*33,"*"*33)

# ----------------------------------------------
# ** def test_set(self): : 
    def test_set(self):
        self.assertFalse( self.test._valueA[0])
        self.test.set(A1, True)
        self.assertEqual( self.test._valueA[1], 1)
        self.assertEqual(
              int.from_bytes(self.test._valueA,
                             byteorder='big', signed=False), 1)
        self.assertEqual( self.test._valueB[0], 0)
        self.test.set(B5, True)
        # print(self.test._valueA)
        # print(self.test._valueB)
        self.assertEqual( self.test._valueB[4], 1)


# ** def test_value(self): : 
    def test_value(self):
        self.test.set(A1, 0)
        self.test.set(B1, 0)
        # print(self.test._valueA)
        # print(self.test._valueB)
        self.assertFalse(self.test.value(A1))
        self.test.set(A1, 1)
        self.assertTrue(self.test.value(A1))
        self.assertFalse(self.test.value(B1))
        self.test.set(B1, True)
        self.assertTrue(self.test.value(B1))
        # self.assertEqual( self.test._valueA[0], 1)
        # self.assertEqual( self.test._valueB[0], 0)
        # print(self.test._valueA)
        # print(self.test._valueB)
        # self.assertEqual( self.test._valueB[4], 1)


# ** ----------------------------------------------:
# * def suite Init(): : 
def suite_Init():
    suite = unittest.TestSuite()
    suite.addTest(Test_Init('test_init1'))
    suite.addTest(Test_Fun('test_set'))
    suite.addTest(Test_Fun('test_value'))
    # suite.addTest(Test_Fun('test_Sharp_cheng'))
    # suite.addTest(WidgetTestCase('test_widget_resize'))
    # tests whith infinit loop
    # suite.addTest(Test_Fun('test_send_2_simbol'))
    # end of tests whith infinit loop
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
# * ----------------------------------------------:
