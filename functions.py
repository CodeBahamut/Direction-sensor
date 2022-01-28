import config
import time

# Function for printing all the values from the ldrs (for testing)
def print_ldr_values():
    # print(config.top_left_ldr.read_ldr(), config.top_mid_ldr.read_ldr(),
    #       config.top_right_ldr.read_ldr())
    print(config.mid_left_ldr.read_ldr(), config.center_ldr.read_ldr(),
          config.mid_right_ldr.read_ldr())
    # print(config.bottom_left_ldr.read_ldr(), config.bottom_mid_ldr.read_ldr(),
    #       config.bottom_right_ldr.read_ldr())
    time.sleep(0.5)

# Function for calibrating the ldrs
def calibration_sensors():
    config.mid_right_ldr.calibration()
    config.center_ldr.calibration()
    config.mid_left_ldr.calibration()

# Function for printing the stack of which LDR was switched first. (For testing)
def print_stack():
    print(config.stack)
    time.sleep(1.0)

# Function to go throught the check function of all the used LDRs
def check():
    config.mid_right_ldr.check_light()
    config.center_ldr.check_light()
    config.mid_left_ldr.check_light()

# Current method for finding direction and putting it in the direction variable.
# Would prefer a switch case but that doesn't exist in python 3.9.
def find_direction():
    if config.stack[0] == config.mid_left_ldr:
        config.stack.remove(config.mid_left_ldr)
        if config.stack[1] == config.center_ldr:
            direction = "Right"
            print("Right")
            return direction

    elif config.stack[0] == config.mid_right_ldr:
        config.stack.remove(config.mid_right_ldr)
        if config.stack[1] == config.center_ldr:
            direction = "Left"
            print("Left")
            return direction



# Original function for finding direction (Didnt work)
# def direction_detection():
#     if config.mid_right_ldr.check_light():
#         if config.center_ldr.check_light():
#             if config.mid_left_ldr.check_light():
#                 config.direction = "Left"
#     elif config.mid_left_ldr.check_light():
#         if config.center_ldr.check_light():
#             if config.mid_right_ldr.check_light():
#                 config.direction = "Right"