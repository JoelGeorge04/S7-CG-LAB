import cv2
import numpy as np

# Load the image in grayscale
img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Canny edge detector
edges = cv2.Canny(img, 50, 150)

# Stack images side by side
side_by_side = np.hstack((img, edges))

# Show the result
cv2.imshow('Original and Edges', side_by_side)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the side-by-side image
cv2.imwrite('side_by_side.jpg', side_by_side)
