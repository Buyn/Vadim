import time
import SDL_DS3231

ds3231 = SDL_DS3231.SDL_DS3231(1, 0x68)
# ds3231.write_now()

for i in range(0, 10):
    print("---DEF------- ", i, " -------------")
    print ("Raspberry Pi=\t" + time.strftime("%Y-%m-%d %H:%M:%S"))
    print ("Ds3231=\t\t%s" % ds3231.read_datetime())
    print("------------- ", i, " -------------")
    time.sleep(3.0)

ds3231.write_now()
for i in range(0, 10):
    print("----NOW------ ", i, " -------------")
    print ("Raspberry Pi=\t" + time.strftime("%Y-%m-%d %H:%M:%S"))
    print ("Ds3231=\t\t%s" % ds3231.read_datetime())
    print("------------- ", i, " -------------")
    time.sleep(3.0)


# "ds3231.write_all
# (seconds,minutes,hours,day,date,month,year,save_as_24h=True)"
# Range:
# ,* seconds [0,59], 
# ,* minutes [0,59], 
# ,* hours [0,23], 
# ,* day [0,7], 
# ,* date [1-31], 
# ,* month [1-12], 
# ,* year [0-99]

ds3231.write_all(29,30,4,1,3,12,92,True)
for i in range(0, 10):
    print("---SET------- ", i, " -------------")
    print ("Raspberry Pi=\t" + time.strftime("%Y-%m-%d %H:%M:%S"))
    print ("Ds3231=\t\t%s" % ds3231.read_datetime())
    print("------------- ", i, " -------------")
    time.sleep(3.0)
