import cv2
import numpy as np
import matplotlib.pyplot as plt

# Path to video
video_path = 'animal.avi'

# Initialize video capture
cap = cv2.VideoCapture(video_path)

# Parameters for drawing the path
trajectory = []  # List to store tracked positions

# Define a function to process each frame
def detect_object(frame):
    # Convert to HSV (useful for color filtering)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define lower and upper bounds for the object's color (adjust as needed)
    lower_bound = np.array([30, 150, 50])  # Example for green
    upper_bound = np.array([80, 255, 255])
    
    # Create a mask for the object's color
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    
    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        # Assume the largest contour corresponds to the object
        c = max(contours, key=cv2.contourArea)
        # Get the object's center
        M = cv2.moments(c)
        if M["m00"] > 0:  # Avoid division by zero
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            return (cx, cy)
    return None

# Process video frame-by-frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Detect object
    position = detect_object(frame)
    
    if position:
        trajectory.append(position)  # Save position
        # Draw the trajectory on the frame
        for i in range(1, len(trajectory)):
            cv2.line(frame, trajectory[i - 1], trajectory[i], (0, 0, 255), 2)
    
    # Display the frame
    cv2.imshow('Object Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Extract and plot the curve
trajectory = np.array(trajectory)
if trajectory.size > 0:
    plt.plot(trajectory[:, 0], trajectory[:, 1], '-o', label='Object Path')
    plt.gca().invert_yaxis()  # Invert y-axis to match video coordinates
    plt.title('Object Path Curve')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.legend()
    plt.show()
