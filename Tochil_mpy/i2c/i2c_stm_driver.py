import pyb, micropython, utime
from pyb import I2C
micropython.alloc_emergency_exception_buf(100)

SLAVE_ADDRESS = 0x40
PORT = 1
BAUDRATE = 100000
PINOUT01 =  pyb.Pin(pyb.Pin.cpu.C13, pyb.Pin.OUT)

# *  class I2C_com :
class I2C_com(object):
# ** def __init__ : 


    def __init__(self, addr_=SLAVE_ADDRESS, port_=PORT, baudrate_=BAUDRATE):
        self.i2c = I2C(port_, I2C.SLAVE, addr=addr_, baudrate=baudrate_)
        self.pinOut01  = PINOUT01


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


# ** def print_in_out : 
    def print_in_out(self, byt = 1):
        while True:
            try:
                # data = i2c_slave.recv(4)
                data = self.i2c.recv(byt)
                self.i2c.send(data)
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



# ** def i2c_2s_send : 
    def i2c_2s_send(self):
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

