import pyautogui

pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

# for i in range(10):
#       pyautogui.moveTo(300, 300, duration=0.25)
#       pyautogui.moveTo(400, 300, duration=0.25)
#       pyautogui.moveTo(400, 400, duration=0.25)
#       pyautogui.moveTo(300, 400, duration=0.25)

# pyautogui.click()
# x, y = pyautogui.position()
pyautogui.click(x=370,y=49)
# print(x, y)

pyautogui.typewrite('bing.com', 0.15)
pyautogui.press('tab')
pyautogui.typewrite('test from python!', 0.15)
pyautogui.press('enter')