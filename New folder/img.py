import cv2
import numpy as np
from google.colab.patches import cv2_imshow
import matplotlib as plt

# Read the image
image = cv2.imread("ss-pb.jpg")
print('Image read successfully')
      
roi_x, roi_y, roi_width, roi_height = 400, 400, 600, 600
print("ROI coordinates defined.")

cv2.rectangle(image, (roi_x, roi_y), (roi_x + roi_width, roi_y + roi_height), (0, 255, 0), 2)

roi = image[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width]
print(roi)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
print(image_rgb)
print(roi_rgb)

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image with ROI")

plt.subplot(1, 2, 2)
plt.imshow(roi_rgb)
plt.title("Cropped ROI")
