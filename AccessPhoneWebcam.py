import requests
import cv2
import numpy as np
import imutils

# Get the URL by download app IP Webcam in play store. Then make sure that your PC and your phone are in the same wifi network.
# In IP Webcam app, click in "Start Server".
# To this code work, you need to maintain ther server running in your mobile phone

url = "http://192.168.0.249:8080/shot.jpg"

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000, height=1000)
    cv2.imshow("VIT_android_cam", img)

    #Press Esc to exit
    if cv2.waitKey(1) == 27:
        break
