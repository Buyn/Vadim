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
step_pin02 = pyb.Pin.cpu.B14
step_pin03 = pyb.Pin.cpu.B15
step_pin04 = pyb.Pin.cpu.A8 #A
step_pin05 = pyb.Pin.cpu.A10
end_pin01 = pyb.Pin.cpu.B5
end_pin02 = pyb.Pin.cpu.B9
end_pin03 = pyb.Pin.cpu.B8
end_pin04 = pyb.Pin.cpu.B1 #A
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
CMD_STEPS       = 10
CMD_10KSTEPS    = 11
CMD_SET_OFFTIME = 20
CMD_SET_ONTIME  = 21
CMD_HOMERUN     = 100

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
       if rpi.get_switch() and len(rpi.msg_list)>0:
           cmd_rutin(rpi.rutin())
       if test: return True


#  ----------------------------------------------:
# * def cmd_rutin(msg) : 
#  ----------------------------------------------:
def cmd_rutin(msg):
    if msg[0] in DEV_SMS:
        print("Step motor = {0}".format(msg[0]-10))
        step_motor_rutine(sms[msg[0]-10], msg[1], [msg[2], msg[3]])


#  ----------------------------------------------:
# * def step_motor_rutine(sm , cmd , data  ): : 
#  ----------------------------------------------:
def step_motor_rutine(sm, cmd, data):
    if cmd == CMD_STEPS:
        r = data[0]*256 + data[1]
        print("start {0} steps on Step motor".format(r))
        sm.step_on(r)
    if cmd == CMD_HOMERUN:
        r = data[0]*256 + data[1]
        print("start homerun")
        sm.homerun(timeout = r)
    if cmd == CMD_SET_OFFTIME:
        r = data[0]*256 + data[1]
        print("set offtime = ", r)
        sm._offtime = r
    if cmd == CMD_SET_ONTIME:
        r = data[0]*256 + data[1]
        print("set ontime = ", r)
        sm._ontime = r


#  ----------------------------------------------:
# * __main__ : 
#  ----------------------------------------------:
if __name__ == "__main__":
    pass
# * ----------------------------------------------:
