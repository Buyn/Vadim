# ----------------------------------------------
# * import block# :
import pyb, micropython, utime
micropython.alloc_emergency_exception_buf(100)


# ----------------------------------------------
# * Vars block :
#  ----------------------------------------------:
TIMEOUT = 10
#  ----------------------------------------------:
# * Commands list block :
#  ----------------------------------------------:

#  ----------------------------------------------:
# * class Step_Driver(object): : 
# ** class : 
#  ----------------------------------------------:
class Step_Driver(object):


#  ----------------------------------------------:
# **     def __init__(self, pin, longs = 50): : 
#  ----------------------------------------------:
    def __init__(self, step_pin, end_pin, longs = 100):
        self.pin  = pyb.Pin(step_pin, pyb.Pin.OUT)
        self._end_pin  = pyb.Pin(end_pin, pyb.Pin.IN)
        # btn = machine.Pin(pyb.Pin.board.PB4, machine.Pin.IN)
        self.longs= longs
        self.offtime= 100
        # timer.callback(self.cb)


#  ----------------------------------------------:
# **     def step(self): : 
#  ----------------------------------------------:
    def step(self):
        self.pin.value(1)
        utime.sleep_us(self.longs)
        self.pin.value(0)


#  ----------------------------------------------:
# **     def step_on(self, steps, timeout): : 
#  ----------------------------------------------:
    def step_on(self, steps, timeout = self.offtime):
        for step in range(steps):
            # print(step)    
            self.step()
            utime.sleep_us(timeout)


#  ----------------------------------------------:

# **     def homerun(self, timeout = 1000): : 
#  ----------------------------------------------:
    def homerun(self, timeout = 1000):
        while True:
            if not self._end_pin.value(): return
            self.step()
            utime.sleep_us(TIMEOUT)


#  ----------------------------------------------:
