# %%
from PIL import Image
import pytesseract as pyt
import pyautogui
import time

# %%
top = pyautogui.locateOnScreen('top.png', grayscale=True)
bottom = pyautogui.locateOnScreen('bottom.png')
text_im = pyautogui.screenshot(region = (top.left, top.top+top.height+70, bottom.width, bottom.top-top.top-top.height-70))

text = pyt.image_to_string(text_im)
text = text.replace('\n', ' ')
text = text.replace('|', 'I')

# %%
time.sleep(1)
pyautogui.write(text, interval=0.03)


