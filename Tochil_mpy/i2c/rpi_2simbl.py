import smbus
from time import sleep

# i2c bus (0 -- original Pi, 1 -- Rev 2 Pi)
I2CBUS = 1

# LCD Address
ADDRESS = 0x40

bus = smbus.SMBus(I2CBUS)

# Write a single command
def write_cmd( cmd):
  bus.write_byte(ADDRESS, cmd)
  sleep(0.0001)

# Write a command and argument
def write_cmd_arg( cmd, data):
  bus.write_byte_data(ADDRESS, cmd, data)
  sleep(0.0001)

# Write a block of data
def write_block_data( cmd, data):
      bus.write_block_data(ADDRESS, cmd, data)
      sleep(0.0001)

while True:
      # cmd = 0x03
      cmd = 0x13
      write_cmd((cmd & 0xF0))
      print("send = ", cmd)
      sleep(1)
      cmd = 0x13
      write_cmd(cmd(cmd << 4) & 0xF0)
      print("send = ", cmd)
      sleep(1)
