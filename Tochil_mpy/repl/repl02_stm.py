# * Init :
D:\shell\Putty\putty.exe -serial com16
cd "D:\Development\version-control\GitHub\Vadim\Tochil_mpy"
# -----------------------------------
# * mainloop :
from stm_main import
mainloop()
# -----------------------------------
# * encoder stm :
from stm_encod import *
enc_pin02 = pyb.Pin.board.PB2
enc_pin01 = pyb.Pin.board.PB10
encoder = Encoder(enc_pin01, enc_pin02)
encoder.get_data()

def print_cheng(self, timeout = 1000): 
    encoder.timeout= timeout
    while True:
      if encoder.have_data() : print(encoder.get_data())

print_cheng()

# -----------------------------------
# * encoder original:
from encoder import *
enc_pin02 = pyb.Pin.board.PB2 # work
# enc_pin01 = pyb.Pin.board.PB10 # not working
enc_pin01 = pyb.Pin.board.PA3 # Testing
encoder = encoder(enc_pin01, enc_pin02)
encoder.counter3 = 0
encoder.get_data()

def print_cheng(self): 
    while True:
      if encoder.have_data() : print(encoder.get_data())


# -----------------------------------
# * get_msg : 
from i2c_stm_driver import *
sd = I2C_com()
sd.get_msg()


# -----------------------------------
# * i2c_2s_send : 
from i2c_stm_driver import *
sd = I2C_com()
sd.i2c_2s_send(5, "abc")
sd.i2c_2s_send(5)
# -----------------------------------
# * print_in : 
from i2c_stm_driver import *
sd = I2C_com()
sd.print_in(5)
# standart oure command 5 bite
# if less time out error
# if inout error retry
# if more show nothing
# -----------------------------------
# * i2c_exec : 
from i2c_stm_driver import *
sd = I2C_com()
sd.print_in_out(1)
sd.print_in(2)
sd.print_in(3)
sd.i2c_pinset(0)
sd.i2c_exec(b'\x13')
# -----------------------------------
# * diode_com : 
from i2c_stm_driver import *
sd = I2C_com()
sd.diode_com()
# -----------------------------------
# * i2c_2s_send : 
from i2c_stm_driver import *
sd = I2C_com()
sd.i2c_2s_send()
# -----------------------------------
# * WS2812(spi_bus=1, led_count=4) : 
from ws2812 import WS2812
chain = WS2812(spi_bus=1, led_count=4)
chain.show([(255, 0, 0, 0), (0, 255, 0, 0), (0, 0, 255, 0), (85, 85, 85, 0),])
chain.show([(255, 0, 0, 10), (0, 255, 0, 100), (0, 0, 255, 100), (85, 85, 85, 100),])

chain.show([(255, 0, 0, 0), (255, 0, 0, 0), (255, 0, 0, 0), (255, 0, 0, 0),])
chain.show([(255, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (255, 0, 0, 0),])
# -----------------------------------
# * WS2812(spi_bus=1, led_count=5) : 
from ws2812 import WS2812
chain = WS2812(spi_bus=1, led_count=5)
chain.show([(255, 0, 0, 0), (0, 255, 0, 0), (0, 0, 255, 0), (255, 255, 0, 0), (255, 0, 255, 0),])
chain.show([(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 255, 0),])
# -----------------------------------
# * step motore activ :
from driver_m import *
step_pin = pyb.Pin.cpu.B13
end_pin = pyb.Pin.cpu.B5
sd = Step_Driver(step_pin, end_pin, 100)
sd.step_on(100,100)
# -----------------------------------
# * step motore old xheged :
from driver_m import *
step_pin = pyb.Pin.cpu.B13
sd = Step_Driver(step_pin)
sd.step_on(100,100)
# -----------------------------------
# * step_pin.value(0) : 
from driver_m import *
step_pin = pyb.Pin.cpu.B13
step_pin.value(0)
# -----------------------------------
# * step motore diod mode test:
from driver_m import *
step_pin = pyb.Pin.cpu.B13
end_pin = pyb.Pin.cpu.B5
sd = Step_Driver(step_pin, end_pin, 1000000)
sd.step_on(10,1000000)
# -----------------------------------
