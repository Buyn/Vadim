# ----------------------------------------------
# * import block# :
import pyb, micropython, utime
from pyb import I2C
micropython.alloc_emergency_exception_buf(100)


# ----------------------------------------------
# * Vars block :
#  ----------------------------------------------:
SLAVE_ADDRESS = 0x40
PORT = 1
BAUDRATE = 100000
PINOUT01 =  pyb.Pin(pyb.Pin.cpu.C13, pyb.Pin.OUT)


#  ----------------------------------------------:
# * Commands list block :
#  ----------------------------------------------:
REG_GETMSGLST        = 0
REG_GETMSGONE        = 1
REG_CMD              = 5


# ----------------------------------------------
# *  class I2C_com :
# ----------------------------------------------
# ** class : 
class I2C_com(object):


# ----------------------------------------------
# ** def __init__ : 
# ----------------------------------------------
    def __init__(self, addr_=SLAVE_ADDRESS, port_=PORT, baudrate_=BAUDRATE):
        self.i2c = I2C(port_, I2C.SLAVE, addr=addr_, baudrate=baudrate_)
        self.pinOut01  = PINOUT01
        self.msg_list=[]
        self.cmd_list=[]


# ----------------------------------------------
# ** def print_in : 
    def print_in(self, byt = 1):
        while True:
            try:
                # data = i2c_slave.recv(4)
                data = self.i2c.recv(byt)
            except OSError as exc:
                if exc.args[0] not in (5, 110):
                    # 5 == EIO, occurs when master does a I2C bus scan
                    # 110 == ETIMEDOUT
                    print(exc)
            except KeyboardInterrupt:
                break
            else:
                print("RECV: %r" % data)
                self.i2c_exec(data)


# ----------------------------------------------
# ** def get_switch(self, byt = 4): : 
# ----------------------------------------------
    def get_switch(self, byt = 4):
        try:
          print("Start waiting byte")	
          data = self.i2c.recv(1)
        except OSError as exc:
          # if exc.args[0] not in (5, 110):
            # 5 == EIO, occurs when master does a I2C bus scan
            # 110 == ETIMEDOUT
            print("OSError in resiv get_switch", exc)
        else:
          if data == b'\x05':
            # print("Date =: %r" % data)
            return self.get_msg(4)
          if data == b'\x01':
            self.send_msg()
            print("Date = 1")
          if data == b'\x00':
            self.i2c_send(len(self.msg_list))
            print("Date = 0")
          else:
            print("RECV&SEND: %r" % data)


# ----------------------------------------------
# ** def get_msg(self, byt = 4): : 
# ----------------------------------------------
    def get_msg(self, byt = 4):
        try:
            # data = i2c_slave.recv(4)
            data = self.i2c.recv(byt)
        except OSError as exc:
            # if exc.args[0] not in (5, 110):
                # 5 == EIO, occurs when master does a I2C bus scan
                # 110 == ETIMEDOUT
            print("OSError get_msg:",exc)
            return False
        if not data:
            print("NO DATA" )
            return False
        self.cmd_list.append(data)
        self.i2c_send(len(self.msg_list))
        # print("RECV cmd:" , data)
        # print("cmd list size:" , len(self.cmd_list))
        return True


# ----------------------------------------------
# ** def i2c_send(snd = 0x40): : 
# ----------------------------------------------
    def i2c_send(self, snd):
      try:
        self.i2c.send(snd)
        # print("send = ", snd)
      except OSError as exc:
        if exc.args[0] == 5:
          print("EIO in send")
        if exc.args[0] == 110:
          print("ETIMEDOUT in send")
        # 5 == EIO, occurs when master does a I2C bus scan
        # 110 == ETIMEDOUT
        print(exc)


# ----------------------------------------------
# ** def add_msg(self, msg) : 
# ----------------------------------------------
    def add_msg(self, msg):
        self.msg_list.append(msg)


# ----------------------------------------------
# ** def send_msg(self): 
# ----------------------------------------------
    def send_msg(self):
        if len(self.msg_list) == 0 : return None
        msg = self.msg_list.pop(0)
        for var in msg:
          self.i2c_send(var)
        return msg


# ----------------------------------------------
# ** def rutin(): : 
# ----------------------------------------------
    def rutin(self):
        return None if len(self.cmd_list) == 0 else self.cmd_list.pop(0)


# ----------------------------------------------
