import time
import board
import microcontroller
import neopixel

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)

try:
    with open("/temperature.txt", "a") as temp_log:
        while True:
            temperature = microcontroller.cpu.temperature
            temp_log.write('{0:.2f}\n'.format(temperature))
            temp_log.flush()
            pixel.fill((0, 255, 0))
            time.sleep(1)  
            pixel.fill((0, 0, 0))  
            time.sleep(9)  

except OSError as e:  
    delay = 0.5  
    if e.args[0] == 28:  
        delay = 0.15  
    while True:
        pixel.fill((255, 0, 0))
        time.sleep(delay)
        pixel.fill((0, 0, 0))
        time.sleep(delay)
