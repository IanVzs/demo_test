"""
Create New profile or Fetch defalu profile path:
    - firefox -P

tree:
|-- geckodriver
|-- geckodriver.log
|-- profile
|-- sele.py
`-- venv

Warning:
    when firefox runing, this script can't use the same profile.

Run:
    - venv/bin/python sele.py
"""

import os
import cv2
os.environ["PATH"] += ':.'
import time
import base64
import numpy as np

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options=Options()
options.add_argument("-profile")
options.add_argument("./profile")

browser=webdriver.Firefox(executable_path="geckodriver", options=options)
# browser.get("https://play.fancybirds.io/")
browser.get("https://www.youtube.com/watch?v=R94NqxlXAOs")

def get_screenshot():
    # full page
    global browser
    img_base64 = browser.get_screenshot_as_base64()
    img_decode = base64.b64decode(img_base64)
    img_array = np.fromstring(img_decode, np.uint8)
    img = cv2.imdecode(img_array, cv2.COLOR_BGR2GRAY)
    return img

def get_element(ele_id: str = ''):
    # one element
    global browser
    get_base64_script = f'''var canvas = document.getElementById("{ele_id}"); return canvas.toDataURL().substring(22);'''
    img_base64 = browser.execute_script(get_base64_script)
    img_decode = base64.b64decode(img_base64)
    img_array = np.fromstring(img_decode, np.uint8)
    img = cv2.imdecode(img_array, cv2.COLOR_BGR2GRAY)
    return img

try:
    while 1:
        a = time.time()
        frame = get_element("movie_player")
        print(f"cap cost: {time.time() - a}s")
        cv2.imshow("", frame)
        cv2.waitKey(1) & 0xff & ord("q")
except Exception as err:
    print(err)
cv2.destroyAllWindows()
browser.quit()

# ---

try:
    while 1:
        a = time.time()
        frame = get_screenshot()
        print(f"cap cost: {time.time() - a}s")
        cv2.imshow("", frame)
        cv2.waitKey(1) & 0xff & ord("q")
except Exception as err:
    print(err)
cv2.destroyAllWindows()
browser.quit()