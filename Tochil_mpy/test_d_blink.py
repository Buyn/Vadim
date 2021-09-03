# ----------------------------------------------
# * import block# :
import unittest
import sys
from unittest.mock import MagicMock, patch

sys.modules['micropython'] = MagicMock()
from d_blink import *

# ----------------------------------------------


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
        # self.sd = mainloop()
        # self.mw = Main_Windows()
        #     print ("file opened")
        # print("*"*33,"*"*33)
        
        
# ----------------------------------------------
# ** @classmethod #tearDownClass# : 
    @classmethod #tearDownClass# {{{
    def tearDownClass(self):
        print("*"*33,"*"*33)
        print("tear down module")
        # self.sd = None
        print("*"*33,"*"*33)

# ----------------------------------------------
# ** def test_inits(self): 
    def test_inits(self):
        # print("probs")
        # print(step_pins)
        self.assertEqual(timeout, 100)
        self.assertEqual( len(step_pins), 2)
        self.assertEqual( len(sms), 2)
        # print(sms)



# ** def test_d_blink(self): : 
    def test_d_blink(self):
        self.assertEqual( diod_status, False)
        print("start")
        r = testloop()
        # self.sd.step()
        self.assertEqual( r, maxcount)
        # self.assertEqual( diod_status, True)
        print("stop")


# ** ----------------------------------------------:
# * def suite Init(): : 
def suite_Init():
    suite = unittest.TestSuite()
    # suite.addTest(Test_Init('test_init1'))
    suite.addTest(Test_Fun('test_inits'))
    suite.addTest(Test_Fun('test_d_blink'))
    # suite.addTest(WidgetTestCase('test_widget_resize'))
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
