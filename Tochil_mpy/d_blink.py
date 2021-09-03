# ----------------------------------------------
# * import block# :
import utime
from driver_m import *
# ----------------------------------------------


# * defines: : 
step_pins = [
    pyb.Pin.cpu.B13,
    pyb.Pin.cpu.B10,
    ]
sms =[Step_Driver(pin) for pin in step_pins]
timeout = 100
maxcount = 1000
diod = pyb.Pin(pyb.Pin.cpu.C13, pyb.Pin.OUT)
diod_status = False
counter = 0
# ----------------------------------------------


# * def mainloop(): : 
def mainloop():
    global diod_status, counter
    while True:
        for sm in sms:
            sm.step()
            counter +=1
        if counter >= maxcount:
            diod.value(diod_status)
            diod_status = not diod_status
            counter = 0
            # return counter
        utime.sleep_us(timeout)
# ----------------------------------------------


# * def testloop(): : 
def testloop():
    global diod_status, counter
    while True:
        for sm in sms:
            sm.step()
            counter +=1
        if counter >= maxcount:
            diod.value(diod_status)
            diod_status = not diod_status
            # counter = 0
            return counter
        utime.sleep_us(timeout)
# ----------------------------------------------


# * if "__main__" : 
if __name__ == "__main__":
    mainloop()


# * ----------------------------------------------:
