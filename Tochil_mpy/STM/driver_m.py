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
CMD_STEPS       = 10
CMD_10KSTEPS    = 11
CMD_SET_OFFTIME = 20
CMD_SET_ONTIME  = 21
CMD_HOMERUN     = 100


#  ----------------------------------------------:
# * class Step_Driver(object): : 
# ** class : 
#  ----------------------------------------------:
class Step_Driver(object):


#  ----------------------------------------------:
# **    def __init__(self, pin, longs = 50): : 
#  ----------------------------------------------:
    def __init__(self, step_pin, end_pin, ontime = 100, offtime = 100):
        self.pin  = pyb.Pin(step_pin, pyb.Pin.OUT)
        self._end_pin  = pyb.Pin(end_pin, pyb.Pin.IN)
        # btn = machine.Pin(pyb.Pin.board.PB4, machine.Pin.IN)
        self._ontime= ontime
        self._offtime= offtime
        self._steps_left= 0
        # timer.callback(self.cb)


#  ----------------------------------------------:
# **    def step(self): : 
#  ----------------------------------------------:
    def step(self):
        self.pin.value(1)
        self._steps_left-=1
        utime.sleep_us(self._ontime)
        self.pin.value(0)


#  ----------------------------------------------:
# **    def step_on(self, steps, timeout): : 
#  ----------------------------------------------:
    def step_on(self, steps, offtime = None):
        if not offtime: offtime = self._offtime
        if self._steps_left<0: self._steps_left =0
        self._steps_left += steps
        while self._steps_left>0:
            # print(self._steps_left)    
            self.step()
            utime.sleep_us(offtime)


#  ----------------------------------------------:

# **    def homerun(self, timeout = 1000): : 
#  ----------------------------------------------:
    def homerun(self, timeout = 1000):
        while True:
            if not self._end_pin.value(): return
            self.step()
            utime.sleep_us(self._offtime)


#  ----------------------------------------------:
# **    def rutine(sm , cmd , data  ): : 
#  ----------------------------------------------:
    def rutine(self, cmd, data):
        r = self.sum_byte(data)
        if cmd == CMD_STEPS:
            print("start {0} steps on Step motor".format(r))
            self.step_on(r)
        if cmd == CMD_10KSTEPS:
            r= r*10000
            print("start {0} k_steps on Step motor".format(r))
            self.step_on(r)
        if cmd == CMD_HOMERUN:
            print("start homerun")
            self.homerun(timeout = r)
        if cmd == CMD_SET_OFFTIME:
            print("set offtime = ", r)
            self._offtime = r
        if cmd == CMD_SET_ONTIME:
            print("set ontime = ", r)
            self._ontime = r


#  ----------------------------------------------:
# ** def sum_byte(self, data) : 
#  ----------------------------------------------:
    def sum_byte(self, data):
            return  data[0]*256 + data[1]


#  ----------------------------------------------:


# ** ----------------------------------------------:
# * ----------------------------------------------:
