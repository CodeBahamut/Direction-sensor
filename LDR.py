import RPi.GPIO as GPIO
import time
import config

GPIO.setmode(GPIO.BOARD)

# Class for the ldr
class LDR:
    def __init__(self, name, pin, number):
        self.name = name
        self.pin = pin
        self.number = number
        self.base_resistance = 0
        self.object_detected = False

    # This method gets the value from ldr
    def resistor_count(self):
        count = 0

        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(self.pin, GPIO.IN)

        while GPIO.input(self.pin) == GPIO.LOW:
            count += 1

        return count

    # This is used to return the value and the number of the ldr
    def read_ldr(self):
        words = (self.number, self.resistor_count())
        return words

    # This calibrates the sensor by taking some samples then getting the average.
    def calibration(self):
        value = 0
        print("Calibrating..." + self.name)
        for x in range(config.calibration_samples):
            value += self.resistor_count()
            time.sleep(config.calibration_samples_interval)

        value = value / config.calibration_samples
        self.base_resistance = value + 1000

    # This check if there is an object/shadow infront of the LDR
    def check_light(self):
        if self.resistor_count() > self.base_resistance:
            self.object_detected = True
            config.stack.append(self.number)

        return self.object_detected
