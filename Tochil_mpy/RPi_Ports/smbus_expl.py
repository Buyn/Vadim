import smbus
import time
 
#bus = smbus.SMBus(0) # Rev 1 Pi
bus = smbus.SMBus(1) # Rev 2 Pi
 
DEVICE = 0x20 # Device Adresse (A0-A2)
IODIRA = 0x00 # Pin Register fuer die Richtung
IODIRB = 0x01 # Pin Register fuer die Richtung
OLATB = 0x15 # Register fuer Ausgabe (GPB)
GPIOA = 0x12 # Register fuer Eingabe (GPA)
 
# Define GPA pin 7 as input (10000000 = 0x80)
# Binary: 0 means output, 1 means input
bus.write_byte_data(DEVICE,IODIRA,0x80)
 
# Define all GPB pins as output (00000000 = 0x00)
bus.write_byte_data(DEVICE,IODIRB,0x00)
 
# Set all 7 output bits to 0
bus.write_byte_data(DEVICE,OLATB,0)
 
# Function that makes all LEDs light up.
def aufleuchten():
    for MyData in range(1,8):
        # Count from 1 to 8, which is binary
        # from 001 to 111.
        bus.write_byte_data(DEVICE,OLATB,MyData)
        print "Zahl:", MyData, "Binaer:", '{0:08b}'.format(MyData)
        time.sleep(1)
        # Reset all pins to 0 again
        bus.write_byte_data(DEVICE,OLATB,0)
 
# Endless loop waiting at the push of a button
while True:
    # Read status of GPIOA register
    Taster = bus.read_byte_data(DEVICE,GPIOA)
 
    if Taster & 0b10000000 == 0b10000000:
        print "Taster gedrueckt"
        aufleuchten()
