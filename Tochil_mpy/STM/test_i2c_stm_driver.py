# ----------------------------------------------
# * import block# :
import unittest
import sys
from unittest.mock import MagicMock, patch

sys.modules['micropython'] = MagicMock()
from i2c_stm_driver import *

# ----------------------------------------------
# * class Test_Init : 
# ** ----------------------------------------------:
class Test_Init(unittest.TestCase):


    @patch('micropython.alloc_emergency_exception_buf')
    def test_load_image(self, imread):
        print('alloc_emergency_exception_buf=', imread)
        assert imread.called

# ** def test_init1 : 
    def test_init1(self):# {{{
        mw = None
        self.assertIsNone( mw)
        mw = I2C_com()
        # temp_A = 11
        # temp_B = 14
        self.assertIsNotNone( mw)
        self.assertIsNotNone( mw.i2c)
        self.assertIsNotNone( mw.pinOut01)
        # self.assertEqual( mw.pin, 'PC13')
        # self.assertEqual( mw.temp_B, 14)

            				
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
        self.sd = I2C_com()
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
# ** def test_print_in(self):
    def test_print_in(self):
        self.sd.print_in()

# ** def test_diode_com(self):
    def test_diode_com(self):
        self.sd.diode_com()

# ** def test_i2c_exec(self):
    def test_i2c_exec(self ):
        self.assertEqual( self.sd.pinOut01.PIN_VALUE, True )
        self.sd.i2c_exec( b'\x13')
        self.assertEqual( self.sd.pinOut01.PIN_VALUE, False )
        self.sd.i2c_exec( b'\x10')
        self.assertEqual( self.sd.pinOut01.PIN_VALUE, True )
        self.sd.i2c_exec( b'\x13')
        self.assertEqual( self.sd.pinOut01.PIN_VALUE, False )
        # self.assertEqual( result, ' New!\n test\n test!\n ')


# ** def test_i2c_2s_send(self):
    def test_i2c_2s_send(self):
        # self.assertEqual( self.sd.pinOut01.PIN_VALUE, True )
        self.sd.i2c_2s_send( )
        # self.assertEqual( self.sd.pinOut01.PIN_VALUE, False )
        # self.sd.i2c_exec( 10)
        # self.assertEqual( self.sd.pinOut01.PIN_VALUE, True )
        # self.sd.i2c_exec( 13)
        # self.assertEqual( self.sd.pinOut01.PIN_VALUE, False )



# ** ----------------------------------------------:
# * def suite Init(): : 
def suite_Init():
    suite = unittest.TestSuite()
    suite.addTest(Test_Init('test_init1'))
    suite.addTest(Test_Fun('test_i2c_exec'))
    # infiniti loop
    # suite.addTest(Test_Fun('test_i2c_2s_send'))
    # suite.addTest(Test_Fun('test_print_in'))
    # suite.addTest(Test_Fun('test_diode_com'))
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
