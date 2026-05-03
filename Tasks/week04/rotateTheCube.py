import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# 1. Define the 8 vertices of a cube in 3D space
vertices = np.array([
    [-1, -1, -1], # 0
    [ 1, -1, -1], # 1
    [ 1,  1, -1], # 2
    [-1,  1, -1], # 3
    [-1, -1,  1], # 4
    [ 1, -1,  1], # 5
    [ 1,  1,  1], # 6
    [-1,  1,  1]  # 7
])

# Define the 12 edges by connecting specific vertex indices
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Bottom face
    (4, 5), (5, 6), (6, 7), (7, 4),  # Top face
    (0, 4), (1, 5), (2, 6), (3, 7)   # Vertical pillars connecting faces
]

# 2. Define rotation matrices for X, Y, and Z axes
def rotate_x(angle):
    rad = np.radians(angle)
    c, s = np.cos(rad), np.sin(rad)
    return np.array([
        [1, 0, 0],
        [0, c, -s],
        [0, s, c]
    ])

def rotate_y(angle):
    rad = np.radians(angle)
    c, s = np.cos(rad), np.sin(rad)
    return np.array([
        [c, 0, s],
        [0, 1, 0],
        [-s, 0, c]
    ])

def rotate_z(angle):
    rad = np.radians(angle)
    c, s = np.cos(rad), np.sin(rad)
    return np.array([
        [c, -s, 0],
        [s, c, 0],
        [0, 0, 1]
    ])

# 3. Set up the figure and 3D axis
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.25) # Make room for sliders

# Plot the initial cube and store the line objects in a list
lines = []
for start, end in edges:
    line, = ax.plot(
        [vertices[start, 0], vertices[end, 0]],
        [vertices[start, 1], vertices[end, 1]],
        [vertices[start, 2], vertices[end, 2]],
        'b-', lw=2
    )
    lines.append(line)

# Set static axis limits so the cube doesn't scale visually when rotating
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('Rotating the Cube')

# 4. Define the position and size of the sliders
ax_rot_x = plt.axes([0.2, 0.15, 0.65, 0.03])
ax_rot_y = plt.axes([0.2, 0.10, 0.65, 0.03])
ax_rot_z = plt.axes([0.2, 0.05, 0.65, 0.03])

# Create the sliders
slider_x = Slider(ax_rot_x, 'Pitch (X)', 0, 360, valinit=0)
slider_y = Slider(ax_rot_y, 'Yaw (Y)', 0, 360, valinit=0)
slider_z = Slider(ax_rot_z, 'Roll (Z)', 0, 360, valinit=0)

# 5. Define the update function
def update(val):
    angle_x = slider_x.val
    angle_y = slider_y.val
    angle_z = slider_z.val

    # Combine rotations
    R = rotate_x(angle_x) @ rotate_y(angle_y) @ rotate_z(angle_z)
    rotated_vertices = (R @ vertices.T).T

    # Update each line segment with new rotated coordinates
    for i, (start, end) in enumerate(edges):
        lines[i].set_data(
            [rotated_vertices[start, 0], rotated_vertices[end, 0]],
            [rotated_vertices[start, 1], rotated_vertices[end, 1]]
        )
        lines[i].set_3d_properties(
            [rotated_vertices[start, 2], rotated_vertices[end, 2]]
        )
    
    fig.canvas.draw_idle()

# 6. Register updates
slider_x.on_changed(update)
slider_y.on_changed(update)
slider_z.on_changed(update)

plt.show()