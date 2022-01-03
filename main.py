from pynput.keyboard import Key, Controller
import time
import random
if __name__ == "__main__":
    keyboard = Controller()
    print("running. Switch window to discord in 5 seconds.")
    time.sleep(5)
    while (True):
        keyboard.type('%f')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random.randint(16, 20))
