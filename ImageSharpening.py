import cv2
import numpy as np

# Load the image
img = cv2.imread('img.jpg')

# Define a sharpening kernel
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

# Apply the kernel to the image
sharpened = cv2.filter2D(img, -1, kernel)

# Display the original and sharpened images
cv2.imshow('Original', img)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the sharpened image
cv2.imwrite('sharpened_image.jpg', sharpened)
