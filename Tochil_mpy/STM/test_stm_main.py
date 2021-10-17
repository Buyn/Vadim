# ----------------------------------------------
# * import block# :
import unittest
import sys
from unittest.mock import MagicMock, patch

sys.modules['micropython'] = MagicMock()
from stm_main import *

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
# ** def test_mainloop(self): : 
# ----------------------------------------------
    def test_mainloop(self):
        mainloop(test = True)


# ----------------------------------------------
# ** def test_cmd_rutine(self): : 
# ----------------------------------------------
    def test_cmd_rutine(self):
        self.assertTrue(DEV_STEPMOTOR01 in DEV_SMS)
        self.assertFalse(1 in DEV_SMS)
        rpi.get_msg()
        msg = rpi.rutin()
        print(msg)
        print(msg[2])
        msg = bytes(b'\x0A\x0A\x00\x0f')
        print(msg)
        cmd_rutin(msg)
        msg = bytes(b'\x0B\x64\x00\x0f')
        print(msg)
        cmd_rutin(msg)


# ----------------------------------------------
# ** def test_step_motor_rutine (self): : 
# ----------------------------------------------
    def test_step_motor_rutine (self):
        step_motor_rutine(sm = sms[1], cmd = CMD_STEPS, data = [0, 100] )
        # step_motor_rutine(sm = sms[1], cmd = CMD_HOMERUN, data = [0, 100] )


# ----------------------------------------------
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
    suite.addTest(Test_Fun('test_mainloop'))
    suite.addTest(Test_Fun('test_cmd_rutine'))
    suite.addTest(Test_Fun('test_step_motor_rutine'))
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
