# * imports : 
import sys
from i2c_rpi_driver import *

# * vars :
stm = i2c_device(0x40, 1)

# * main :
def main(argv):
# ** start : 
    print ("start")
    print (argv)
# ** i2c_2s : 
    if argv[1] == "i2c_2s":
        print ("start i2c 2simbol rutin")
        print ("with defalt params")
        stm.send_2_simbol(argv[2], argv[3])
# ** i2c_s : 
    if argv[1] == "i2c_s":
        print ("start i2c 2simbol rutin")
        stm.send_simbol(argv[2])
# ** i2c_b : 
    if argv[1] == "i2c_b":
        print ("start i2c block rutin")
        stm.write_block_data(int(argv[2], 0), [int(argv[3], 0), int(argv[4], 0)])
# ** i2c_bio : 
    if argv[1] == "i2c_bio":
        print ("start i2c block in and out")
        stm.write_block_data(int(argv[2], 0), (int(argv[3], 0)))
        result = stm.read_byte_data(1)
        print("result = ", result)
# ** i2c_sio : 
    if argv[1] == "i2c_sio":
        print ("start i2c simbol in and ruturn")
        stm.send_resiv(argv[2])
# ** "i2c_sar_l" : 
    if argv[1] == "i2c_sar_l":
        print ("start i2c 2simbol rutin")
        print ("with defalt params")
        # stm.send_and_reiv_loop(10, 13)
        stm.send_and_reiv_loop(0x00, 0x08)
# ** diod control: 
    if argv[1] == "diod":
      print ("start diod control")
# *** on : 
      if argv[2] == "on":
        print ("set to loop")
        # stm.send_and_reiv_loop(10, 13)
        print ("set to on")
        stm.write_cmd(0x10)
# *** off : 
      if argv[2] == "off":
        print ("set to loop")
        # stm.send_and_reiv_loop(10, 13)
        print ("set to off")
        stm.write_cmd(0x13)
# *** loop : 
      if argv[2] == "loop":
        print ("set to loop")
        # stm.send_and_reiv_loop(10, 13)
        stm.send_2_simbol(0x10, 0x13)
# ** end : 
    print ("end")

# * if __name__ : 
if __name__ == "__main__": 
    import sys
    # sys.argv = ['', 'Test.testName']
    main(sys.argv)


