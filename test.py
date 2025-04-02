import time
import keyboard
import pydirectinput

def interrupted_sleep(seconds, check_interval=0.1):
    """
    Sleeps for the specified number of seconds, checking repeatedly
    if the 'q' key has been pressed. Returns True if 'q' is pressed,
    or False if the sleep completes normally.
    """
    steps = int(seconds / check_interval)
    for _ in range(steps):
        if keyboard.is_pressed("q"):
            return True
        time.sleep(check_interval)
    return False

def main():
    print("The script will start in 5 seconds. Switch to Roblox now.")
    time.sleep(5)
    print("Script running. Press 'q' to stop.")

    while True:
        # Check if 'q' is pressed before pressing space
        if keyboard.is_pressed("q"):
            print("Stop key pressed. Exiting.")
            break

        # Press the space bar using pydirectinputq
        pydirectinput.press("space")
        print("Space bar pressed. Waiting 10 second...")

        if interrupted_sleep(10):
            print("Stop key pressed during waiting period. Exiting.")
            break

if __name__ == "__main__":
    main()