from machine import Pin
from time import sleep, sleep_us, ticks_us
from lcd1602 import LCD1602

lcd = LCD1602(62, 5, 4)

lcd.write("Distance:")

lcd.set_cursor(0, 1)

trigger = Pin(0, Pin.OUT)
echo = Pin(1, Pin.IN)

def get_distance():
    trigger.low()
    sleep_us(2)
    trigger.high()
    sleep_us(5)
    trigger.low()
    
    while echo.value() == 0:
        off_time = ticks_us()
    while echo.value() == 1:
        on_time = ticks_us()
    
    time_passed = on_time - off_time # type: ignore
    distance = (time_passed * 0.0343) / 2
    return int(distance)

while True:
    try:
        distance = get_distance()
        lcd.set_cursor(0, 1)
        lcd.write(" " * 16)
        lcd.set_cursor(0, 1)
        lcd.write(str(distance) + " cm")
        sleep(0.25)
    except KeyboardInterrupt:
        break
    except Exception as e:
        print("Error:", e)
        break

lcd.reset()
print("Exited")