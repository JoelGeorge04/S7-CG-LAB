import cv2
import numpy as np

# Load the image in grayscale
img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)

# Menu
print("Choose Image Transformation:")
print("1. Negative")
print("2. Log Transform")
print("3. Inverse Log Transform")
print("4. Power-Law (Gamma) Transform")
choice = int(input("Enter choice (1-4): "))

# Apply the chosen transformation
if choice == 1:
    transformed = 255 - img
    title = "Negative Transformation"

elif choice == 2:
    # s=c⋅log(1+r)
    c = 255 / np.log(1 + np.max(img))
    log = c * np.log(1 + img)
    transformed = np.array(log, dtype=np.uint8)
    title = "Log Transformation"

elif choice == 3:
    # s=c⋅(er−1)
    c = 1
    inverse_log = c * (np.exp(img / 255) - 1)
    transformed = np.array(255 * inverse_log / np.max(inverse_log), dtype=np.uint8)
    title = "Inverse Log Transformation"

elif choice == 4:
    # s=c⋅rγ
    gamma = float(input("Enter gamma value (e.g., 0.5 for brighten, >1 for darken): "))
    transformed = np.array(255 * (img / 255) ** gamma, dtype=np.uint8)
    title = f"Power-Law (Gamma) Transformation (γ={gamma})"

else:
    print("Invalid choice!")
    exit()

# Show results
cv2.imshow("Original", img)
cv2.imshow(title, transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save result
cv2.imwrite('transformed_image.jpg', transformed)
