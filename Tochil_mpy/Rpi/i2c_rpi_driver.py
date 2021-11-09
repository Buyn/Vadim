# ----------------------------------------------
# * import block# :
import smbus2
# from smbus2 import SMBus, i2c_msg
from time import sleep

# ----------------------------------------------
# * Vars block :
# i2c bus (0 -- original Pi, 1 -- Rev 2 Pi)
I2CBUS = 1

# LCD Address
ADDRESS = 0x40


# * Commands list block :
REG_GETMSGLST        = 0
REG_GETMSGONE        = 1
REG_CMD              = 5

#  ----------------------------------------------:
#  ----------------------------------------------:
# * i2c_device: : 
class i2c_device:
# ** __init__ : 
   def __init__(self, addr, port=I2CBUS):
      self.addr = addr
      self.port = port
      self.msg_list = []
      self.cmd_list = []
      self.bus = smbus2.SMBus(port)


#  ----------------------------------------------:
# **  Write a single command :
   def write_cmd(self, rgst, data):
      with smbus2.SMBus(self.port) as bus:
          bus.write_byte_data(self.addr, rgst, data)


#  ----------------------------------------------:
# **  Write a single command read result :
   def write_cmd_read(self, cmd):
      with smbus2.SMBus(self.port) as bus:
        self.bus.write_byte(self.addr, cmd)
        sleep(0.0001)
        return self.bus.read_byte(self.addr)


#  ----------------------------------------------:
# **  Write a command and argument : 
   def write_cmd_arg(self, dev, cmd, data, reg = REG_CMD):
      with smbus2.SMBus(self.port) as bus:
         try:
            bus.write_byte(self.addr, reg)
            bus.write_i2c_block_data(self.addr, dev,
                          [cmd, data[0], data[1]])
            return bus.read_byte(self.addr)
         except OSError as exc:
            print(exc)


#  ----------------------------------------------:
# **  msg_list_size :
   def msg_list_size(self, reg = REG_GETMSGLST):
      with smbus2.SMBus(self.port) as bus:
         try:
            bus.write_byte(self.addr, reg)
            return bus.read_byte(self.addr)
         except OSError as exc:
            if exc.args[0]==121:
              print("stm is busy or lost", exc.args[0])
              print("waiting...")
              sleep(1)
            else:    
              print(exc)


#  ----------------------------------------------:
# **  msg_get_one :
   def msg_get_one(self, reg = REG_GETMSGONE, lengs = 4):
      with smbus2.SMBus(self.port) as bus:
         try:
            bus.write_byte(self.addr, reg)
            result = [bus.read_byte(self.addr) for i in range(lengs)]
            self.msg_list.append(result)
            return result 
         except OSError as exc:
            print(exc)


#  ----------------------------------------------:
# * ----------------------------------------------:
