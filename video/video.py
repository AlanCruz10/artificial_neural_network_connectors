import cv2
import os

videos = ['usb_male_nluz_2', 'usb_male_nluz', 'usb_male_luz_2', 'usb_male_luz']

for video in videos:
    vidcap = cv2.VideoCapture(video + '.mp4')
    success, image = vidcap.read()
    count = 0
    os.mkdir(video)
    while success:
        cv2.imwrite(f"{video}/frame{count}.jpg", image)  # save frame as JPEG file
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1
