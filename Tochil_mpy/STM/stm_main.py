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
step_pin02 = pyb.Pin.cpu.B10
step_pin03 = pyb.Pin.cpu.B10
step_pin04 = pyb.Pin.cpu.B10
step_pin05 = pyb.Pin.cpu.A10
end_pin01 = pyb.Pin.cpu.B5
end_pin02 = pyb.Pin.cpu.B10
end_pin03 = pyb.Pin.cpu.B10
end_pin04 = pyb.Pin.cpu.B10
end_pin05 = pyb.Pin.cpu.A10
sm01 =  Step_Driver(step_pin01 , end_pin01)
sms = [ Step_Driver(step_pin01, end_pin01),
        Step_Driver(step_pin02, end_pin02),
        Step_Driver(step_pin03, end_pin03),
        Step_Driver(step_pin04, end_pin04),
        Step_Driver(step_pin05, end_pin05)
       ,]


#  ----------------------------------------------:
# * Commands list block :
CMD_STEPS = 10
CMD_HOMERUN = 100
DEV_STEPMOTOR01 = 10
DEV_STEPMOTOR02 = 11
DEV_STEPMOTOR03 = 12
DEV_STEPMOTOR04 = 13
DEV_STEPMOTOR05 = 14
DEV_SMS = range(DEV_STEPMOTOR01, DEV_STEPMOTOR05)

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
    if msg[1] in DEV_SMS:
        print("Step motor = {0}".format(msg[1]-10))
        step_motor_rutine(sms[msg[1]-10], msg[2], [msg[3], msg[4]])


#  ----------------------------------------------:
# * def step_motor_rutine(sm , cmd , data  ): : 
#  ----------------------------------------------:
def step_motor_rutine(sm, cmd, data):
    if cmd == CMD_STEPS:
        r = data[0]*256 + data[1]
        print("start {0} steps on Step motor".format(r))
        sm.step_on(r,100)
    if cmd == CMD_HOMERUN:
        r = data[0]*256 + data[1]
        print("start homerun")
        sm.homerun(timeout = r)


#  ----------------------------------------------:
# * __main__ : 
#  ----------------------------------------------:
if __name__ == "__main__":
    pass
# * ----------------------------------------------: