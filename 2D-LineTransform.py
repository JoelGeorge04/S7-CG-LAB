import numpy as np
import matplotlib.pyplot as plt

x1, y1 = 2, 2
x2, y2 = 6, 2

P1 = np.array([x1, y1, 1])
P2 = np.array([x2, y2, 1])

print("Choose 2D Line Transformation:")
print("1. Translation")
print("2. Scaling")
print("3. Rotation")
print("4. Shearing")
print("5. Reflection")
choice = int(input("Enter choice (1-5): "))

if choice == 1:
    # Translation
    tx, ty = 3, 2
    T = np.array([[1, 0, tx],
                  [0, 1, ty],
                  [0, 0, 1]])
    title = f"Translation by ({tx}, {ty})"

elif choice == 2:
    # Scaling
    sx, sy = 1.5, 0.5
    T = np.array([[sx, 0, 0],
                  [0, sy, 0],
                  [0, 0, 1]])
    title = f"Scaling by ({sx}, {sy})"

elif choice == 3:
    # Rotation
    theta = np.radians(45)
    T = np.array([[np.cos(theta), -np.sin(theta), 0],
                  [np.sin(theta), np.cos(theta), 0],
                  [0, 0, 1]])
    title = "Rotation by 45°"

elif choice == 4:
    # Shearing
    shx, shy = 0.5, 0
    T = np.array([[1, shx, 0],
                  [shy, 1, 0],
                  [0, 0, 1]])
    title = f"Shearing (X={shx}, Y={shy})"

elif choice == 5:
    # Reflection (about x-axis)
    T = np.array([[1, 0, 0],
                  [0, -1, 0],
                  [0, 0, 1]])
    title = "Reflection about X-axis"

else:
    print("Invalid choice!")
    exit()

P1_new = T @ P1
P2_new = T @ P2

plt.plot([x1, x2], [y1, y2], 'b-o')  
plt.plot([P1_new[0], P2_new[0]], [P1_new[1], P2_new[1]], 'r--o')  
plt.title(title)
plt.axis('equal')  
plt.show()