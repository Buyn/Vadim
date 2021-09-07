# ----------------------------------------------
# * import block# :
#  ----------------------------------------------:
from i2c_stm_driver import *
from driver_m import *


# ----------------------------------------------
# * Vars block :
#  ----------------------------------------------:
rpi = I2C_com()
step_pin01 = pyb.Pin.cpu.B13
sm01 = Step_Driver(step_pin01)


#  ----------------------------------------------:
# * Commands list block :
CMD_STEPS = 10
DEV_STEPMOTOR01 = 1

#  ----------------------------------------------:
# * mainloop : 
#  ----------------------------------------------:
def mainloop(test = False):
    while (True):
       if rpi.get_msg() and len(rpi.msg_list)>0:
           cmd_rutin(rpi.rutin())
       if test: return True


#  ----------------------------------------------:
# * def cmd_rutin(msg) : 
#  ----------------------------------------------:
def cmd_rutin(msg):
    if msg[1] == 1:
        # r = int.from_bytes([msg[3],msg[4]], "big") 
        print(msg[3])
        print (msg[4])
        # r = int(str(msg[3]) +str(msg[4]))
        r = msg[3]*256 + msg[4]
        # r = msg[3]
        print("start Step motor on steps = ", r)
        sm01.step_on(r,100)


#  ----------------------------------------------:
# * __main__ : 
#  ----------------------------------------------:
if __name__ == "__main__":
    pass
# * ----------------------------------------------:
