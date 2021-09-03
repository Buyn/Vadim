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
# **  Write a single command :
   def steps(self, times = 1):
      self._stm.write_cmd_arg(self._motor, CMD_STEPS, [times, 0])
      # self.bus.write_byte(self.addr, cmd)
      # sleep(0.0001)


#  ----------------------------------------------:
# * ----------------------------------------------:
