import time
import board
import adafruit_veml7700

i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
veml7700 = adafruit_veml7700.VEML7700(i2c)

while True:
    print("Ambient light:", veml7700.light)
    print("\n")
    print("Lux:", veml7700.lux)
    time.sleep(0.1)
