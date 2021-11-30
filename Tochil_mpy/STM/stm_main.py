# ----------------------------------------------
# * import block# :
#  ----------------------------------------------:
from i2c_stm_driver import *
from driver_m import *
from stm_encod import *
import utime


# ----------------------------------------------
# * Vars block :
runing = False
# scl1 = PB6
# sda1 = PB7
i2cpin01 = pyb.Pin.cpu.B6
# i2cpin01 = pyb.Pin.cpu.B7
#  ----------------------------------------------:
# ** Pins :
#  ----------------------------------------------:
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
enc_pin01 = pyb.Pin.board.PB2
enc_pin02 = pyb.Pin.board.PB10
#  ----------------------------------------------:
# ** Devices :
#  ----------------------------------------------:
rpi = I2C_com()
sm01 =  Step_Driver(step_pin01 , end_pin01)
sms = [ Step_Driver(step_pin01, end_pin01),
        Step_Driver(step_pin02, end_pin02),
        Step_Driver(step_pin03, end_pin03),
        Step_Driver(step_pin04, end_pin04),
        Step_Driver(step_pin05, end_pin05)
       ,]
encoder = Encoder(enc_pin01, enc_pin02)


#  ----------------------------------------------:
# * Commands list block :
DEV_STEPMOTOR01 = 10
DEV_STEPMOTOR02 = 11
DEV_STEPMOTOR03 = 12
DEV_STEPMOTOR04 = 13
DEV_STEPMOTOR05 = 14
DEV_SMS = range(DEV_STEPMOTOR01, DEV_STEPMOTOR05)
DEV_ENCODER     = 20


#  ----------------------------------------------:
# * mainloop :
#  ----------------------------------------------:
# async def mainloop(test = False):
def mainloop(test=False):
    while (True):
        if rpi.get_switch() and len(rpi.cmd_list) > 0:
            cmd_rutin(rpi.rutin())
        # utime.sleep_us(1000)
        if test:
            return True


#  ----------------------------------------------:
# * def cmd_rutin(msg) :
#  ----------------------------------------------:
def cmd_rutin(msg):
    if msg[0] in DEV_SMS:
        print("Step motor = {0}".format(msg[0]-10))
        # step_motor_rutine(sms[msg[0]-10], msg[1], [msg[2], msg[3]])
        sms[msg[0]-10].rutine(msg[1], [msg[2], msg[3]])
    if msg[0] == DEV_ENCODER:
        print("Encoder code = {0}".format(msg[0]))
        # rpi.add_msg([20, *encoder.rutine(msg[1], [msg[2], msg[3]])])
        r = encoder.rutine(msg[1], [msg[2], msg[3]])
        rpi.add_msg([20, r[0], r[1], r[2]])


#  ----------------------------------------------:
# * def t_find_pin :
#  ----------------------------------------------:
def t_find_pin():
    global runing
    pin01 = pyb.Pin(i2cpin01, pyb.Pin.IN)
    # pin01.irq(trigger=pyb.Pin.IRQ_RISING | pyb.Pin.IRQ_FALLING, handler=call_test)
    # pin01.irq(trigger=pyb.Pin.IRQ_FALLING, handler=call_test)
    pin01.irq(trigger=pyb.Pin.IRQ_RISING, handler=call_test)
    print("", )
    return True


#  ----------------------------------------------:
# * def call_test(p): :
#  ----------------------------------------------:
def call_test(p):
    global runing
    if runing:
        print("alredy run")
        return
    ts1 = utime.ticks_cpu()
    runing = True
    rutin_one()
    ts2 = utime.ticks_cpu()
    runing = False
    print("end call start= {0:}, end= {1:} ".format(ts1, ts2))


#  ----------------------------------------------:
# t_find_pin()
#  ----------------------------------------------:
# * rurin_one :
#  ----------------------------------------------:
# async def rutin_one():
def rutin_one():
    # print("rutin start", )
    # print("rutin run", )
    if rpi.get_switch() and len(rpi.cmd_list) > 0:
        cmd_rutin(rpi.rutin())
    # utime.sleep_us(1000)
    # print("rutin end", )


#  ----------------------------------------------:
# * __main__ :
#  ----------------------------------------------:
if __name__ == "__main__":
    pass
# * ----------------------------------------------:
