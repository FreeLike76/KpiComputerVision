import numpy as np
import cv2

img = np.ones((512, 512, 3), dtype=np.uint8) * 255

for i in range(0, 10000, 10):
    cv2.rectangle(img, (12 + i, 12 + i), (64 + i, 64 + i), (0, 0, 0), 1)
    cv2.imshow("Display", img)
    cv2.waitKey(500)
