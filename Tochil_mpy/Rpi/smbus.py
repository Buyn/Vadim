I2CBUS =1

class SMBus:
   def __init__(self, port=I2CBUS):
      self.bus = port


   def write_byte(self, addr, cmd):
       pass

   def write_byte_data(self, addr, cmd, data):
       pass

   def write_block_data(self, addr, cmd, data):
       pass

   def read_byte(self, addr):
       pass

   def read_byte_data(self, addr, cmd):
       pass

   def read_block_data(self, addr, cmd):
       pass
