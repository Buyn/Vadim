# * imports : 
import sys
from i2c_rpi_driver import *
from stepmotor_rpi_driver import *
from Port_drv_rpi import *
from AbSm_rpi import *

# * vars :
stm = i2c_device(0x40, 1)
sm1 = stepmotor_rpi_driver(i2c_device(0x40, 1), 10)
port = Port_drv_rpi( i2c_device(0x20))
absm = AbSm_rpi(stepmotor_rpi_driver(i2c_device(0x40), 10),
                 B0, A0, 100000)
absmm = [   AbSm_rpi(stepmotor_rpi_driver(i2c_device(0x40), 1),
                      B0, A0, 100000),
            AbSm_rpi(stepmotor_rpi_driver(i2c_device(0x40), 2),
                      B0, A0, 100000),
            AbSm_rpi(stepmotor_rpi_driver(i2c_device(0x40), 3),
                      B0, A0, 100000),
         ]
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
# ** sm1 : 
    if argv[1] == "sm1":
        print ("send step motor command")
        sm1.steps(int(argv[2]))
# ** portA : 
    if argv[1] == "portA":
        print ("send command to portA", argv[2])
        port.set([14, int(argv[2])], int(argv[3]))
# ** portB : 
    if argv[1] == "portB":
        print ("send command to portA", argv[2])
        port.set([15, int(argv[2])], int(argv[3]))
# ** absm : 
    if argv[1] == "absm":
        print ("send command to absolute step motor pos =", argv[2])
        if argv[2] == "pos":
            print ("pos =", argv[3])
            absm.move_to_pos(int(argv[3]))
        if argv[2] == "actv":
            print ("is_activ_dir_is_forward =", argv[3])
            absm.is_activ_dir_is_forward(int(argv[3]))
        if argv[2] == "mnts":
            print ("maintenance")
            absm.maintenance()


# ** wca : 
    if argv[1] == "wca":
        print ("send command and arguments")
        print("stm.write_cmd_arg(argv[2], argv[3], [argv[4], argv[5]]) = ", argv[2], argv[3], [argv[4], argv[5]])
        stm.write_cmd_arg(int(argv[2]), int(argv[3]), [int(argv[4]), int(argv[5])])
# ** rdwr : 
    if argv[1] == "rdwr":
        print ("send and resiv command and arguments")
        print("stm.write_cmd_arg(argv[2], argv[3], [argv[4], argv[5]]) = ", argv[2], argv[3], [argv[4], argv[5]])
        r = stm.rdwr_cmd_arg(int(argv[2]), int(argv[3]), [int(argv[4]), int(argv[5])])
        print ("resiv = ", r)
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
# ** i2c_msgl : 
    if argv[1] == "i2c_msgl":
        print ("start i2c simbol in and ruturn")
        r = stm.msg_list_size()
        print("return = ", r)
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
        print ("set to on")
        stm.write_cmd(0x10)
# *** off : 
      if argv[2] == "off":
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


