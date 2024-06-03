import time
import board
import analogio

analog_pin = analogio.AnalogIn(board.A2)

def get_voltage(pin):
    return (pin.value / 65535) * 3.3
while True:
    print(get_voltage(analog_pin))
    time.sleep(0.1)
