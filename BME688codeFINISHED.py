#general imports
import time
import board
import microcontroller
import neopixel

import adafruit_BME680 #sensor specific import

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1) #shortens neopixel command, can be called a pixel now
i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

temperature_offset = -5 #tempature offset, needs to be tested against control sensor


try: #try statement to catch errors
    with open("/BME688_data_values.txt", "a") as data_log: #open text file, in appendage mode, called data_log
        while True:
            bme680 = adafruit_BME680.Adafruit_BME680_I2C(i2c, debug=False) #pull data from sensor, storing as variable
            bme680.sea_level_pressure = 1013.25 #local sea level pressure, needs to be changed
            data_log.write("\nTemperature (in Celcius):  ") #begin writing to file
            data_log.write(str(bme680.temperature + temperature_offset)) #sensor values need to be converted from int to str
            data_log.write("\n") #new line
            data_log.write("Humidity (in Percent):  ")
            data_log.write(str(bme680.relative_humidity)) #sensor values need to be converted from int to str
            data_log.write("\n") #new line
            data_log.write("Air Pressure (in HectoPascals):  ")
            data_log.write(str(bme680.pressure)) #sensor values need to be converted from int to str
            data_log.write("\n") #new line
            data_log.flush() #reset file status for next iteration
            pixel.fill((0, 255, 0)) #blink the NeoPixel green to confirm writing
            time.sleep(1)  #delay one second
            pixel.fill((0, 0, 0))  #turn off Neopixel
            time.sleep(4)  #delay 4 seconds, for data collection every 5 seconds

except OSError as e:  # When the filesystem is NOT writable by microcontroller (your computer has permission instead)
    delay = 0.5  #blink the NeoPixel red every half second
    if e.args[0] == 28:  # If the file system is full
        delay = 0.15  #blink the NeoPixel red every 0.15 seconds!
    while True:
        pixel.fill((255, 0, 0))
        time.sleep(delay)
        pixel.fill((0, 0, 0))
        time.sleep(delay)
