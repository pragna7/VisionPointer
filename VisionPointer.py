#VisionPointer: Real-Time Eye Movement Cursor Simulation


import cv2
import numpy as np
import time
import os

# Optional: Use PyUSB or OS HID interface for USB cursor control
# For now, we'll simulate with print statements

def detect_eyes(frame):
    """Detects eyes using Haar cascades."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    return eyes

def get_cursor_direction(eye_coords, frame_width):
    """Estimate direction based on eye position in frame."""
    if len(eye_coords) == 0:
        return "NONE"

    (x, y, w, h) = eye_coords[0]  # Take the first detected eye
    center_x = x + w // 2

    if center_x < frame_width // 3:
        return "LEFT"
    elif center_x > (2 * frame_width) // 3:
        return "RIGHT"
    else:
        return "CENTER"

def simulate_cursor_movement(direction):
    """Simulate cursor control (replace with actual movement or serial send)."""
    if direction == "LEFT":
        print("Moving cursor LEFT")
    elif direction == "RIGHT":
        print("Moving cursor RIGHT")
    elif direction == "CENTER":
        print("Cursor at CENTER")
    else:
        print("No eyes detected")

def main():
    cap = cv2.VideoCapture(0)  # USB webcam

    if not cap.isOpened():
        print("Camera not found!")
        return

    print("Starting eye tracking...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        eyes = detect_eyes(frame)
        direction = get_cursor_direction(eyes, frame.shape[1])
        simulate_cursor_movement(direction)

        # Draw rectangles for visualization (optional)
        for (x, y, w, h) in eyes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Show frame (for debugging)
        cv2.imshow('Eye Tracker', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

main()

