import cv2

# Load image in grayscale
img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)

# Apply binary thresholding
_, segmented = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

# Display original and segmented images
cv2.imshow('Original', img)
cv2.imshow('Segmented', segmented)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the segmented image
cv2.imwrite('segmented_image.jpg', segmented)
