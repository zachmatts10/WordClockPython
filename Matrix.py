# File MUST be named Matrix.py or adjusted in the wordclock program
#Gpio import
import RPi.GPIO as GPIO
import time

# use P1 header pin numbering convention
GPIO.setmode (GPIO.BCM)
# Deactivate the already set Gpio warning
GPIO.setwarnings (False)

#Pins as variables Adjust if the pink configuration changes
redZero = 11
greenZero = 21
blueZero = 7
redOne = 8
greenOne = 9
blueOne = 10
a = 22
b = 23
c = 24
d = 25
oe = 18
clock = 17
latch = 4

# GPIO pin - as output
GPIO.setup (redZero, GPIO.OUT)
GPIO.setup (greenZero, GPIO.OUT)
GPIO.setup (blueZero, GPIO.OUT)
GPIO.setup (redOne, GPIO.OUT)
GPIO.setup (greenOne, GPIO.OUT)
GPIO.setup (blueOne, GPIO.OUT)
GPIO.setup (a, GPIO.OUT)
GPIO.setup (b, GPIO.OUT)
GPIO.setup (c, GPIO.OUT)
GPIO.setup (d, GPIO.OUT)
GPIO.setup (oe, GPIO.OUT)
GPIO.setup (clock, GPIO.OUT)
GPIO.setup (latch, GPIO.OUT)

# GPIO list (array)
gpioList = [oe, d, c, b, a]
Zero = [redZero, greenZero, blueZero]
One = [redOne, greenOne, blueOne]

def panel (table):
        for j in range (16):
# bin converts j into binary number, zfill fills up to 5 digits (oe must be with), 2: abbreviates the first two digits (0b), list creates a list
                demux = list (bin (j) [2:]. zfill (5))
# controls the demultiplexer
                for x in range (5):
                        if demux [x] == '0':
                                GPIO.output (gpioList [x], False)
                        elif demux [x] == '1':
                                GPIO.output (gpioList [x], True)
                for i in range (32):
                        if table [j] [i] == 0:
                                GPIO.output (clock, GPIO.HIGH)
                                GPIO.output (clock, GPIO.LOW)
                        elif table [j] [i] == 1:
                                for a in range (3):
                                        GPIO.output (Zero [a], GPIO.HIGH)
                                GPIO.output (clock, GPIO.HIGH)
                                GPIO.output (clock, GPIO.LOW)
                                for a in range (3):
                                        GPIO.output (Zero [a], GPIO.LOW)
                GPIO.output (latch, GPIO.HIGH)
                GPIO.output (latch, GPIO.LOW)

                for i in range (32):
                        if table [j + 16] [i] == 0:
                                GPIO.output (clock, GPIO.HIGH)
                                GPIO.output (clock, GPIO.LOW)
                        elif table [j + 16] [i] == 1:
                                for a in range (3):
                                        GPIO.output (One [a], GPIO.HIGH)
                                GPIO.output (clock, GPIO.HIGH)
                                GPIO.output (clock, GPIO.LOW)
                                for a in range (3):
                                        GPIO.output (One [a], GPIO.LOW)

                GPIO.output (latch, GPIO.HIGH)
                GPIO.output (latch, GPIO.LOW)
