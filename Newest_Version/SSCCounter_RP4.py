import requests
import time
import cv2
import numpy as np
from datetime import datetime

url = 'http://114.71.48.94:80/uploadfile'
filename = 'photo.jpg'
ksize = 20              # 블러 처리에 사용할 커널 크기

def send_img():
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        while True:
            ret, frame = cap.read()
            if ret:
                if cv2.waitKey(1) == -1:
                    x,y,w,h = 390, 325, 80, 100 # 관심영역 선택
                    roi = frame[y:y+h, x:x+w]   # 관심영역 지정
                    roi = cv2.blur(roi, (ksize, ksize)) # 블러(모자이크) 처리
                    frame[y:y+h, x:x+w] = roi   # 원본 이미지에 적용
                    
                    x,y,w,h = 342, 390, 40, 70 # 관심영역 선택
                    roi = frame[y:y+h, x:x+w]   # 관심영역 지정
                    roi = cv2.blur(roi, (ksize, ksize)) # 블러(모자이크) 처리
                    frame[y:y+h, x:x+w] = roi   # 원본 이미지에 적용
                    
                    fliped = cv2.flip(frame, -1)
                    cv2.imwrite('photo.jpg', fliped)  # 이미지 저장
                    break
            else:
                print('no frame')
                break
    else:
        print('no camera!')
    cap.release()
    img = "photo.jpg"  # 이미지 경로
    

    with open(filename, 'rb') as f:
        r = requests.post(url, files={'file': f})
        
    print(datetime.now(),end="      ")
    print(r.text,end="\n\n")

send_img()
while True:
    try:
        send_img()
    except:
        print("{0}      !Send Error!".format(datetime.now()), end = "\n\n")
    #if datetime.now().second % 1 == 0:
    #    try:
    #        send_img()
    #    except:
    #        print("{0}      !Send Error!".format(datetime.now()), end = "\n\n")
    time.sleep(0.3)