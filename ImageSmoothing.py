import cv2

# Load the image
img = cv2.imread('img.jpg')

# 1. Averaging
blur_avg = cv2.blur(img, (5, 5))

# 2. Gaussian Blur
blur_gauss = cv2.GaussianBlur(img, (5, 5), 0)

# 3. Median Filter
blur_median = cv2.medianBlur(img, 5)

# Display the results
cv2.imshow('Original', img)
cv2.imshow('Averaging', blur_avg)
cv2.imshow('Gaussian Blur', blur_gauss)
cv2.imshow('Median Filter', blur_median)
cv2.waitKey(0)
cv2.destroyAllWindows()
