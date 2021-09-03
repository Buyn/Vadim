# ----------------------------------------------
# * import block# :

# ----------------------------------------------
# * Vars block :


#  ----------------------------------------------:
# * i2c_device: : 
class stepmotor_rpi_driver:
# ** __init__ : 
   def __init__(self, addr, port=I2CBUS):
      self.addr = addr
      self.port = port
      self.bus = smbus2.SMBus(port)


#  ----------------------------------------------:
# **  Write a single command :
   def write_cmd(self, cmd):
      self.bus.write_byte(self.addr, cmd)
      sleep(0.0001)


#  ----------------------------------------------:
# * ----------------------------------------------:
