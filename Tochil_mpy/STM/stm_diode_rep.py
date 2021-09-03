mode = 1
cmd = 0x03
print(cmd )
# self.lcd_write(0x02)
mode = 0
cmd = 0x03
# def lcd_write(self, cmd, mode=0):
# self.lcd_write_four_bits(mode | (cmd & 0xF0))
print(mode | (cmd & 0xF0))
print(mode | ((cmd << 4) & 0xF0))

# def lcd_write_four_bits(self, data):
# self.lcd_device.write_cmd(data | LCD_BACKLIGHT)
data = 0
LCD_BACKLIGHT = 0x08
print(data | LCD_BACKLIGHT)
