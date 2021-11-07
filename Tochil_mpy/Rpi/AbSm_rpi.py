# ----------------------------------------------
# * import block# :
from Port_drv_rpi import *
from stepmotor_rpi_driver import *


# ----------------------------------------------
# * Vars block :
PORT_ADRRES = 0x20

#  ----------------------------------------------:
# * Commands list block :
#  ----------------------------------------------:
SM_X            = 10
SM_Y            = 11
SM_Z            = 12
SM_R            = 13 #A


#  ----------------------------------------------:
# * AbSm_rpi: : 
class AbSm_rpi:
#  ----------------------------------------------:
# ** __init__ : 
   def __init__(self, sm, enbl, dir, max_pos):
#  ----------------------------------------------:
      self._sm = sm
      self._enbl = enbl
      self._dir = dir
      self._max_pos = max_pos
      self._pos = 0
      self._forward = True
      self._port = Port_drv_rpi(i2c_device(PORT_ADRRES))


#  ----------------------------------------------:
# ** def is_activ_dir_is_forward(self, forward): : 
#  ----------------------------------------------:
   def is_activ_dir_is_forward(self, forward):
       self._forward = forward


#  ----------------------------------------------:
# ** def move_to_pos(self, pos): : 
#  ----------------------------------------------:
   def move_to_pos(self, pos):
        if self._pos < 0: self._pos = 0
        if pos < 0: return
        if self._pos == pos: return
        if pos > self._max_pos : pos = self._max_pos
        if self._pos > pos:
            delta = self._pos - pos
            self.set_backward()
        if self._pos < pos:
            delta = pos - self._pos 
            self.set_forward()
        self._sm.steps(delta)
        self._pos = pos
        return delta


#  ----------------------------------------------:
# ** def set_forward(self): : 
#  ----------------------------------------------:
   def set_forward(self):
       if self._port.value(self._dir) == self._forward: return
       self._port.setport(self._dir, self._forward)


#  ----------------------------------------------:
# ** def set_backward(self): : 
#  ----------------------------------------------:
   def set_backward(self):
       if self._port.value(self._dir) !=  self._forward: return
       self._port.setport(self._dir, not self._forward)


#  ----------------------------------------------:
#  ----------------------------------------------:
# ** def maintenance(self): : 
#  ----------------------------------------------:
   def maintenance(self): 
      self.set_backward()
      self._sm.homerun()
      self._pos = 0


#  ----------------------------------------------:
# ** def set_offtime(self, timeout): : 
#  ----------------------------------------------:
   def set_offtime(self, timeout): 
      self._sm.set_offtime(timeout)


#  ----------------------------------------------:
# ** def set_ontime(self, timeout): : 
#  ----------------------------------------------:
   def set_ontime(self, timeout): 
      self._sm.set_ontime(timeout)


#  ----------------------------------------------:
# ** def is_ready : 
#  ----------------------------------------------:
   def is_ready(self): 
      return self._sm.is_ready()


#  ----------------------------------------------:
# * ----------------------------------------------:
