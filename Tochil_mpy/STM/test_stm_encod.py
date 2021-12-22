# ##############################################
# ==============================================
# * import block * # :
# ==============================================
import unittest
import sys
from unittest.mock import MagicMock, patch
sys.modules['micropython'] = MagicMock()
from stm_encod import *


# ==============================================
# * class Test_Init * # : 
# ** ======= class ===============================:
class Test_Init(unittest.TestCase):


    # @patch('micropython.alloc_emergency_exception_buf')
    # def test_load_image(self, imread):
    #     print('alloc_emergency_exception_buf=', imread)
    #     assert imread.called
# ----------------------------------------------:
# ** def test_init1 : 
# ----------------------------------------------:
    def test_init1(self):# {{{
        mw = None
        self.assertIsNone( mw)
        mw = Encoder(pyb.Pin.cpu.C13, pyb.Pin.cpu.A5)
        # temp_A = 11
        # temp_B = 14
        self.assertIsNotNone( mw)
        self.assertIsNotNone( mw.pin01)
        self.assertIsNotNone( mw.pin02)
        # self.assertEqual( mw.pin, 'PC13')
        # self.assertEqual( mw.temp_B, 14)


# ----------------------------------------------
# ** ===========================================:


# ==============================================
# * class Test_Fun(unittest.TestCase) * # : 
# ** ======= class =============================:
class Test_Fun(unittest.TestCase):


# ----------------------------------------------
# ** @classmethod #setUpClass#  : 
# ----------------------------------------------:
    @classmethod #setUpClass# {{{
    def setUpClass(self):
        print("*"*33,"*"*33)
        self.sd = Encoder(pyb.Pin.cpu.C13, pyb.Pin.cpu.A5)
        # self.mw = Main_Windows()
        #     print ("file opened")
        # print("*"*33,"*"*33)
        
        
# ----------------------------------------------
# ** @classmethod #tearDownClass# : 
# ----------------------------------------------:
    @classmethod #tearDownClass# {{{
    def tearDownClass(self):
        print("*"*33,"*"*33)
        print("tear down module")
        self.sd = None
        print("*"*33,"*"*33)

# ----------------------------------------------
# ** def test_reset_time(self):
# ----------------------------------------------:
    def test_reset_time(self):
        self.sd.sensor_time = 100
        self.assertEqual( self.sd.sensor_time, 100)
        tmp = utime.TIME_MICROSEKUNDS 
        utime.TIME_MICROSEKUNDS = 0
        self.sd.reset_time()
        self.assertEqual( self.sd.sensor_time, self.sd.timeout)
        utime.TIME_MICROSEKUNDS = tmp


# ----------------------------------------------:
# ** def test_callback_pin01(self):
# ----------------------------------------------:
    def test_callback_pin01(self):
        self.sd.counter3 = 0
        self.assertEqual( self.sd.counter3, 0)
        self.sd.pin01.PIN_VALUE = False
        self.assertEqual( self.sd.pin01.value(), False)
        self.sd.pin02.PIN_VALUE = True
        self.assertEqual( self.sd.pin02.value(), True)
        self.sd.callback_pin01('tim')
        self.assertEqual( self.sd.counter3, 1)
        self.sd.pin01.PIN_VALUE = True
        self.sd.pin02.PIN_VALUE = False
        self.sd.callback_pin01('tim')
        # self.sd.counter3 += 1
        self.assertEqual( self.sd.counter3, 2)
        self.sd.pin01.PIN_VALUE = True
        self.sd.pin02.PIN_VALUE = True
        self.sd.callback_pin01('tim')
        # self.sd.counter3 += 1
        self.assertEqual( self.sd.counter3, 1)
        self.sd.pin01.PIN_VALUE = False
        self.sd.pin02.PIN_VALUE = False
        self.sd.callback_pin01('tim')
        # self.sd.counter3 += 1
        self.assertEqual( self.sd.counter3, 0)
        # self.assertEqual( test.list_of_chosens, { 'Too sides', 'Antibacterial', "New!", "Full cicle", "test!"})


# ----------------------------------------------:
# ** def test_callback_pin02(self):
# ----------------------------------------------:
    def test_callback_pin02(self):
        # self.sd.callback_pin02('tim')
        self.sd.counter3 = 0
        self.assertEqual( self.sd.counter3, 0)
        self.sd.pin01.PIN_VALUE = True
        self.assertEqual( self.sd.pin01.value(), True)
        self.sd.pin02.PIN_VALUE = True
        self.assertEqual( self.sd.pin02.value(), True)
        self.sd.callback_pin02('tim')
        self.assertEqual( self.sd.counter3, 1)
        self.sd.pin01.PIN_VALUE = False
        self.assertEqual( self.sd.pin01.value(), False)
        self.sd.pin02.PIN_VALUE = False
        self.assertEqual( self.sd.pin02.value(), False)
        self.sd.callback_pin02('tim')
        # self.sd.counter3 += 1
        self.assertEqual( self.sd.counter3, 2)
        self.sd.pin01.PIN_VALUE = False
        self.sd.pin02.PIN_VALUE = True
        self.sd.callback_pin02('tim')
        # self.sd.counter3 += 1
        self.assertEqual( self.sd.counter3, 1)
        self.sd.pin01.PIN_VALUE = True
        self.sd.pin02.PIN_VALUE = False
        self.sd.callback_pin02('tim')
        # self.sd.counter3 += 1
        self.assertEqual( self.sd.counter3, 0)


# ----------------------------------------------:
# ** def test_new_callback_pin01(self):
# ----------------------------------------------:
    def test_new_callback_pin01(self):
        self.sd.counter3 = 0
        self.assertEqual( self.sd.counter3, 0)
        self.sd.pin01.PIN_VALUE = False
        self.assertEqual( self.sd.pin01.value(), False)
        self.sd.pin02.PIN_VALUE = True
        self.assertEqual( self.sd.pin02.value(), True)
        self.sd.pin01.PIN_VALUE = True # for chenge on opisete in calbeke
        self.sd.gipo_checker()
        self.sd.new_callback_pin01('tim')
        self.assertEqual( self.sd.counter3, 1)
        self.sd.pin01.PIN_VALUE = True
        self.sd.pin02.PIN_VALUE = False
        self.sd._last_pin01 = False # for chenge on opisete in calbeke
        self.sd._last_pin02 = False
        self.sd.new_callback_pin01('tim')
        # self.sd.counter3 += 1
        self.assertEqual( self.sd.counter3, 2)
        self.sd.pin01.PIN_VALUE = True
        self.sd.pin02.PIN_VALUE = True
        self.sd._last_pin01 = False # for chenge on opisete in calbeke
        self.sd._last_pin02 = True
        self.sd.new_callback_pin01('tim')
        # self.sd.counter3 += 1
        self.assertEqual( self.sd.counter3, 1)
        self.sd.pin01.PIN_VALUE = False
        self.sd.pin02.PIN_VALUE = False
        self.sd._last_pin01 = True # for chenge on opisete in calbeke
        self.sd._last_pin02 = False
        self.sd.new_callback_pin01('tim')
        # self.sd.counter3 += 1
        self.assertEqual( self.sd.counter3, 0)


# ----------------------------------------------:
# ** def test_new_callback_pin02(self):
# ----------------------------------------------:
    def test_new_callback_pin02(self):
        self.sd.counter3 = 0
        self.assertEqual( self.sd.counter3, 0)
        self.sd.pin01.PIN_VALUE = True
        self.assertEqual( self.sd.pin01.value(), True)
        self.sd.pin02.PIN_VALUE = True
        self.assertEqual( self.sd.pin02.value(), True)
        self.sd.pin02.PIN_VALUE = False # for chenge on opisete in calbeke
        self.sd.gipo_checker()
        self.sd.new_callback_pin02('tim')
        self.assertEqual( self.sd.counter3, 1)
        self.sd.pin01.PIN_VALUE = False
        self.sd.pin02.PIN_VALUE = False
        self.sd._last_pin01 = False 
        self.sd._last_pin02 = True # for chenge on opisete in calbeke
        self.sd.new_callback_pin02('tim')
        # self.sd.counter3 += 1
        self.assertEqual( self.sd.counter3, 2)
        self.sd.pin01.PIN_VALUE = False
        self.sd.pin02.PIN_VALUE = True
        self.sd._last_pin01 = False 
        self.sd._last_pin02 = False # for chenge on opisete in calbeke
        self.sd.new_callback_pin02('tim')
        # self.sd.counter3 += 1
        self.assertEqual( self.sd.counter3, 1)
        self.sd.pin01.PIN_VALUE = True
        self.sd.pin02.PIN_VALUE = False
        self.sd._last_pin01 = True 
        self.sd._last_pin02 = True # for chenge on opisete in calbeke
        self.sd.new_callback_pin02('tim')
        # self.sd.counter3 += 1
        self.assertEqual( self.sd.counter3, 0)


# ----------------------------------------------:
# ** test_gipo_checker : 
#  ----------------------------------------------:
    def test_gipo_checker(self):
        self.sd.pin01.PIN_VALUE = True
        self.sd._last_pin01 = False
        self.sd._last_pin02 = False
        self.assertEqual( self.sd.pin01.value(), True)
        self.sd.gipo_checker()
        self.assertEqual( self.sd._last_pin01, True)
        self.sd.pin02.PIN_VALUE = True
        self.assertEqual( self.sd.pin02.value(), True)
        self.sd.gipo_checker()
        self.assertEqual( self.sd._last_pin02, True)
        self.sd.pin02.PIN_VALUE = False
        self.sd.gipo_checker()
        self.assertEqual( self.sd._last_pin02, False)
        self.sd.pin01.PIN_VALUE = False
        self.sd.gipo_checker()
        self.assertEqual( self.sd._last_pin01, False)


#  ----------------------------------------------:
# ** def test_corrector(self) : 
#  ----------------------------------------------:
    def test_corrector(self):
        self.sd.pin01.PIN_VALUE = False
        self.sd.pin02.PIN_VALUE = False
        self.sd._last_pin01 = True
        self.sd._last_pin02 = True
        self.sd.corrector()
        self.assertEqual( self.sd.pin01.value(), False)
        self.assertEqual(self.sd._last_pin01 , False )
        self.assertEqual( self.sd.pin02.value(), False)
        self.assertEqual(self.sd._last_pin02 , False )
        self.sd.pin01.PIN_VALUE = True
        self.sd._last_pin01 = False
        self.sd._last_pin02 = False
        self.assertEqual( self.sd.pin01.value(), True)
        self.sd.corrector()
        self.assertEqual( self.sd._last_pin01, True)
        self.sd.pin02.PIN_VALUE = True
        self.assertEqual( self.sd.pin02.value(), True)
        self.sd.corrector()
        self.assertEqual( self.sd._last_pin02, True)
        self.sd.pin02.PIN_VALUE = False
        self.sd.corrector()
        self.assertEqual( self.sd._last_pin02, False)
        self.sd.pin01.PIN_VALUE = False
        self.sd.corrector()
        self.assertEqual( self.sd._last_pin01, False)


#  ----------------------------------------------:
# ** def test_have_data(self):
# ----------------------------------------------:
    def test_have_data(self):
        self.sd.last_count = self.sd.counter3
        utime.TIME_MICROSEKUNDS = 0
        self.assertEqual( self.sd.have_data(), False)
        self.sd.last_count = self.sd.counter3 + self.sd.last_count + 1
        utime.TIME_MICROSEKUNDS = self.sd.sensor_time + 1
        self.assertEqual( self.sd.have_data(), True)
        # self.sd.have_data()
        # self.sd.counter3 += 1


# ----------------------------------------------:
# ** def test_get_data(self):
    def test_get_data(self):
# ----------------------------------------------:
        self.sd.last_count = self.sd.counter3 + self.sd.last_count + 1
        utime.TIME_MICROSEKUNDS = self.sd.sensor_time + 1
        self.assertEqual( self.sd.have_data(), True)
        self.assertEqual( self.sd.get_data(), self.sd.counter3)
        self.assertEqual( self.sd.have_data(), False)
        self.sd.last_count = self.sd.counter3 + self.sd.last_count + 1
        utime.TIME_MICROSEKUNDS = self.sd.sensor_time + 1
        self.assertEqual( self.sd.have_data(), True)
        self.assertEqual( self.sd.get_data(), self.sd.counter3)
        self.assertEqual( self.sd.have_data(), False)


# ----------------------------------------------:
# ** test_rutine : 
#  ----------------------------------------------:
    def test_rutine(self):
        r = self.sd.rutine(10, [0,1])
        self.assertEqual([1,1], self.sd.convert(257))
        self.assertEqual([0,255], self.sd.convert(255))
        self.assertEqual([100,0], self.sd.convert(25600))
        self.assertEqual([10, 0, 0], r)


#  ----------------------------------------------:
# ** ============================================ :


# ==============================================
# * class Test_REPL : 
# ** ======= class =============================:
class Test_REPL(unittest.TestCase):


    # @patch('micropython.alloc_emergency_exception_buf')
    # def test_load_image(self, imread):
    #     print('alloc_emergency_exception_buf=', imread)
    #     assert imread.called

# ** def test_repl_while : 
    def test_repl_while(self):# {{{
        enc = Encoder(pyb.Pin.board.PB4, pyb.Pin.board.PB5)
        # while True:
        enc.counter3 = enc.counter3 + enc.last_count + 10
        utime.TIME_MICROSEKUNDS = enc.sensor_time + 1
        if enc.have_data(): print ("c = ", enc.get_data())
        if enc.have_data(): print ("c = ", enc.get_data())
        enc.counter3 = enc.counter3 + enc.last_count - 100
        if enc.have_data(): print ("c = ", enc.get_data())
        utime.TIME_MICROSEKUNDS = enc.sensor_time + 1
        if enc.have_data(): print ("c = ", enc.get_data())
        if enc.have_data(): print ("c = ", enc.get_data())
        utime.TIME_MICROSEKUNDS = enc.sensor_time + 1
        if enc.have_data(): print ("c = ", enc.get_data())
        enc.counter3 = enc.counter3 + enc.last_count - 100
        if enc.have_data(): print ("c = ", enc.get_data())

            				
# ----------------------------------------------
# ** ============================================ :


# ==============================================
# * suite_Init(self) : 
# ==============================================
def suite_Init():
    suite = unittest.TestSuite()
    # loader = unittest.TestLoader()
    # start_dir = 'path/to/your/test/files'
    # suite = loader.discover(start_dir)
    # suite.addTest(Test_Init('test_init1'))
    # suite.addTest(Test_Fun('test_reset_time'))
    # suite.addTest(Test_Fun('test_callback_pin01'))
    # suite.addTest(Test_Fun('test_callback_pin02'))
    # suite.addTest(Test_Fun('test_have_data'))
    # suite.addTest(Test_Fun('test_get_data'))
    # suite.addTest(Test_Fun('test_rutine'))
    # suite.addTest(Test_REPL('test_repl_while'))
    return suite
		

# ==============================================
# * Test runer : 
# ==============================================
# (compile " D:/Development/version-control/GitHub/Vadim/Tochil/main_test.py -k init")
# (compile " python -m unittest D:/Development/version-control/GitHub/Vadim/Tochil/main_test.py ")
# (compile "python -m unittest discover -s D:/Development/version-control/GitHub/Vadim/Tochil -p 'test_*.py'")
# (compile "python -m unittest test_stm_encod")
# run all test in dir
# (compile "python -m unittest")
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    # runner = unittest.TextTestRunner()
    # runner.run(suite_Init())
    unittest.main()
    # unittest.Init()


# ==============================================
# * ############################################ :
