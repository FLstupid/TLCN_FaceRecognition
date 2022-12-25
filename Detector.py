import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
import uuid #unique id
import os
import time

def main_app(name):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path = 'yolov5/runs/train/exp3/weights/best.pt', force_reload = True)
    model.conf = 0.8
    
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
