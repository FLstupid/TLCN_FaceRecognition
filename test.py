#%% YOLOv5 🚀 by Ultralytics, GPL-3.0 license
import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
import uuid #unique id
import os
import time

from PIL import Image 
import PIL
import glob

img = "https://th.bing.com/th/id/R.12861775d1711ce08e63a8286a867a68?rik=VmZt%2fzkgJ1gtXQ&pid=ImgRaw&r=0"

model = torch.hub.load('ultralytics/yolov5','yolov5s')

#%%
img = "https://scontent.fsgn5-11.fna.fbcdn.net/v/t1.6435-9/72185635_151101159465101_8664037780176764928_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=oNHXnntwomwAX_HNK4l&_nc_ht=scontent.fsgn5-11.fna&oh=00_AfAbJhnrt3wn0fPkReTZCRvmG3Dx8vrf_6CW3np9cehyuw&oe=63BD4088"
# print(img.size)
# resized_image = img.resize((640,640)) 
# print(resized_image.size)

result = model(img)
result.show()
result.pandas().xyxy[0]
# result

#%%
model = torch.hub.load('ultralytics/yolov5', 'custom', path = 'yolov5/runs/train/exp/weights/best.pt', force_reload = True)

#%%
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ref, frame = cap.read()

    # detections
    result = model(frame)
    
    cv2.imshow('YOLO', np.squeeze(result.render()))
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
# %%
