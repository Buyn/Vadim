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


    @patch('micropython.alloc_emergency_exception_buf')
    def test_load_image(self, imread):
        print('alloc_emergency_exception_buf=', imread)
        assert imread.called

# ** def test_init1 : 
    def test_init1(self):# {{{
        mw = None
        self.assertIsNone( mw)
        mw = Step_Driver(pyb.Pin.cpu.C13)
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
    @patch('micropython.alloc_emergency_exception_buf')
    def test_load_image(self, imread):
        print('alloc_emergency_exception_buf=', imread)
        assert imread.called

# ** @classmethod #setUpClass#  : 
    @classmethod #setUpClass# {{{
    def setUpClass(self):
        print("*"*33,"*"*33)
        self.sd = Step_Driver(pyb.Pin.cpu.C13)
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
# ** def test_step(self):
    def test_step(self):
        self.sd.step()

# ** def test_step_on(self):
    def test_step_on(self):
        self.sd.step_on(10, 1000)

# ** def test_StarComform(self):
    def test_StarComform(self):
        test = ConformSharpeningScreen()
        # print("main_menu_timer_label =", main_menu_timer_label)
        result = test.make_comform_list_string( ("New!", "test", "test!"))
        self.assertEqual( result, ' New!\n test\n test!\n ')



# ** def test_Sharp_cheng(self):
    def test_Sharp_cheng(self):
        test = SharpScreen()
        # print("main_menu_timer_label =", main_menu_timer_label)
        self.assertIsNotNone(test.list_of_chosens)
        test.chenge_list( add = ("New!", "test", "test!"), remove = ("Full cicle", "sdf"))
        tuple_var = ("Full cicle", "sdf")
        print(type(tuple_var))
        if isinstance(tuple_var, tuple) : print ("It Tuple")
        else: print ("Not Tuple")
        test.chenge_list()
        self.assertEqual( test.list_of_chosens, { 'Too sides', 'Antibacterial', "New!", "test", "test!"})
        test.chenge_list( add = ("Full cicle"), remove = ("test"))
        # print (test.list_of_chosens)
        self.assertEqual( test.list_of_chosens, { 'Too sides', 'Antibacterial', "New!", "Full cicle", "test!"})



# ** ----------------------------------------------:
# * def suite Init(): : 
def suite_Init():
    suite = unittest.TestSuite()
    # suite.addTest(Test_Init('test_init1'))
    # suite.addTest(Test_Fun('test_step'))
    suite.addTest(Test_Fun('test_step_on'))
    # suite.addTest(Test_Fun('test_Sharp_cheng'))
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
