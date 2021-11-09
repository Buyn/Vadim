# ----------------------------------------------
# * import block :
import unittest
import sys
from unittest.mock import MagicMock, patch

sys.modules['micropython'] = MagicMock()
from stepmotor_rpi_driver import *

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
        mw = stepmotor_rpi_driver( i2c_device(13, 1), 1)
        self.assertIsNotNone( mw)
        self.assertIsNotNone( mw._stm)
        self.assertIsNotNone( mw._motor)
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
#  ----------------------------------------------:
    @classmethod #setUpClass# {{{
    def setUpClass(self):
        print("*"*33,"*"*33)
        self.sd = stepmotor_rpi_driver( i2c_device(13, 1), 1)
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
# ** def test_steps(self):
#  ----------------------------------------------:
    def test_steps(self):
        print(self.sd.steps(100))
        print(self.sd.steps(1000))
        print(self.sd.steps(10000))
        print(self.sd.steps(100000))
        print(self.sd.steps(1000000))
        print(self.sd.steps(1000001))


# ** def test_status(self) : 
#  ----------------------------------------------:
    def test_status(self):
        print(self.sd.status(STT_READY))


# ** def test_is_ready(self) : 
#  ----------------------------------------------:
    def test_is_ready(self):
        self.assertTrue(self.sd.is_ready())


#  ----------------------------------------------:
# ** def test_homerun(self):
# ----------------------------------------------
    def test_homerun(self):
        self.sd.homerun()


#  ----------------------------------------------:
# ** def test_set_speed(self): : 
# ----------------------------------------------
    def test_set_speed(self):
        self.sd.set_ontime(100)
        self.sd.set_offtime(200)


#  ----------------------------------------------:
# ** def test_multstep(self): : 
# ----------------------------------------------
    def test_multstep(self):
        s, ks = self.sd.k10step(111111)
        self.assertEqual(s , 1111) 
        self.assertEqual(ks , 11) 
        s, ks = self.sd.k10step(100000)
        self.assertEqual(s , 0) 
        self.assertEqual(ks , 10) 
        s, ks = self.sd.k10step(70000)
        self.assertEqual(s , 0) 
        self.assertEqual(ks , 7) 
        s, ks = self.sd.k10step(70001)
        self.assertEqual(s , 1) 
        self.assertEqual(ks , 7) 
        s, ks = self.sd.k10step(99999)
        self.assertEqual(s , 9999) 
        self.assertEqual(ks , 9) 


# ** ----------------------------------------------:
# * def suite Init(): : 
def suite_Init():
    suite = unittest.TestSuite()
    # suite.addTest(Test_Init('test_init1'))
    suite.addTest(Test_Fun('test_steps'))
    # suite.addTest(Test_Fun('test_homerun'))
    # suite.addTest(Test_Fun('test_set_speed'))
    # suite.addTest(Test_Fun('test_multstep'))
    # suite.addTest(Test_Fun('test_status'))
    # suite.addTest(Test_Fun('test_is_ready'))
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
