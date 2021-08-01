import time
import SDL_DS3231

ds3231 = SDL_DS3231.SDL_DS3231(1, 0x68)
ds3231.write_all(29,30,4,1,3,12,92,True)

while True:
    print “Raspberry Pi=\t” + time.strftime(%Y-%m-%d %H:%M:%S”)
    print “Ds3231=\t\t%s” % ds3231.read_datetime()
    time.sleep(10.0)
