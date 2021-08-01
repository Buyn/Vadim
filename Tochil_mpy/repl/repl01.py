import machine
# ----------------------
import pyb, machine
blue =pyb.Pin(pyb.Pin.cpu.C13, pyb.Pin.OUT)
blue =pyb.Pin(pyb.Pin.board.C13, pyb.Pin.OUT)
blue.off() # IS ON!!!!
blue.on() # IS OFF!!!!
blue.value(1) # IS ON!!!!
blue.value(0) # IS OFF!!!!
# ----------------------
from driver_m import *
# enc = encoder(pyb.Pin.board.PB4, pyb.Pin.board.PB5)
sd = Step_Driver(pyb.Pin.board.PB1)
sd = Step_Driver(pyb.Pin.board.PB1, 100)
sd = Step_Driver(pyb.Pin.board.PB1, 10)
sd = Step_Driver(pyb.Pin.board.PB13, 100)
from driver_m import *
sd = Step_Driver(pyb.Pin.board.PB13)
sd.step()
sd.step_on(200,500)
sd.pin.value(0)
sd.step_on(2000,50)
# ----------------------
from encoder import *
enc = encoder(pyb.Pin.board.PA4, pyb.Pin.board.PA3)
while True:
    if enc.have_data(): print (enc.get_data())
