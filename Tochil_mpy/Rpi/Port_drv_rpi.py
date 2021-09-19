# ----------------------------------------------
# * import block# :
from i2c_rpi_driver import *


# ----------------------------------------------
# * Vars block :

#  ----------------------------------------------:
# * Commands list block :
A0 = [14, 0]
A1 = [14, 1]
A2 = [14, 2]
A3 = [14, 3]
A4 = [14, 4]
A5 = [14, 5]
A6 = [14, 6]
A7 = [14, 7]
           
B0 = [15, 0]
B1 = [15, 1]
B2 = [15, 2]
B3 = [15, 3]
B4 = [15, 4]
B5 = [15, 5]
B6 = [15, 6]
B7 = [15, 7]

#  ----------------------------------------------:
# * Port_drv_rpi: : 
class Port_drv_rpi:
# ** __init__ : 
   def __init__(self, i2c):
      self._i2c = i2c
      self._valueA = bytearray(8)
      self._valueB = bytearray(8)
      self._i2c.write_block_data(0,
                                [0])
      self._i2c.write_block_data(1,
                                [0])


#  ----------------------------------------------:
# ** def set(self, port, value): :
   def set(self, port, value):
       if port[0] == 14:
           self._valueA[port[1]] = value
           self._i2c.write_block_data(int(port[0]),
                                      [int(self._valueA.hex())])
       else:
           self._valueB[port[1]] = value
           self._i2c.write_block_data(int(port[0]),
                                      [int(self._valueB.hex())])


#  ----------------------------------------------:
# ** def is_on : 
   def value(self, num): 
       return self._valueA[num[1]] if num[0]==14 else self._valueB[num[1]]


#  ----------------------------------------------:
# * ----------------------------------------------:
