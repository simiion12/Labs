import numpy as np
from PIL import Image

# Load the image and convert it to a numpy array
img = np.array(Image.open('C:/Users/Administrator/Pictures/picture.jpg'))

# Define the rotation angle in degrees
angle = int(input("Enter the value of angle: "))

def rotation_img(angle):
    # Create a rotation matrix using the given angle
    theta = np.radians(angle)
    cos = np.cos(theta)
    sin = np.sin(theta)
    rotation_matrix = np.array([[cos, -sin, 0], [sin, cos, 0], [0, 0, 1]])

    # Determine the dimensions of the rotated image
    height, width = img.shape[:2]
    new_width = int(np.round(height * np.abs(sin) + width * np.abs(cos)))
    new_height = int(np.round(width * np.abs(sin) + height * np.abs(cos)))

    # Define the center of rotation
    cx, cy = width / 2, height / 2
    dx, dy = new_width / 2, new_height / 2
    center_matrix = np.array([[1, 0, cx], [0, 1, cy], [0, 0, 1]])
    center_matrix_inv = np.array([[1, 0, -dx], [0, 1, -dy], [0, 0, 1]])

    # Apply the rotation and centering matrices to the image
    affine_matrix = np.dot(np.dot(center_matrix, rotation_matrix), center_matrix_inv)
    rotated_img = np.zeros((new_height, new_width, 3), dtype=np.uint8)
    for y in range(new_height):
        for x in range(new_width):
            src_x, src_y, _ = np.dot(affine_matrix, [x, y, 1]).astype(np.int)
            if 0 <= src_x < width and 0 <= src_y < height:
                rotated_img[y, x, :] = img[src_y, src_x, :]
    return rotated_img

# Save the rotated image
rotated_img = Image.fromarray(rotation_img(angle))

rotated_img.show()
