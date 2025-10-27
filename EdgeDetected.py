import cv2
import numpy as np

img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(img, 50, 150)

side_by_side = np.hstack((img, edges))

cv2.imshow('Original and Edges', side_by_side)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('side_by_side.jpg', side_by_side)
