# ##############################################
# ==============================================
# * import block * # :
# ==============================================
import pyb, utime
import micropython
micropython.alloc_emergency_exception_buf(100)


# ==============================================
# ==============================================
# * Vars block * # :
# ==============================================


# ==============================================
# * Commands list block * # :
# ==============================================


# ==============================================
# * class Ecoder * # :
# ** ======= class =============================:
class Encoder:


# ----------------------------------------------
# ** def __init__(self, pin01, pin02, timeout = 500): : 
# ----------------------------------------------:
    def __init__(self, pin01, pin02, timeout = 500):
        self.pin01  = pyb.Pin(pin01, pyb.Pin.IN)
        self.pin02  = pyb.Pin(pin02, pyb.Pin.IN)
        self.counter3 = 0
        self.last_count = 0;
        # btn = machine.Pin(pyb.Pin.board.PB4, machine.Pin.IN)
        self.pin01.irq(trigger=pyb.Pin.IRQ_RISING | pyb.Pin.IRQ_FALLING, handler=self.callback_pin01)
        # IRQ_RISING_FALLING = "IRQ_FALLING"
        self.pin02.irq(trigger=pyb.Pin.IRQ_RISING | pyb.Pin.IRQ_FALLING, handler=self.callback_pin02)
        self.timeout= timeout
        self.sensor_time = 0
        self.reset_time()
        # timer.callback(self.cb)


#  ----------------------------------------------:
# ** def callback_pin01(self, p): : 
#  ----------------------------------------------:
    def callback_pin01(self, p):
        if self.pin01.value() :
            # print("Pin01 true")
            if self.pin02.value() : self.counter3 -= 1
            else: self.counter3 += 1
        else:
            # print("Pin01 false")
            if self.pin02.value() : self.counter3 += 1
            else: self.counter3 -= 1
            

#  ----------------------------------------------:
# ** def callback_pin02(self, p): : 
#  ----------------------------------------------:
    def callback_pin02(self, p):
        if self.pin02.value():
            if self.pin01.value() : self.counter3 += 1
            else: self.counter3 -= 1
        else:
            if (self.pin02.value() == 1): self.counter3 -= 1
            else: self.counter3 += 1


#  ----------------------------------------------:
# ** def get_data(self): : 
#  ----------------------------------------------:
    def get_data(self):
        self.reset_time()
        self.last_count = self.counter3
        return self.counter3


#  ----------------------------------------------:
# ** def have_data(self): : 
#  ----------------------------------------------:
    def have_data(self):
        if utime.ticks_diff( self.sensor_time, utime.ticks_ms) <= 0 and self.last_count != self.counter3: return True
        else: return False


#  ----------------------------------------------:


# ** def reset_time(self): : 
#  ----------------------------------------------:
    def reset_time(self):
        self.sensor_time = utime.ticks_add(utime.ticks_ms(), self.timeout)


#  ----------------------------------------------:
# ** ============================================
# * ############################################ :
