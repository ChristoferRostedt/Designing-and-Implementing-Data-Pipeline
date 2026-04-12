import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

# --- 1. Configuration and Setup ---
# Set the time logic (frames and speed)
fps = 20  # Frames per second (animation smoothness)
countdown_sec = 5  # Length of the countdown
travel_sec = 6  # Length of the flight time

total_sec = countdown_sec + travel_sec
total_frames = int(total_sec * fps)
launch_frame = int(countdown_sec * fps)  # The specific frame launch begins

# Set up the visual boundary
space_x_lim = (-50, 50)
space_y_lim = (-10, 110)

# Define planetary positions
earth_radius = 8
moon_center = np.array([0, 100])  # Target x,y coordinate for lunar arrival
moon_radius = 5

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor("#0a0a20")  # Very dark blue background for space
ax.set_xlim(space_x_lim)
ax.set_ylim(space_y_lim)
ax.set_title("Mission: Two Rockets to the Moon", color='white')

# Turn off standard axis numbers/ticks for cleaner look
ax.set_xticks([])
ax.set_yticks([])

# --- 2. Add Static Visuals (Background) ---
# Add scattered stars (background texture)
for _ in range(200):
    sx = random.randint(*space_x_lim)
    sy = random.randint(*space_y_lim)
    size = random.uniform(0.1, 1.5)
    ax.scatter(sx, sy, s=size, color='white', alpha=random.uniform(0.3, 0.8), zorder=0)

# Add Earth (Semi-circle at bottom)
earth_circle = plt.Circle((0, -3), earth_radius, color='dodgerblue', zorder=1)
ax.add_artist(earth_circle)

# Add Moon (Circle at top)
moon_circle = plt.Circle(moon_center, moon_radius, color='lightgray', zorder=1)
ax.add_artist(moon_circle)

# --- 3. Pre-calculate Data (No-Collision Logic) ---
# We define start points and paths to ensure separation
flight_frames_count = total_frames - launch_frame
frames_flight = np.linspace(0, 1, flight_frames_count)

# -- Rocket 1: Path curves slightly LEFT --
# Start slightly left on Earth's surface
R1_start = np.array([-4, 1])
# A "control point" to pull the curve left and higher before converging
R1_mid_left = np.array([-15, 60]) 

# Generate a Quadratic Bezier curve (B(t) = (1-t)^2*P0 + 2(1-t)t*P1 + t^2*P2)
r1_coords = ( (1-frames_flight)**2 * R1_start[:, np.newaxis] + 
               2*(1-frames_flight)*frames_flight * R1_mid_left[:, np.newaxis] + 
               frames_flight**2 * moon_center[:, np.newaxis] )

# -- Rocket 2: Path curves slightly RIGHT --
# Start slightly right on Earth's surface
R2_start = np.array([4, 1])
# A "control point" to pull the curve right and higher before converging
R2_mid_right = np.array([15, 60])

r2_coords = ( (1-frames_flight)**2 * R2_start[:, np.newaxis] + 
               2*(1-frames_flight)*frames_flight * R2_mid_right[:, np.newaxis] + 
               frames_flight**2 * moon_center[:, np.newaxis] )

# --- 4. Define Dynamic Objects (to be animated) ---
# We use marker '^' (upward pointing triangle) as rockets
rocket1, = ax.plot([], [], marker='^', markersize=12, color='#FF4500', 
                    label="Apollo (R1)", linestyle='None', zorder=5)
rocket2, = ax.plot([], [], marker='^', markersize=12, color='#FF8C00', 
                    label="Artemis (R2)", linestyle='None', zorder=5)
ax.legend(facecolor='white', framealpha=0.5, loc='upper right')

# Text elements (centered)
text_countdown = ax.text(0, 50, '', color='white', fontsize=28, 
                        fontweight='bold', ha='center', va='center', zorder=6)
text_time = ax.text(0, 5, '', color='#ffffffcc', fontsize=12, 
                    ha='center', va='center', zorder=6)

# --- 5. The Animation Core Logic ---
def update_flight(frame):
    # Calculate current mission time
    current_time_sec = frame / fps
    text_time.set_text(f"Mission Time: T+{current_time_sec:.1f}s")
    
    # PHASE A: COUNTDOWN
    if frame < launch_frame:
        # Calculate time remaining in countdown (5s down to 0s)
        time_until_launch = countdown_sec - current_time_sec
        # Round up to the nearest whole integer
        seconds_val = int(time_until_launch) + 1
        
        text_countdown.set_text(f"LIFTOFF IN:\n{seconds_val}")
        text_countdown.set_color('#ffddaa') # Orange glow during countdown
        
        # Keep rockets visible at their starting pads
        rocket1.set_data([R1_start[0]], [R1_start[1]])
        rocket2.set_data([R2_start[0]], [R2_start[1]])
        
        # No trail visible yet
        
        return rocket1, rocket2, text_countdown, text_time

    # PHASE B: ASCENT / FLIGHT
    else:
        # Determine the flight index (how far into the pre-calculated path)
        flight_idx = frame - launch_frame
        
        # Convert flight_idx to 'progress' between 0.0 and 1.0
        # Check against flight_frames_count - 1 to handle the final index
        current_flight_idx = min(flight_idx, flight_frames_count - 1)
        
        text_countdown.set_text("LIFTOFF!")
        text_countdown.set_color('#ccffcc') # Green success color during flight
        
        # Update rocket locations from pre-calculated NumPy data
        # Note: set_data requires sequences, so we wrap single numbers in lists
        r1_current_x = r1_coords[0, current_flight_idx]
        r1_current_y = r1_coords[1, current_flight_idx]
        rocket1.set_data([r1_current_x], [r1_current_y])
        
        r2_current_x = r2_coords[0, current_flight_idx]
        r2_current_y = r2_coords[1, current_flight_idx]
        rocket2.set_data([r2_current_x], [r2_current_y])
        
        # OPTIONAL: Keep countdown text briefly, then hide it
        if current_time_sec > (countdown_sec + 1.5):
             text_countdown.set_visible(False)
        
        # OPTIONAL: Stop rockets when they hit the moon radius
        # You would add complex stopping logic here if needed. 
        # This script runs them to the center of the moon then completes.
        
        # When both reach the target, change text
        if current_flight_idx == (flight_frames_count - 1):
             text_countdown.set_text("ARRIVAL SUCCESS!")
             text_countdown.set_visible(True)
             text_countdown.set_color('white')

        return rocket1, rocket2, text_countdown, text_time

# --- 6. Run and Display Animation ---
# interval determines speed: 1000ms / fps
# blit=True optimizes by only redrawing changed objects (rockets, text)
ani = animation.FuncAnimation(fig, update_flight, frames=total_frames, 
                              interval=1000/fps, blit=True, repeat=False)

plt.tight_layout()
plt.show()