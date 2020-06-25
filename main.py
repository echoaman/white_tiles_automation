import cv2
import os
from ppadb.client import Client
import time

adb = Client('127.0.0.1', 5037)
devices = adb.devices()

if len(devices) == 0:
    print('No device connected')
    quit()

device = devices[0]

depth = 1200
boxes = [135, 405, 675, 945]       # x coordinates

while True:
    screen = device.screencap()

    with open('screen.png', 'wb') as f:
        f.write(screen)

    screen = cv2.imread('screen.png')

    for idx,box in enumerate(boxes):
        r, g, b = screen[depth][box]
        # print(r, g, b)
        if r == 255 and g == 255 and b == 255:
            continue

        print(idx)
        device.shell(f'input touchscreen swipe {box} {depth} {box} {depth} 100')
        break

    # time.sleep(0.05)

# cv2.destroyAllWindows()

def debug():
    screen = device.screencap()

    with open('screen.png', 'wb') as f:
        f.write(screen)

    screen = cv2.imread('screen.png')

    for box in boxes:
        print(screen[depth][box])