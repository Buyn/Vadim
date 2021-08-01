import I2C_LCD_driver
from time import *

print(" start ")
mylcd = I2C_LCD_driver.lcd()


print("backlight  on  ")
mylcd.backlight( 1)

print("send string  ")
mylcd.lcd_display_string("Hello World!", 1)
