import cv2
import matplotlib.pyplot as plt

# Read the image in grayscale
img = cv2.imread('image.jpg', 0)

# Apply histogram equalization
equalized = cv2.equalizeHist(img)

# Create a window for display
plt.figure(figsize=(10,5))

# Show original image
plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Show equalized image
plt.subplot(2,2,2)
plt.imshow(equalized, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

# Show histogram of original image
plt.subplot(2,2,3)
plt.hist(img.ravel(), 256, [0,256])
plt.title('Original Histogram')

# Show histogram of equalized image
plt.subplot(2,2,4)
plt.hist(equalized.ravel(), 256, [0,256])
plt.title('Equalized Histogram')

# Display everything
plt.tight_layout()
plt.show()
