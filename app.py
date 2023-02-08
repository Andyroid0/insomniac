import pyautogui


def operation():

    currentMouseX, currentMouseY = pyautogui.position()

    mouseToX = currentMouseX + 100

    pyautogui.moveTo(mouseToX, currentMouseY)

    pyautogui.sleep(30)

    currentMouseX, currentMouseY = pyautogui.position()

    mouseToX = currentMouseX - 100

    pyautogui.moveTo(mouseToX, currentMouseY)

    pyautogui.sleep(30)

    execute()


def execute():

    operation()


execute()