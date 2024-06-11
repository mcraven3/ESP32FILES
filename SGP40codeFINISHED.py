#general imports
import time
import board
import microcontroller
import neopixel

import adafruit_sgp40 #sensor specific import

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1) #shortens neopixel command, can be called a pixel now
i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

try: #try statement to catch errors
    with open("/SGP40_data_values.txt", "a") as gas_log: #open text file, in appendage mode, called gas_log
        while True:
            sgp = adafruit_sgp40.SGP40(i2c) #pull data from sensor, storing as variable
            gas_log.write("raw gas:  ") #begin writing in file
            gas_log.write(str(sgp.raw)) #sensor values need to be converted from int to str
            gas_log.write("\n") #new line
            gas_log.flush() #reset file status for next iteration
            pixel.fill((0, 255, 0)) #blink the NeoPixel green to confirm writing
            time.sleep(1)  #delay one second
            pixel.fill((0, 0, 0))  #turn off Neopixel
            time.sleep(4)  #delay 4 seconds, for data collection every 5 seconds

except OSError as e:  # When the filesystem is NOT writable by microcontroller (your computer has permission instead)
    delay = 0.5  #blink the NeoPixel  red every half second.
    if e.args[0] == 28:  #If the file system is full
        delay = 0.15  #blink the NeoPixel red every 0.15 seconds!
    while True:
        pixel.fill((255, 0, 0))
        time.sleep(delay)
        pixel.fill((0, 0, 0))
        time.sleep(delay)
