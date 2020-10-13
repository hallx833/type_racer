# %%
from PIL import Image
import pytesseract as pyt
import pyautogui

# %%
top = pyautogui.locateOnScreen('top.png')
bottom = pyautogui.locateOnScreen('bottom.png')
text_im = pyautogui.screenshot(region = (top.left-3, top.top+top.height+70, bottom.width, bottom.top-top.top-top.height-70))

text = pyt.image_to_string(text_im)
text = text.replace('\n', ' ')
text = text.replace('|', 'I')

pyautogui.moveTo(bottom.left + (bottom.width // 2), bottom.top + (bottom.height // 2))
pyautogui.click()
pyautogui.write(text, interval=0.01)

# %%
