# ----------------------------------------------
# * import block :
import unittest
import sys
from unittest.mock import MagicMock, patch

sys.modules['micropython'] = MagicMock()
from i2c_rpi_driver import *

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
        mw = i2c_device( 13, 1)
        self.assertIsNotNone( mw)
        self.assertIsNotNone( mw.bus)
        self.assertIsNotNone( mw.cmd_list)
        self.assertEqual( len(mw.cmd_list), 0)
        self.assertIsNotNone( mw.msg_list)
        self.assertEqual( len(mw.msg_list), 0)
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
        self.sd = i2c_device(13)
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
# ** def test_write_cmd(self):
    def test_write_cmd(self):
        self.sd.write_cmd( 13 )

# ** def test_write_block_data(self): : 
    def test_write_block_data(self):
        self.sd.write_block_data( 14, 5)

# ** def test_write_cmd_arg(self): : 
    def test_write_cmd_arg(self):
        # print (list(range(11))[::-1])
        r = self.sd.write_cmd_arg( 1, 13, [13, 14 ] )
        # self.assertEqual( int.from_bytes(r.buf[0], "big"), 10)
        # self.assertEqual( int.from_bytes(r.buf[0], "big"), 10)
        self.assertEqual( r, 11)


# ** def test_send_2_simbol(self):
    def test_send_2_simbol(self):
        self.sd.send_2_simbol(10, 1000)

# ** def test_send_simbol(self):
    def test_send_simbol(self):
        self.sd.send_simbol("0x10")

# ** def test_send_resiv(self):
    def test_send_resiv(self):
        print(self.sd.send_resiv("0x10"))

# ** def test_StarComform(self):
    def test_StarComform(self):
        test = ConformSharpeningScreen()
        # print("main_menu_timer_label =", main_menu_timer_label)
        result = test.make_comform_list_string( ("New!", "test", "test!"))
        self.assertEqual( result, ' New!\n test\n test!\n ')



# ** def test_msg_list_size(self):
    def test_msg_list_size(self):
       result = self.sd.msg_list_size()
       self.assertEqual( result, 11)
       result = self.sd.msg_list_size()
       self.assertEqual( result, 11)


# ** def test_msg_get_one(self):
    def test_msg_get_one(self):
       result = self.sd.msg_get_one()
       self.assertEqual( result, [11, 12, 13, 14])
       result = self.sd.msg_get_one()
       self.assertEqual( result, [11, 12, 13, 14])


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
    suite.addTest(Test_Init('test_init1'))
    # suite.addTest(Test_Fun('test_send_resiv'))
    suite.addTest(Test_Fun('test_write_cmd_arg'))
    # suite.addTest(Test_Fun('test_write_block_data'))
    # suite.addTest(Test_Fun('test_wr_cmd_arg'))
    suite.addTest(Test_Fun('test_msg_list_size'))
    suite.addTest(Test_Fun('test_msg_get_one'))
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
