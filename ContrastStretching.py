import cv2
import numpy as np

# Load a grayscale image
img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)

# Find the minimum and maximum pixel values
r_min = np.min(img)
r_max = np.max(img)

# Apply contrast stretching
stretched = ((img - r_min) / (r_max - r_min) * 255).astype(np.uint8)

# Show original and stretched images
cv2.imshow('Original', img)
cv2.imshow('Contrast Stretched', stretched)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Horizontally both imges display
# combined = cv2.hconcat([img,stretched])
# cv2.imshow("Original (Left) vs Stretched (Right)", combined)

# Save the result
cv2.imwrite('stretched_image.jpg', stretched)
