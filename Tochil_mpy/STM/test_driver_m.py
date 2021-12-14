# ----------------------------------------------
# * import block# :
import unittest
import sys
from unittest.mock import MagicMock, patch

sys.modules['micropython'] = MagicMock()
from driver_m import *

# ----------------------------------------------
# * class Test_Init : 
# ** ----------------------------------------------:
class Test_Init(unittest.TestCase):


    # @patch('micropython.alloc_emergency_exception_buf')
    # def test_load_image(self, imread):
    #     print('alloc_emergency_exception_buf=', imread)
    #     assert imread.called


#  ----------------------------------------------:
# ** def test_init1 : 
#  ----------------------------------------------:
    def test_init1(self):# {{{
        mw = None
        self.assertIsNone( mw)
        mw = Step_Driver(pyb.Pin.cpu.C13, pyb.Pin.cpu.C14)
        # temp_A = 11
        # temp_B = 14
        self.assertIsNotNone( mw)
        self.assertIsNotNone( mw.pin)
        # self.assertEqual( mw.pin, 'PC13')
        # self.assertEqual( mw.temp_B, 14)

            				
# ----------------------------------------------
# ** ----------------------------------------------:
# * class Test_Fun(unittest.TestCase): : 
# ** ----------------------------------------------:
class Test_Fun(unittest.TestCase):
    # @patch('micropython.alloc_emergency_exception_buf')
    # def test_load_image(self, imread):
    #     print('alloc_emergency_exception_buf=', imread)
    #     assert imread.called


# ** @classmethod #setUpClass#  : 
    @classmethod #setUpClass# {{{
#  ----------------------------------------------:
    def setUpClass(self):
        print("*"*33,"*"*33)
        self.sd = Step_Driver(pyb.Pin.cpu.C13, pyb.Pin.cpu.C14)
        # self.mw = Main_Windows()
        #     print ("file opened")
        # print("*"*33,"*"*33)
        
        
# ----------------------------------------------
# ** @classmethod #tearDownClass# : 
#  ----------------------------------------------:
    @classmethod #tearDownClass# {{{
    def tearDownClass(self):
        print("*"*33,"*"*33)
        print("tear down module")
        self.sd = None
        print("*"*33,"*"*33)


# ----------------------------------------------
# ** def test_step(self):
#  ----------------------------------------------:
    def test_step(self):
        self.sd._steps_left = 0
        self.assertEqual(self.sd._steps_left, 0)      
        self.sd.step()
        self.assertEqual(self.sd._steps_left, -1)      

        self.sd._steps_left = 10
        self.assertEqual(self.sd._steps_left, 10)      
        self.sd.step()
        self.assertEqual(self.sd._steps_left, 9)      


#  ----------------------------------------------:
# ** def test_step_encoder(self) : 
#  ----------------------------------------------:
    def test_step_encoder(self):
        self.sd._steps_left = 0
        self.assertEqual(self.sd._steps_left, 0)      
        from stm_encod import Encoder
        enc = Encoder(pyb.Pin.cpu.C13, pyb.Pin.cpu.A5)
        self.sd.step_ecoder(enc.corrector)
        self.assertEqual(self.sd._steps_left, -1)      
        self.sd._steps_left = 10
        self.assertEqual(self.sd._steps_left, 10)      
        self.sd.step()
        self.assertEqual(self.sd._steps_left, 9)      


#  ----------------------------------------------:
# ** def test_step_on(self):
#  ----------------------------------------------:
    def test_step_on(self):
        self.sd._steps_left = 0
        self.assertEqual(self.sd._steps_left, 0)      
        self.sd.step_on(10, 1000)
        self.assertEqual(self.sd._steps_left, 0)      
        self.sd._steps_left = 10
        self.assertEqual(self.sd._steps_left, 10)      
        self.sd.step_on(10, 1000)
        self.assertEqual(self.sd._steps_left, 0)      
        self.sd._steps_left = -10
        self.assertEqual(self.sd._steps_left, -10)      
        self.sd.step_on(10, 1000)
        self.assertEqual(self.sd._steps_left, 0)      


#  ----------------------------------------------:
# ** def test_step_on_enc(self):
#  ----------------------------------------------:
    def test_step_on_encod(self):
        self.sd._steps_left = 0
        self.assertEqual(self.sd._steps_left, 0)      
        from stm_encod import Encoder
        enc = Encoder(pyb.Pin.cpu.C13, pyb.Pin.cpu.A5)
        self.sd.step_on_encod([0, 10], enc, offtime = 1000 )
        self.assertEqual(self.sd._steps_left, 0)      
        self.sd._steps_left = 10
        self.assertEqual(self.sd._steps_left, 10)      
        self.sd.step_on_encod([0, 10], enc, offtime = 1000 )
        self.assertEqual(self.sd._steps_left, 0)      
        self.sd._steps_left = -10
        self.assertEqual(self.sd._steps_left, -10)      
        self.sd.step_on_encod([0, 10], enc, offtime = 1000 )
        self.assertEqual(self.sd._steps_left, 0)      


#  ----------------------------------------------:
# ** def test_rutine(self): : 
#  ----------------------------------------------:
    def test_rutine(self):
        self.sd.rutine(CMD_STEPS, [100, 10])
        self.sd.rutine(CMD_SET_OFFTIME, [100, 10])
        self.sd.rutine(CMD_SET_ONTIME, [100, 10])
        self.sd.rutine(CMD_10KSTEPS, [0, 10])

# ** ----------------------------------------------:
# * def suite Init(): : 
def suite_Init():
    suite = unittest.TestSuite()
    suite.addTest(Test_Init('test_init1'))
    suite.addTest(Test_Fun('test_step'))
    suite.addTest(Test_Fun('test_step_on'))
    suite.addTest(Test_Fun('test_rutine'))
    return suite
# ----------------------------------------------


# * Test runer : 
# ----------------------------------------------
# (compile " D:/Development/version-control/GitHub/Vadim/Tochil/main_test.py -k init")
# (compile " python -m unittest D:/Development/version-control/GitHub/Vadim/Tochil/main_test.py ")
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    # runner = unittest.TextTestRunner()
    # runner.run(suite_Init())
    unittest.main()
# * ----------------------------------------------:
