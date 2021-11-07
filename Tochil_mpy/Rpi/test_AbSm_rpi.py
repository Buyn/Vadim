# ----------------------------------------------
# * import block :
import unittest
import sys
from unittest.mock import MagicMock, patch

sys.modules['micropython'] = MagicMock()
from AbSm_rpi import *

# ----------------------------------------------
# * class Test_Init : 
# ** ----------------------------------------------:
class Test_Init(unittest.TestCase):


    # @patch('micropython.alloc_emergency_exception_buf')
    # def test_load_image(self, imread):
    #     print('alloc_emergency_exception_buf=', imread)
    #     assert imread.called

# ** def test_init1 : 
#  ----------------------------------------------:
    def test_init1(self):# {{{
        mw = None
        self.assertIsNone( mw)
        mw = AbSm_rpi( stepmotor_rpi_driver(i2c_device(13, 1), 1), 1, 2, 100000)
        self.assertIsNotNone( mw)
        self.assertIsNotNone( mw._sm)
        self.assertEqual( mw._max_pos, 100000)
        self.assertEqual( mw._enbl, 1)
        self.assertEqual( mw._dir, 2)
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
#  ----------------------------------------------:
    @classmethod #setUpClass# {{{
    def setUpClass(self):
        print("*"*33,"*"*33)
        self.test = AbSm_rpi( stepmotor_rpi_driver(i2c_device(13, 1), 1), A1, B5, 10000)
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
# ** def test_move_to_pos(self): : 
#  ----------------------------------------------:
    def test_move_to_pos(self):
        # self.assertFalse( self.test._pos)
        self.assertEqual( self.test._pos, 0)
        self.test._port.setport(self.test._dir, False)
        self.test.is_activ_dir_is_forward(False)
        self.assertFalse(self.test._port.value(self.test._dir))
        r = self.test.move_to_pos(100)
        self.assertEqual( r, 100)
        self.assertEqual( self.test._pos, 100)
        self.assertFalse(self.test._port.value(self.test._dir))
        r =self.test.move_to_pos(90)
        self.assertEqual( self.test._pos, 90)
        self.assertEqual( r, 10)
        self.assertTrue(self.test._port.value(self.test._dir))
        r = self.test.move_to_pos(900)
        self.assertEqual( self.test._pos, 900)
        self.assertEqual( r, 810)
        self.assertFalse(self.test._port.value(self.test._dir))
        # tests -values
        r = self.test.move_to_pos(-900)
        self.assertIsNone(r)
        self.assertEqual( self.test._pos, 900)
        self.assertFalse(self.test._port.value(self.test._dir))
        # tests values = 0
        r = self.test.move_to_pos(0)
        self.assertEqual( r, 900)
        self.assertEqual( self.test._pos, 0)
        self.assertTrue(self.test._port.value(self.test._dir))
        # tests pos is lowe then 0
        self.test._pos = -900
        r = self.test.move_to_pos(900)
        self.assertEqual( r, 900)
        self.assertEqual( self.test._pos, 900)
        self.assertFalse(self.test._port.value(self.test._dir))
        # tests values is more then max_pos
        r = self.test.move_to_pos(90000)
        self.assertEqual( r, 9100)
        self.assertEqual( self.test._pos, 10000)
        self.assertFalse(self.test._port.value(self.test._dir))
        # tests values = 0
        r = self.test.move_to_pos(0)
        self.assertEqual( r, 10000)
        self.assertEqual( self.test._pos, 0)
        self.assertTrue(self.test._port.value(self.test._dir))


#  ----------------------------------------------:
# ** def test_maintenance(self): : 
#  ----------------------------------------------:
    def test_maintenance(self):
        self.test.move_to_pos(100)
        self.assertEqual( self.test._pos, 100)
        self.test.maintenance()
        self.assertEqual( self.test._pos, 0)
        self.assertTrue(self.test._port.value(self.test._dir))


#  ----------------------------------------------:
# ** def test_is_activ_dir_is_forward(self): : 
#  ----------------------------------------------:
    def test_is_activ_dir_is_forward(self):
        self.test.is_activ_dir_is_forward(True)
        self.assertTrue( self.test._forward)
        self.assertTrue(self.test._port.value(self.test._dir))
        self.test.set_forward()
        self.assertTrue(self.test._port.value(self.test._dir))
        self.test.set_backward()
        self.assertFalse(self.test._port.value(self.test._dir))
        self.test.is_activ_dir_is_forward(False)
        self.assertFalse( self.test._forward)
        self.assertFalse(self.test._port.value(self.test._dir))
        self.test.set_backward()
        self.assertTrue(self.test._port.value(self.test._dir))
        self.test.set_forward()
        self.assertFalse(self.test._port.value(self.test._dir))


#  ----------------------------------------------:
# ** def test_set_speed(self): 
#  ----------------------------------------------:
    def test_set_speed(self):
        self.test.set_ontime(100)
        self.test.set_offtime(200)


#  ----------------------------------------------:
# ** def test_is_ready(self) : 
#  ----------------------------------------------:
    def test_is_ready(self):
        self.assertTrue(self.test.is_ready())


#  ----------------------------------------------:
# ** ----------------------------------------------:

# * def suite Init(): : 
def suite_Init():
    suite = unittest.TestSuite()
    suite.addTest(Test_Init('test_init1'))
    suite.addTest(Test_Fun('test_is_activ_dir_is_forward'))
    suite.addTest(Test_Fun('test_move_to_pos'))
    suite.addTest(Test_Fun('test_maintenance'))
    suite.addTest(Test_Fun('test_is_ready'))
    suite.addTest(Test_Fun('test_set_speed'))
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
