import cv2
import numpy as np
from libs import utils

#to use image
image = cv2.imread('images/test_image.jpg')
lane_image = np.copy(image)
canny_image = utils.canny(lane_image)
cropped_image = utils.region_of_interest(canny_image)
lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 10, np.array([]), minLineLength = 8, maxLineGap = 5)
# image ,no. of pixels , degrees to move "degree precision" , threshold "km no2ta yt2t3o 34an a2dr a2ol de image" , 
# averaged_lines = average_slope_intercept(lane_image,lines)
line_image = utils.display_lines(lane_image,lines)
combo_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1) # multiply all elements in lane image with & 1 the same thing
cv2.imshow("result", combo_image)
cv2.waitKey(0)

#====================================================================
# # #to use videos
# cap = cv2.VideoCapture("videos/test2.mp4")
# while(cap.isOpened()):
#     _,frame = cap.read()
#     canny_image = utils.canny(frame)
#     cropped_image = utils.region_of_interest(canny_image)
#     lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 10, np.array([]), minLineLength = 8, maxLineGap = 5)
#     # averaged_lines = average_slope_intercept(frame,lines)
#     line_image = utils.display_lines(frame, lines)
#     combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
#     cv2.imshow("result", combo_image)
#     cv2.waitKey(1)
