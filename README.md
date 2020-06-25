# White Tiles Automation

Using [ADB](https://developer.android.com/studio/command-line/adb) and python, I have automated the game [White Tiles 4](https://play.google.com/store/apps/details?id=com.brighthouse.whitetiles4And&hl=en_IN) on my android phone.
ADB gets screenshot of the game and using cv2 library, I get a 2D matrix of pixels of the screenshot. The program checks the colour of each box or rectangle from left to right at a certain depth(the y coordinate for the bottom most black box). If the RGB values of a box are 255 each, the program skips that box as it is white, otherwise the program send a touch command to the phone for that box via ADB.

## Demo:

![Demo gif](https://user-images.githubusercontent.com/45307657/85741777-55877a80-b720-11ea-9499-164f3da33255.gif)
