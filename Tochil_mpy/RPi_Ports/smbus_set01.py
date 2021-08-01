# * import :
import smbus
import time
 
#bus = smbus.SMBus(0) # Rev 1 Pi
bus = smbus.SMBus(1) # Rev 2 Pi
 
DEVICE = 0x20 # Device Adresse (A0-A2)
IODIRA = 0x00 # Pin Register fuer die Richtung
IODIRB = 0x01 # Pin Register fuer die Richtung
OLATA = 0x14 # Register OUTPUT (GPA)
OLATB = 0x15 # Register OUTPUT (GPB)
REDA  = 0x14 # Register OUTPUT (GPA)
GREENB= 0x15 # Register OUTPUT (GPA)
OLATB = 0x15 # Register OUTPUT (GPB)
GPIOA = 0x12 # Register fuer Eingabe (GPA)
 
# Define GPA pin 7 as input (10000000 = 0x80)
# Binary: 0 means output, 1 means input
bus.write_byte_data(DEVICE,IODIRA,0x00)
 
# Define all GPB pins as output (00000000 = 0x00)
bus.write_byte_data(DEVICE,IODIRB,0x00)
 
# Set all 7 output bits to 0
bus.write_byte_data(DEVICE,OLATB,0)
 
# Function that makes all LEDs light up.
def setallon(port):
    # set all pins on 1111 1111 = 0xFF = 255
    # green on 1000 0000 = 0x80 = 128
    bus.write_byte_data(DEVICE, port, 0xFF)

# Function that makes all LEDs light off.
def setalloff(port):
    # set all pins on 00000000  = 0x00 = 0
    bus.write_byte_data(DEVICE, port, 0x00)
 
# Endless loop waiting at the push of a button
while True:
    # Read status of GPIOA register
    print("set Gree on")
    setallon(GREENB)
    time.sleep(3)
    print("set Ylou on")
    setallon(REDA)
    time.sleep(3)
    print("set Red on")
    setalloff(GREENB)
    time.sleep(3)
    print("set ALL on")
    setalloff(REDA)
    time.sleep(3)
