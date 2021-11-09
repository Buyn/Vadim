# ##############################################
# ==============================================
# * import block * # :
# ==============================================
import unittest
import sys
# from unittest.mock import MagicMock, patch
# sys.modules['micropython'] = MagicMock()
from rpi_encod import *


# ==============================================
# ==============================================
# * class Test_Init * # : 
# ** ======= class ===============================:
class Test_Init(unittest.TestCase):


# ----------------------------------------------:
# ** def test_init1 : 
# ----------------------------------------------:
  def test_init1(self):# {{{
    test = None
    self.assertIsNone(test)
    test = Encoder(i2c_device(13, 1))
    self.assertIsNotNone( test._stm)

            				
# ----------------------------------------------
# ** ===========================================:


# ==============================================
# * class Test_Fun(unittest.TestCase) * # : 
# ** ======= class =============================:
class Test_Fun(unittest.TestCase):


# ----------------------------------------------
# ** @classmethod #setUpClass#  : 
# ----------------------------------------------
    @classmethod #setUpClass# {{{
    def setUpClass(self):
        print("*"*33,"*"*33)
        self.test = Encoder(i2c_device(13, 1))
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
# ** def test_get_data(self) : 
# ----------------------------------------------
    def test_get_data(self):
        self.assertEqual( self.test.get_data(), 3342)
        # self.assertEqual( self.test.get_data(), 1)


# ----------------------------------------------
# ** def test_status(self) : 
#  ----------------------------------------------:
    def test_status(self):
        print(self.test.status(STT_READY))


# ** def test_is_ready(self) : 
#  ----------------------------------------------:
    def test_is_ready(self):
        self.assertTrue(self.test.is_ready())


#  ----------------------------------------------:
# ** test_msg_convert : 
#  ----------------------------------------------:
    def test_msg_convert(self):
       self.assertEqual(100, self.test.msg_convert(0, 100))
       self.assertEqual(256, self.test.msg_convert(1, 0))
       self.assertEqual(257, self.test.msg_convert(1, 1))
       self.assertEqual(267, self.test.msg_convert(1, 11))
        


#  ----------------------------------------------:



# ** ===========================================:


# ==============================================
# * suite_Init(self) : 
# ==============================================
def suite_Init():
    suite = unittest.TestSuite()
    # suite.addTest(Test_Init('test_init1'))
    suite.addTest(Test_Fun('test_get_data'))
    # suite.addTest(Test_Fun('test_status'))
    # suite.addTest(Test_Fun('test_is_ready'))
    suite.addTest(Test_Fun('test_msg_convert'))
    return suite
		

# ==============================================
# ==============================================
# * Test runer : 
# ==============================================
# (compile " D:/Development/version-control/GitHub/Vadim/Tochil/main_test.py -k init")
# (compile " python -m unittest D:/Development/version-control/GitHub/Vadim/Tochil/main_test.py ")
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    runner = unittest.TextTestRunner()
    runner.run(suite_Init())
    # unittest.main()


# ==============================================
# * ############################################ :
