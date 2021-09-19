D:\shell\Putty\putty.exe -serial com16
cd "D:\Development\version-control\GitHub\Vadim\Tochil_mpy"
# -----------------------------------
from stm_main import *
mainloop()
int.from_bytes([100,100], "big") 
# -----------------------------------
from i2c_stm_driver import *
sd = I2C_com()
sd.get_msg()
# -----------------------------------
from i2c_stm_driver import *
sd = I2C_com()
sd.i2c_2s_send(1)
# -----------------------------------
from i2c_stm_driver import *
sd = I2C_com()
sd.print_in()
# -----------------------------------
from i2c_stm_driver import *
sd = I2C_com()
sd.print_in_out(1)
sd.print_in(2)
sd.print_in(3)
sd.i2c_pinset(0)
sd.i2c_exec(b'\x13')
# -----------------------------------
from i2c_stm_driver import *
sd = I2C_com()
sd.diode_com()
# -----------------------------------
from i2c_stm_driver import *
sd = I2C_com()
sd.i2c_2s_send()
# -----------------------------------
from ws2812 import WS2812
chain = WS2812(spi_bus=1, led_count=4)
chain.show([(255, 0, 0, 0), (0, 255, 0, 0), (0, 0, 255, 0), (85, 85, 85, 0),])
chain.show([(255, 0, 0, 10), (0, 255, 0, 100), (0, 0, 255, 100), (85, 85, 85, 100),])

chain.show([(255, 0, 0, 0), (255, 0, 0, 0), (255, 0, 0, 0), (255, 0, 0, 0),])
chain.show([(255, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (255, 0, 0, 0),])
# -----------------------------------
from ws2812 import WS2812
chain = WS2812(spi_bus=1, led_count=5)
chain.show([(255, 0, 0, 0), (0, 255, 0, 0), (0, 0, 255, 0), (255, 255, 0, 0), (255, 0, 255, 0),])
chain.show([(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 255, 0),])
# -----------------------------------
# step motore
from driver_m import *
step_pin = pyb.Pin.cpu.B13
sd = Step_Driver(step_pin)
sd.step_on(100,100)
# -----------------------------------

# -----------------------------------
