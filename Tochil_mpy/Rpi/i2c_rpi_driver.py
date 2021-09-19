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


#  ----------------------------------------------:
# * i2c_device: : 
class i2c_device:
# ** __init__ : 
   def __init__(self, addr, port=I2CBUS):
      self.addr = addr
      self.port = port
      self.cmd_list = []
      self.bus = smbus2.SMBus(port)


#  ----------------------------------------------:
# **  Write a single command :
   def write_cmd(self, cmd):
      self.bus.write_byte(self.addr, cmd)
      sleep(0.0001)


#  ----------------------------------------------:
# **  Write a single command read result :
   def write_cmd_read(self, cmd):
      self.bus.write_byte(self.addr, cmd)
      sleep(0.0001)
      return self.bus.read_byte(self.addr)


#  ----------------------------------------------:
# **  Write a command and argument : 
   def write_cmd_arg(self, dev, cmd, data):
      with smbus2.SMBus(self.port) as bus:
          # Write a block of 8 bytes to address 80 from offset 0
          # data = [1, 2, 3, 4, 5, 6, 7, 8]
          # bus.write_i2c_block_data(80, 0, data)
          bus.write_i2c_block_data(self.addr, 5,
                        [dev, cmd, data[0], data[1]])


#  ----------------------------------------------:
# **  Write and read a command and argument : 
   def rdwr_cmd_arg(self, dev, cmd, data):
      # # Single transaction writing two bytes then read two at address 80
      write = smbus2.i2c_msg.write(self.addr, [5, dev, cmd, data[0], data[1]])
      read = smbus2.i2c_msg.read(self.addr, 1)
      with smbus2.SMBus(self.port) as bus:
          bus.i2c_rdwr(write, read)
          # return bus.i2c_rdwr(write, read)
          return list(read)
          # return bus.read_byte_data(self.addr, 0)

          
#  ----------------------------------------------:
# **  Write a block of data :
   def write_block_data(self, cmd, data):
      with smbus2.SMBus(self.port) as bus:
         self.bus.write_block_data(self.addr, cmd, data)


#  ----------------------------------------------:
# **  Read a single byte :
   def read(self):
      return self.bus.read_byte(self.addr)


#  ----------------------------------------------:
# **  Read :
   def read_data(self, cmd):
      while True:
         try:
            return self.bus.read_byte_data(self.addr, cmd)
         except OSError as exc:
            print("Timeout")


#  ----------------------------------------------:
# **  msg_list_size :
   def msg_list_size(self):
      with smbus2.SMBus(self.port) as bus:
         try:
            return self.bus.read_byte_data(self.addr, 0)
         except OSError as exc:
            print("Timeout")


#  ----------------------------------------------:
# **  Read a block of data :
   def read_block_data(self, cmd):
      return self.bus.read_block_data(self.addr, cmd)


#  ----------------------------------------------:
# **  Tow simbols send cicle :
   def send_2_simbol(self, cmd1, cmd2):
      while True:
         self.write_cmd(cmd1)
         # write_block_data((cmd & 0xF0), 0xF0)
         print("send = ", cmd1)
         sleep(2)
         self.write_cmd(cmd2)
         print("send = ", cmd2)
         sleep(2)


#  ----------------------------------------------:
# **  send simbols:
   def send_simbol(self, cmd1):
      print("get = ", cmd1)
      print("send = ", int(cmd1,0))
      self.write_cmd(int(cmd1,0))
      # write_block_data((cmd & 0xF0), 0xF0)


#  ----------------------------------------------:
# **  send resiv:
   def send_resiv(self, cmd1):
      print("get = ", cmd1)
      print("send = ", int(cmd1,0))
      result = self.write_cmd_read(int(cmd1,0))
      print ("get back = ", result)
      # write_block_data((cmd & 0xF0), 0xF0)


#  ----------------------------------------------:
# **  send and resiv Tow simbols cicle :
   def send_and_reiv_loop(self, cmd1, cmd2):
      while True:
         print("send = ", cmd1)
         self.write_cmd(cmd1)
         # write_block_data((cmd & 0xF0), 0xF0)
         tmp = self.read()
         print("resiv = ", tmp)
         sleep(2)
         print("send = ", cmd2)
         self.write_cmd(cmd2)
         tmp = self.read()
         print("resiv = ", tmp)
         sleep(2)


#  ----------------------------------------------:
# * ----------------------------------------------:
