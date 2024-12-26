import time
from machine import I2C, Pin

class LCD1602:
    def __init__(self, addr, scl, sda):
        self.i2c = I2C(0, scl=Pin(scl), sda=Pin(sda))
        self.addr = addr
        self.send_command(0x33)
        self.send_command(0x32)
        self.send_command(0x28)
        self.send_command(0x0c)
        self.send_command(0x06)
        self.send_command(0x01)
        time.sleep(0.002)

    def send_command(self, command):
        self.i2c.writeto(self.addr, bytes([0x80, command]))

    def send_data(self, data):
        self.i2c.writeto(self.addr, bytes([0x40, data]))
    
    def clear(self):
        self.send_command(0x01)
        time.sleep(0.002)

    def set_cursor(self, col, row):
        if row == 0:
            pos = 0x80 + col
        elif row == 1:
            pos = 0xC0 + col
        self.send_command(pos)

    def write(self, msg):
        for char in msg:
            self.send_data(ord(char))

    def scroll_display_left(self):
        self.send_command(0x18)

    def scroll_display_right(self):
        self.send_command(0x1C)

    def typewrite(self, msg):
        for char in msg:
            self.send_data(ord(char))
            time.sleep(0.1)

    def reset(self):
        self.send_command(0x01)
        time.sleep(0.002)
        self.send_command(0x38)
        self.send_command(0x0C)
        self.send_command(0x06)



