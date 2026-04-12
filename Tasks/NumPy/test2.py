import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# 1. Base Square Vertices (Centered at origin for clean rotation)
vertices = np.array([
    [-0.5, -0.5, 0],
    [ 0.5, -0.5, 0],
    [ 0.5,  0.5, 0],
    [-0.5,  0.5, 0]
])

# 2. Setup Figure and Axes
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Shrink the main plot to leave room for sliders at the bottom
plt.subplots_adjust(bottom=0.3) 

# 3. Initial Plotting
closed_square = np.vstack((vertices, vertices[0]))

# We save the plot to a variable ('line,') so we can update its data later
line, = ax.plot(closed_square[:, 0], closed_square[:, 1], closed_square[:, 2], 
                color='red', linewidth=2, marker='o')

# Lock the axis limits so the square moves, not the camera
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.set_box_aspect([1, 1, 1])
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# 4. Slider Setup (Positioning: [left, bottom, width, height])
ax_x = plt.axes([0.2, 0.2, 0.65, 0.03])
ax_y = plt.axes([0.2, 0.15, 0.65, 0.03])
ax_z = plt.axes([0.2, 0.1, 0.65, 0.03])

slider_x = Slider(ax_x, 'Rotate X', 0, 360, valinit=0)
slider_y = Slider(ax_y, 'Rotate Y', 0, 360, valinit=0)
slider_z = Slider(ax_z, 'Rotate Z', 0, 360, valinit=0)

# 5. The Update Function (Triggered every time a slider moves)
def update(val):
    # Get current slider values and convert to radians
    ax_deg = np.radians(slider_x.val)
    ay_deg = np.radians(slider_y.val)
    az_deg = np.radians(slider_z.val)
    
    # Rotation Matrix X
    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(ax_deg), -np.sin(ax_deg)],
        [0, np.sin(ax_deg),  np.cos(ax_deg)]
    ])
    
    # Rotation Matrix Y
    Ry = np.array([
        [ np.cos(ay_deg), 0, np.sin(ay_deg)],
        [ 0,              1, 0             ],
        [-np.sin(ay_deg), 0, np.cos(ay_deg)]
    ])
    
    # Rotation Matrix Z
    Rz = np.array([
        [np.cos(az_deg), -np.sin(az_deg), 0],
        [np.sin(az_deg),  np.cos(az_deg), 0],
        [0,              0,               1]
    ])
    
    # Combined rotation matrix
    R = Rz @ Ry @ Rx
    
    # Apply transformation and close the shape
    rotated = vertices @ R.T
    closed_rotated = np.vstack((rotated, rotated[0]))
    
    # Update the existing line data instead of redrawing the whole plot
    line.set_data(closed_rotated[:, 0], closed_rotated[:, 1])
    line.set_3d_properties(closed_rotated[:, 2])
    
    # Redraw the canvas
    fig.canvas.draw_idle()

# 6. Attach the update function to the sliders
slider_x.on_changed(update)
slider_y.on_changed(update)
slider_z.on_changed(update)

plt.show()