#General Imports
import time
import board

import adafruit_sgp40 #sensor specific

i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sgp = adafruit_sgp40.SGP40(i2c) #Shortens sensor command, sensor can be referenced as sgp

while True: #loop will go on until interupted by a reset
    print("Raw Gas: ", sgp.raw) #read the raw data from the sensor, and then print in serial monitor
    print("\n") #create a new line for next iteration
    time.sleep(1) #1 second delay
