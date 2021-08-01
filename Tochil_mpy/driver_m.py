import pyb, micropython, utime
micropython.alloc_emergency_exception_buf(100)

class Step_Driver(object):
    def __init__(self, pin, longs = 500):
        self.pin  = pyb.Pin(pin, pyb.Pin.OUT)
        self.longs= longs
        # timer.callback(self.cb)


    def step(self):
        self.pin.value(0)
        utime.sleep_us(self.longs)
        self.pin.value(1)


    def step_on(self, steps, timeout):
        for step in range(steps):
            # print(step)    
            self.step()
            utime.sleep_us(timeout)

