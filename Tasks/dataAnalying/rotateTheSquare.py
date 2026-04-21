from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

def main() -> None:
    fig = plt.figure(figsize=(8, 8))
    ax = plt.axes(projection='3d')

    # Each row is a point: [X, Y, Z]
    vertices = np.array([
        [0, 0, 0],  # Point 1: Bottom-left
        [1, 0, 0],  # Point 2: Bottom-right
        [1, 1, 0],  # Point 3: Top-right
        [0, 1, 0]   # Point 4: Top-left
    ])

    # Stack the first row onto the bottom of the array
    closed_square = np.vstack((vertices, vertices[0]))

    print("Closed Square Coordinates:")
    print(closed_square)
    
    # Extract x, y, z coordinates
    x = closed_square[:, 0]
    y = closed_square[:, 1]
    z = closed_square[:, 2]

    # Plot the square
    ax.plot3D(x, y, z, color='blue', linewidth=2)

    ax.set_title('Rotate the square')
    plt.show()
    return None

if __name__ == "__main__":
    main()