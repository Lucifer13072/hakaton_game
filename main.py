import pygame

import time

timer = 1 * 60

while timer > 0:
    mins, secs = divmod(timer, 60)
    timer_format = '{:02d}:{:02d}'.format(mins, secs)
    print(timer_format, end="\r")
    time.sleep(1)
    timer -= 1

print("Таймер завершен!")

