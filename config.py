from LDR import *

calibration_samples = 5  # Numbers of samples taken in the calibration of the LDR
calibration_samples_interval = 0.2  # The time between the samples

direction = " "  # Variable for the direction of the last swipe

stack = [] #

# declaring pin number relative to position
top_right_pin = 15
top_left_pin = 16
top_mid_pin = 18
mid_right_pin = 31
center_pin = 29
mid_left_pin = 36
bottom_right_pin = 13
bottom_mid_pin = 11
bottom_left_pin = 7

# declaring the LDR objects; The first given value is the name and the second is the pin number.
top_right_ldr = LDR("Top right LDR", top_right_pin, 9)
top_left_ldr = LDR("Top left LDR", top_left_pin, 7)
top_mid_ldr = LDR("Top mid LDR", top_mid_pin, 8)
mid_right_ldr = LDR("Mid right LDR", mid_right_pin, 6)
center_ldr = LDR("Center LDR", center_pin, 5)
mid_left_ldr = LDR("Mid left LDR", mid_left_pin, 4)
bottom_right_ldr = LDR("Bottom right LDR", bottom_right_pin, 3)
bottom_mid_ldr = LDR("Bottom mid LDR", bottom_mid_pin, 2)
bottom_left_ldr = LDR("Bottom left LDR", bottom_left_pin, 1)
