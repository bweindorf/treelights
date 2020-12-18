import time
import sys
import RPi.GPIO as GPIO


on = "1111111100000000101110001"
off = "1111111100000000101110101"
multi = "1111111100000000101110111" 
warm_white = "1111111100000000101111001" 
slo_gol = "1111111100000000111101101" 
twinkle = "1111111100000000111110001" 
dim = "1111111100000000111100101" 
bright = "1111111100000000111010011" 
short_delay = 0.00025
long_delay = 0.000736
extended_delay = 0.007

NUM_ATTEMPTS = 20
TRANSMIT_PIN = 23

def transmit_code(code):
    '''Transmit a chosen code string using the GPIO transmitter'''
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRANSMIT_PIN, GPIO.OUT)
    for t in range(NUM_ATTEMPTS):
        for i in code:
            if i == '1':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(short_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(long_delay)
            elif i == '0':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(long_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(short_delay)
            else:
                continue
        GPIO.output(TRANSMIT_PIN, 0)
        time.sleep(extended_delay)
    GPIO.cleanup()

if __name__ == '__main__':
    for argument in sys.argv[1:]:
        exec('transmit_code(' + str(argument) + ')')
