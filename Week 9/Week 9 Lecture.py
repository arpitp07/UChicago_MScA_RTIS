import cv2
import numpy as np
import time

# image = cv2.imread('mario.png', cv2.IMREAD_GRAYSCALE)
# print(image)

# img2 = cv2.imread('mario.png', cv2.IMREAD_GRAYSCALE)



# cv2.imshow('mario', image)
# cv2.waitKey(0)
# # cv2.destroyAllWindows()


# _, image_threshold = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
# cv2.imshow('mario_threshold', image_threshold)
# cv2.waitKey(0)
# # cv2.destroyAllWindows()

# diff = 

# img_blur = cv2.GaussianBlur(image, (31, 31), 0)
# cv2.imshow('mario_blur', img_blur)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

feed_descriptor=cv2.VideoCapture('train_training.mp4')
previous_frame = None
while (feed_descriptor.isOpened()):
    current_frame=feed_descriptor.read()[1]
    
    if current_frame is None:
        break
    current_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    current_frame = cv2.GaussianBlur(current_frame, (31, 31), 0)
    current_frame = cv2.rectangle(current_frame, (284, 300), (400, 400), (0, 255, 0), 3)
    current_frame = cv2.rectangle(current_frame, (484, 300), (600, 400), (0, 255, 0), 3)
    if previous_frame is not None:
        current_frame = cv2.absdiff(np.float32(previous_frame),	np.float32(current_frame))
    
    box1 = current_frame[284:400, 300:400]
    box2 = current_frame[484:600, 300:400]
    # box1_ratio = np.count_nonzero(box1)/box1.size

    
    previous_frame = current_frame
    
    cv2.imshow('video', current_frame)

    time.sleep(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
feed_descriptor.release()
