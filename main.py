import config
import time
import functions
import threading
import website
from LDR import *


# The main method and loop for the ldr.
def game():
    try:
        time.sleep(3)
        functions.calibration_sensors()
        while True:

            functions.calibration_sensors()

            # direction_detection()
            # print(config.direction)
            # time.sleep(0.01)
            # config.direction = "null"

            functions.check()
            print(config.stack)
            if len(config.stack) >= 3:
                config.direction = functions.find_direction()
                print(config.direction)
            time.sleep(0.2)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    game()
    # t_game = threading.Thread(target=game())
    # t_website = threading.Thread(target=website.app.run())
    # t_game.start()
    # t_website.start()
    # t_game.join()
    # t_website.join()
