import pyautogui
import re
def mouse_move():
    pyautogui.FAILSAFE = False
    size = str(pyautogui.size())
    num = re.findall(r'\d+', size)
    print(num)
    print(type(num))
    pyautogui.moveTo(int(num[0])-1, 0, duration = 1)
    x = int(num[0]) * 0.01
    y = int(num[1]) * 0.01
    pyautogui.moveRel(0 - x, y, duration = 1)
    pyautogui.click(int(num[0]) - x, y)
    pyautogui.click()

if __name__ == '__main__':
    mouse_move()
