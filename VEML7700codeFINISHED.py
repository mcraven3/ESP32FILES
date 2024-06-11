#general imports
import time
import board
import microcontroller
import neopixel

import adafruit_veml7700 #sensor specific import

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1) #shortens neopixel command, can be called a pixel now
i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

try: #try statement to catch errors
    with open("/VEML7700_data_values.txt", "a") as light_log: #open text file, in appendage mode, called light_log
        while True: #loops forever
            veml7700 = adafruit_veml7700.VEML7700(i2c) #pull data from sensor, storing as variable
            light_log.write("Lux:  ") #begin writing to file
            light_log.write(str(veml7700.lux)) #sensor values need to be converted from int to str
            light_log.write("\n") #begin a new line
            light_log.flush() #reset file status for next iteration
            pixel.fill((0, 255, 0)) #blink the NeoPixel green to confirm writing
            time.sleep(1)  #delay one second
            pixel.fill((0, 0, 0))  #turn off Neopixel
            time.sleep(4)  #delay 4 seconds, for data collection every 5 seconds

except OSError as e:  # When the filesystem is NOT writable by microcontroller (your computer has permission instead)
    delay = 0.5  # ...blink the NeoPixel red every half second.
    if e.args[0] == 28:  # If the file system is full...
        delay = 0.15  # ...blink the NeoPixel red every 0.15 seconds!
    while True:
        pixel.fill((255, 0, 0))
        time.sleep(delay)
        pixel.fill((0, 0, 0))
        time.sleep(delay)
