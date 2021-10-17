# ----------------------------------------------
# * import block# :
from i2c_rpi_driver import *


# ----------------------------------------------
# * Vars block :

#  ----------------------------------------------:
# * Commands list block :
CMD_STEPS       = 10
CMD_10KSTEPS    = 11
CMD_SET_OFFTIME = 20
CMD_SET_ONTIME  = 21
CMD_HOMERUN     = 100

#  ----------------------------------------------:
# * class stepmotor_rpi_driver: : 
# ** class **-------------------------------------:
class stepmotor_rpi_driver:


#  ----------------------------------------------:
# ** __init__ : 
#  ----------------------------------------------:
   def __init__(self, stm, motor):
      self._stm = stm
      self._motor = motor


#  ----------------------------------------------:
# ** def steps(self, times = 1): : 
#  ----------------------------------------------:
   def steps(self, times = 1):
      if times < 65535: self.normal_steps(times) 
      else: self.k10step(times)


#  ----------------------------------------------:
# ** def normal_steps(self, times = 1): : 
#  ----------------------------------------------:
   def normal_steps(self, times = 1):
      _ = (times).to_bytes(2, "big")
      self._stm.write_cmd_arg(self._motor, CMD_STEPS, [_[0], _[1]])
      # sleep(0.0001)


#  ----------------------------------------------:
# ** def k10step(self, ksteps): : 
#  ----------------------------------------------:
   def k10step(self, allsteps):
      steps = allsteps % 10000
      ksteps = (allsteps - steps)/10000
      # if ksteps > 65535: ksteps = 65535
      _ = int(ksteps).to_bytes(2, "big")
      self._stm.write_cmd_arg(self._motor, CMD_10KSTEPS, [_[0], _[1]])
      sleep(0.001)
      if steps : self.normal_steps(steps)
      return steps, ksteps


#  ----------------------------------------------:
# ** def homerun : 
#  ----------------------------------------------:
   def homerun(self, timeout = 0): 
      if timeout > 65535: timeout = 65535
      _ = (timeout).to_bytes(2, "big")
      self._stm.write_cmd_arg(self._motor, CMD_HOMERUN, [_[0], _[1]])


#  ----------------------------------------------:
# ** def set_ontime(self, timeout):  : 
#  ----------------------------------------------:
   def set_ontime(self, timeout): 
      if timeout > 65535: timeout = 65535
      _ = (timeout).to_bytes(2, "big")
      self._stm.write_cmd_arg(self._motor, CMD_SET_ONTIME, [_[0], _[1]])


#  ----------------------------------------------:
# ** def set_offtime(self, timeout):  : 
#  ----------------------------------------------:
   def set_offtime(self, timeout): 
      if timeout > 65535: timeout = 65535
      _ = (timeout).to_bytes(2, "big")
      self._stm.write_cmd_arg(self._motor, CMD_SET_OFFTIME, [_[0], _[1]])


#  ----------------------------------------------:
# ** ----------------------------------------------:
# * ----------------------------------------------:
