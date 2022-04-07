from tempfile import template
import cv2
import numpy as np
import pyautogui
import time

fps = 30
prev = 0
template = cv2.imread('template.png')
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
print(template.shape)
counter = 0
while True:
    # time_elapsed = time.time()-prev
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # frame = cv2.imread('Снимок экрана 2022-04-07 в 12.45.53.png')
    # frame = cv2.imread('Снимок экрана 2022-04-07 в 15.47.27.png')
    # pic2 = cv2.cvtColor(pic2, cv2.COLOR_BGR2GRAY)
    # res = cv2.matchTemplate(pic1, pic2, cv2.TM_CCOEFF_NORMED)
    # if time_elapsed > 1.0/fps:
    #     prev = time.time()
    frame = frame[102:438, 2668:2870, :]
    # frame = cv2.resize(frame, (template.shape[1], template.shape[0]))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(template, frame, cv2.TM_CCOEFF_NORMED)
    print(res)
    loc = np.where(res >= 0.50)
    if loc[0].size != 0:
        counter += 1
        cv2.imwrite(f'{counter}.jpg', frame)
    cv2.imshow('template', template)
    cv2.imshow('frame', frame)
    cv2.waitKey(3000)



