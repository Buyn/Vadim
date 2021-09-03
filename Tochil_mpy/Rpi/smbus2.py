I2CBUS =1
LAST_ADR =0
LAST_CMD =0
LAST_DATA =0

class SMBus:
   def __init__(self, port=I2CBUS):
      self.bus = port


   def write_byte(self, addr, cmd):
       pass

   def write_byte_data(self, addr, cmd, data):
       pass

   def write_block_data(self, addr, cmd, data):
       pass

   def write_i2c_block_data (self, adr, offset, data):
      LAST_ADR = adr
      LAST_DATA = data
      print("adr = {}; data =".format(adr), data )

   def __enter__(self):
       return self

   def __exit__(self, type, value, tb):
       pass 

   def read_byte(self, addr):
       return addr

   def read_byte_data(self, addr, cmd):
       return cmd

   def read_block_data(self, addr, cmd):
       return cmd
