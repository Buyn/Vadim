# ----------------------------------------------
# * import block# :
from i2c_rpi_driver import *


# ----------------------------------------------
# * Vars block :

#  ----------------------------------------------:
# * Commands list block :
A0 = [0x14, 0]
A1 = [0x14, 1]
A2 = [0x14, 2]
A3 = [0x14, 3]
A4 = [0x14, 4]
A5 = [0x14, 5]
A6 = [0x14, 6]
A7 = [0x14, 7]
           
B0 = [0x15, 0]
B1 = [0x15, 1]
B2 = [0x15, 2]
B3 = [0x15, 3]
B4 = [0x15, 4]
B5 = [0x15, 5]
B6 = [0x15, 6]
B7 = [0x15, 7]

#  ----------------------------------------------:
# * Port_drv_rpi: : 
class Port_drv_rpi:
# ** __init__ : 
   def __init__(self, i2c):
      self._i2c = i2c
      self._valueA = bytearray(8)
      self._valueB = bytearray(8)
      self._i2c.write_block_data(0x00, [0x00])
      self._i2c.write_block_data(0x01, [0x00])


#  ----------------------------------------------:
# ** def set(self, port, value): :
   def set(self, port, value):
       if port[0] == 0x14:
           self._valueA[port[1]] = value
           # self._i2c.write_block_data(int(port[0]),
           #                            [int(self._valueA.hex())])
           self._i2c.write_cmd(int(port[0]),
                                      int(self._valueA.hex()))
           print(int(port[0]), int(self._valueA.hex()))
       else:
           self._valueB[port[1]] = value
           # self._i2c.write_block_data(int(port[0]),
           #                            [int(self._valueB.hex())])
           self._i2c.write_cmd(int(port[0]),
                                      int(self._valueB.hex()))
           print(int(port[0]), int(self._valueB.hex()))


#  ----------------------------------------------:
# ** def value(self, num):  : 
   def value(self, num): 
       return self._valueA[num[1]] if num[0]==14 else self._valueB[num[1]]


#  ----------------------------------------------:
# * ----------------------------------------------:
