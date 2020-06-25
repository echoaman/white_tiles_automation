import cv2
from ppadb.client import Client

adb = Client('127.0.0.1', 5037)
devices = adb.devices()

if len(devices) == 0:
    print('No device connected')
    quit()

device = devices[0]

depth = 1200                       # y coordinate
tiles = [135, 405, 675, 945]       # x coordinates

while True:
    screen = device.screencap()

    with open('screen.png', 'wb') as f:
        f.write(screen)

    screen = cv2.imread('screen.png')

    for idx,tile in enumerate(tiles):
        r, g, b = screen[depth][tile]
        # print(r, g, b)
        
        if r == 255 and g == 255 and b == 255:
            continue

        device.shell(f'input touchscreen swipe {tile} {depth} {tile} {depth} 10')
        print(f'Tile clicked: {idx}')
        break

