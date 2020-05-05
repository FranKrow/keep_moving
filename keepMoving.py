import pyautogui
import time

selectIconPath = "icons/select.png"
pencilIconPath = "icons/pencil.png"
maximizeIconPath = "icons/maximize.png"

# Class that represents an array objects for the color selection


class color:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def clickOnIcon(iconPath):
    location = None
    try:
        location = pyautogui.locateOnScreen(iconPath)
    except ImageNotFoundException as e:
        print(e)
    if location != None:
        pyautogui.click(location.left+(location.width/2),
                        location.top+(location.height/2))
    else:
        print("Can't find icon at path: {0}".format(iconPath))
    time.sleep(0.5)

# Set up the variables for the init of the loop


def setUp():
    global count, accumulativeWidth, startX
    # Click on Select icon
    clickOnIcon(selectIconPath)
    # select all the canvas
    pyautogui.hotkey('ctrl', 'a')
    # Delete All
    pyautogui.hotkey('delete')
    # Click on the pencil
    clickOnIcon(pencilIconPath)
    count = 0
    accumulativeWidth = 200
    startX = 11

# Draw the image on paint


def drawImage(lineLength):
    # Change color
    pyautogui.doubleClick(colors[count].x, colors[count].y, 0.2)
    duration = 0.1
    pyautogui.click(startX, startY)
    while lineLength > 0:
        pyautogui.drag(lineLength, 0, duration)   # move right
        lineLength -= 5
        pyautogui.drag(0, lineLength, duration)   # move down
        pyautogui.drag(-lineLength, 0, duration)  # move left
        lineLength -= 5
        pyautogui.drag(0, -lineLength, duration)  # move up


def initPaint():
    pyautogui.hotkey("win")
    time.sleep(1)  # giving time for windows bar to show
    pyautogui.typewrite("paint", interval=0.25)
    pyautogui.press('enter')


screenWidth, screenHeight = pyautogui.size()

# colors palet from paint (x,y coordinates for the color icons)
colors = []
colors.append(color(960, 60))
colors.append(color(940, 60))
colors.append(color(920, 60))
colors.append(color(900, 60))
colors.append(color(880, 60))
colors.append(color(860, 60))

count = 0  # How many figures were drawn
accumulativeWidth = 200  # The total of the width used for the figures
startX = 15  # Initial x point within paint
startY = 150  # Initial y point within paint

initPaint()
time.sleep(2)  # Some time so the paint app can load
# Click on Maximize
clickOnIcon(maximizeIconPath)
setUp()  # Setup the app

while accumulativeWidth < screenWidth:
    distance = 200
    accumulativeWidth += distance

    drawImage(distance)

    startX += distance
    count += 1

    if accumulativeWidth > screenWidth:
        setUp()
