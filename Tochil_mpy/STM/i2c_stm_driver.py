# ----------------------------------------------
# * import block# :
import pyb, micropython, utime
from pyb import I2C
micropython.alloc_emergency_exception_buf(100)

# ----------------------------------------------
# * Vars block :
SLAVE_ADDRESS = 0x40
PORT = 1
BAUDRATE = 100000
PINOUT01 =  pyb.Pin(pyb.Pin.cpu.C13, pyb.Pin.OUT)


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
# ** def get_msg(self, byt = 5): : 
# ----------------------------------------------
    def get_msg(self, byt = 5):
        try:
            # data = i2c_slave.recv(4)
            data = self.i2c.recv(byt)
        except OSError as exc:
            if exc.args[0] not in (5, 110):
                # 5 == EIO, occurs when master does a I2C bus scan
                # 110 == ETIMEDOUT
                print(exc)
            return False
        if not data:
            print("NO DATA" )
            return False
        print("RECV:" , data)
        print("str - " , isinstance(data, bytes))
        self.msg_list.append(data)
        return True


# ----------------------------------------------
# ** def rutin(): : 
# ----------------------------------------------
    def rutin(self):
        return None if len(self.msg_list) == 0 else self.msg_list.pop(0)


# ----------------------------------------------
# ** def i2c_2s_send : 
    def i2c_2s_send(self, byt =5):
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
                # self.i2c.send(data)
                self.i2c.send(0x40)
                print("RECV&SEND: %r" % data)



# ** def i2c_exec : 
    def i2c_exec(self, data):
        if data == b'\x13' : 
            self.pinOut01.value(0)
            print("dion off")
        elif data == b'\x10' : 
            self.pinOut01.value(1)
            print("dion on")


# ** def i2c_pinset(value) : 
    def i2c_pinset(self, value):
        print("dion on")
        self.pinOut01.value(value)


# ** def diode_com : 
    def diode_com(self):
        while True:
            try:
                # data = i2c_slave.recv(4)
                data = self.i2c.recv(1)
            except OSError as exc:
                if exc.args[0] not in (5, 110):
                    # 5 == EIO, occurs when master does a I2C bus scan
                    # 110 == ETIMEDOUT
                    print(exc)
            except KeyboardInterrupt:
                break
            else:
                print("RECV: %r" % data)
                print("RECV: ", data)
                self.i2c_exec(data)

