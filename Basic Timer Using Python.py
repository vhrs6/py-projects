from time import sleep
from playsound import playsound

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def timer(x):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < x:
        sleep(1)
        time_elapsed += 1
        time_left = x - time_elapsed
        minutes = time_left // 60
        seconds = time_left % 60

        print(f"{CLEAR_AND_RETURN}{minutes:02d}:{seconds:02d}")

    playsound("Ringtone Of Your Choice")


timer(3)
