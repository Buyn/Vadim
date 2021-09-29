# ----------------------------------------------
# * import block# :
from i2c_rpi_driver import *
from bitman import *


# ----------------------------------------------
# * Vars block :


#  ----------------------------------------------:
# * Commands list block :
IODIRA = 0x00
IODIRB = 0x01
OLATA  = 0x14
OLATB  = 0x15
GPIOA  = 0x12

ON     = True
OFF    = False

A0 = [OLATA, 0]
A1 = [OLATA, 1]
A2 = [OLATA, 2]
A3 = [OLATA, 3]
A4 = [OLATA, 4]
A5 = [OLATA, 5]
A6 = [OLATA, 6]
A7 = [OLATA, 7]
           
B0 = [OLATB, 0]
B1 = [OLATB, 1]
B2 = [OLATB, 2]
B3 = [OLATB, 3]
B4 = [OLATB, 4]
B5 = [OLATB, 5]
B6 = [OLATB, 6]
B7 = [OLATB, 7]

#  ----------------------------------------------:
# * Port_drv_rpi: : 
class Port_drv_rpi:
# ** __init__ : 
   def __init__(self, i2c):
      self._i2c = i2c
      self._valueA = Bitman(8)
      self._valueB = Bitman(8)
      self._i2c.write_cmd(IODIRA, 0x00)
      self._i2c.write_cmd(IODIRB, 0x00)
      self.setport(A6, ON)
      self.setport(B0, ON)
      self.setport(B1, ON)
      self.setport(B2, ON)
      self.setport(B3, ON)
      self.setport(B4, ON)
      self.setport(B5, ON)


#  ----------------------------------------------:
# ** def setport(self, port, value): :
   def setport(self, port, value):
      base = self._valueA if port[0] == OLATA else self._valueB
      if base[port[1]] == value : return value
      base[port[1]] = value
      # print("set self._valueA =", self._valueA._value)
      # print("set self._valueA =", self._valueB._value)
      # self._valueA[port[1]] = value
      # self._i2c.write_block_data(int(port[0]),
      #                            [int(self._valueA.hex())])
      self._i2c.write_cmd(int(port[0]), base())
      # print(int(port[0]), base())
      return not value


#  ----------------------------------------------:
# ** def value(self, num):  : 
   def value(self, num): 
      return self._valueA[num[1]] if num[0]==OLATA else self._valueB[num[1]]


# * ----------------------------------------------:
