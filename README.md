# VisionPointer
Here is a **well-structured, detailed explanation** of your project **#VisionPointer: Real-Time Eye Movement Cursor Simulation**, written in a clear and professional format for your GitHub README:

---

# 👁️ VisionPointer: Real-Time Eye Movement Cursor Simulation

## 📌 Overview

**VisionPointer** is a real-time eye tracking system that simulates cursor movement based on the direction of a user's eye movement using a webcam. It uses **OpenCV's Haar Cascade Classifier** to detect eyes and then estimates whether the user is looking **left**, **right**, or **center**, simulating the corresponding cursor movement.

This project can serve as the foundation for:

* Assistive technologies (for users with physical disabilities),
* Hands-free computer control interfaces,
* Human-computer interaction (HCI) research.

---

## 🔧 Features

* Detects eyes in real-time using Haar cascades.
* Estimates gaze direction (LEFT, RIGHT, CENTER).
* Simulates cursor movement with print statements (can be extended to actual cursor control).
* Visual feedback via live video feed with bounding boxes over detected eyes.
* Simple and beginner-friendly implementation using OpenCV and Python.

---

## 📷 How It Works – Detailed Breakdown

### 1. **Eye Detection (`detect_eyes()`)**

This function uses **Haar cascade classifiers** trained to detect human eyes from the video frame:

```python
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
```

* Converts the frame to grayscale for faster processing.
* Uses OpenCV’s built-in `haarcascade_eye.xml` file to detect eyes.
* Returns a list of bounding box coordinates for detected eyes.

---

### 2. **Gaze Direction Estimation (`get_cursor_direction()`)**

Determines whether the user is looking **left**, **right**, or **center** based on the position of the first detected eye:

```python
center_x = x + w // 2
```

* The eye's horizontal center (`center_x`) is compared against the frame's width.
* Based on thresholds:

  * Left third → "LEFT"
  * Middle third → "CENTER"
  * Right third → "RIGHT"

---

### 3. **Cursor Movement Simulation (`simulate_cursor_movement()`)**

A placeholder function that simulates cursor behavior using print statements:

```python
if direction == "LEFT":
    print("Moving cursor LEFT")
```

* This can later be replaced with **PyAutoGUI**, **serial communication**, or **USB HID device code** to control the actual cursor.

---

### 4. **Main Function (`main()`)**

This is the driver function:

* Captures live video using `cv2.VideoCapture(0)`.
* Continuously reads frames and detects eyes.
* Estimates eye direction and simulates cursor movement.
* Draws rectangles on detected eyes for visualization.
* Quits when the user presses **‘q’**.

```python
while True:
    ret, frame = cap.read()
    ...
    eyes = detect_eyes(frame)
    direction = get_cursor_direction(eyes, frame.shape[1])
    simulate_cursor_movement(direction)
```

---

## 🧠 Possible Enhancements

* Replace print simulation with **actual mouse movement** using [`pyautogui.moveRel()`](https://pyautogui.readthedocs.io/en/latest/mouse.html).
* Add support for **head pose estimation** for more robust control.
* Improve detection using **Dlib**, **MediaPipe**, or **Deep Learning-based** models.
* Integrate with an **Arduino or Raspberry Pi** for hardware applications.
* Implement **calibration steps** for more accurate cursor mapping.

---

## 🧪 Requirements

* Python 3.x
* OpenCV

### 📦 Install Dependencies

```bash
pip install opencv-python numpy
```

---
---

## 📁 Project Structure

```
VisionPointer/
├── vision_pointer.py       # Main Python file
├── README.md               # Project documentation
```

---

## 🤝 Contributing

Contributions and ideas are welcome! Feel free to fork this repository, submit issues, or suggest improvements.

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

---

