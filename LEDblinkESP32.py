import time
import board
import microcontroller
import neopixel

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)

while True:
    pixel.fill((255, 255, 255))
    time.sleep(2)
    pixel.fill((0, 0, 0))
    time.sleep(2)
    time.sleep(2)# Write your code here :-)
