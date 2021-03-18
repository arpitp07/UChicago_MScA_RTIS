import cv2
import torch
import numpy as np
import time
# from PIL import Image

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)  # for file/URI/PIL/cv2/np inputs and NMS
# feed_descriptor = cv2.VideoCapture('Chicago Biking.mp4')
feed_descriptor = cv2.VideoCapture('Chicago Biking_Trim.mp4')


while (feed_descriptor.isOpened()):
    current_frame=feed_descriptor.read()[1]
    
    if current_frame is None:
        break
    results = model(current_frame, size=1080) 
    # results.show()
    cv2.imshow('video_original', current_frame)
    cv2.imshow('video_results', results.render()[0])
    # results.save()
    # cv2.imshow('video', current_frame)

    time.sleep(1/20)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
feed_descriptor.release()

# Inference
# results = model('train_testing.mp4')  # includes NMS

# # Results
# results.print()  
# results.save()  # or .show()