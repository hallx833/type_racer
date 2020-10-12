# %%
from PIL import Image
import pytesseract as pyt
import pyautogui
from pynput import mouse

# %%
def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        return False

# %%
top = pyautogui.locateOnScreen('top.png', grayscale=True)
bottom = pyautogui.locateOnScreen('bottom.png')
text_im = pyautogui.screenshot(region = (top.left-3, top.top+top.height+70, bottom.width, bottom.top-top.top-top.height-70))

text = pyt.image_to_string(text_im)
text = text.replace('\n', ' ')
text = text.replace('|', 'I')

# %%
listener = mouse.Listener(on_click=on_click)
listener.start()
listener.join()
pyautogui.write(text, interval=0.01)

# %%
