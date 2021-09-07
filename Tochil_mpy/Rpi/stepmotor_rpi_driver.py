# ----------------------------------------------
# * import block# :
from i2c_rpi_driver import *


# ----------------------------------------------
# * Vars block :

#  ----------------------------------------------:
# * Commands list block :
CMD_STEPS = 10

#  ----------------------------------------------:
# * i2c_device: : 
class stepmotor_rpi_driver:
# ** __init__ : 
   def __init__(self, stm, motor):
      self._stm = stm
      self._motor = motor


#  ----------------------------------------------:
# ** def steps(self, times = 1): : 
   def steps(self, times = 1):
      # r = 65535
      # print(int("0xffff", base=16 ))
      # print((r).to_bytes(2, "big"))
      if times > 65535: times = 65535
      _ = (times).to_bytes(2, "big")
      self._stm.write_cmd_arg(self._motor, CMD_STEPS, [_[0], _[1]])
      # self.bus.write_byte(self.addr, cmd)
      # sleep(0.0001)


#  ----------------------------------------------:
# * ----------------------------------------------:
