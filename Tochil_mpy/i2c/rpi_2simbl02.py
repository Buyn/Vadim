import smbus
from time import sleep

# i2c bus (0 -- original Pi, 1 -- Rev 2 Pi)
I2CBUS = 1

# LCD Address
ADDRESS = 0x40


bus = smbus.SMBus(I2CBUS)

class i2c_device:
   def __init__(self, addr, port=I2CBUS):
      self.addr = addr
      self.bus = smbus.SMBus(port)

# Write a single command
   def write_cmd(self, cmd):
      self.bus.write_byte(self.addr, cmd)
      sleep(0.0001)

# Write a command and argument
   def write_cmd_arg(self, cmd, data):
      self.bus.write_byte_data(self.addr, cmd, data)
      sleep(0.0001)

# Write a block of data
   def write_block_data(self, cmd, data):
      self.bus.write_block_data(self.addr, cmd, data)
      sleep(0.0001)

# Read a single byte
   def read(self):
      return self.bus.read_byte(self.addr)

# Read
   def read_data(self, cmd):
      return self.bus.read_byte_data(self.addr, cmd)

# Read a block of data
   def read_block_data(self, cmd):
      return self.bus.read_block_data(self.addr, cmd)

lcd_device = i2c_device(ADDRESS, 1)

while True:
      cmd = 0x08
      lcd_device.write_cmd(cmd)
      # write_block_data((cmd & 0xF0), 0xF0)
      print("send = ", cmd)
      sleep(2)
      cmd = 0x00
      lcd_device.write_cmd(cmd)
      print("send = ", cmd)
      sleep(2)
