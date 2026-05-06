# Webcam Color-Controlled Webots E-puck

This project allows for real-time control of a Webots E-puck robot by tracking a colored object (like a red ball or a blue block) using a webcam. The robot moves based on the object's position within the camera frame.

## 🚀 How It Works
The system utilizes **OpenCV** for image processing and **UDP Sockets** for communication.
- **Python (Vision Script):** Captures video, converts it to the HSV color space, and applies a mask to isolate a specific color. It then calculates the "center of mass" (centroid) of the color.
- **Webots (Robot Controller):** Receives positional commands and drives the motors accordingly.

## 🕹️ Control Logic
The camera feed is divided into a grid. The robot's behavior depends on where the colored object is detected:

| Object Position | Robot Action |
| :--- | :--- |
| **Top Section** | Move Forward |
| **Bottom Section** | Move Backward |
| **Left Section** | Turn Left |
| **Right Section** | Turn Right |
| **No Color Detected** | **STOP** |

## 🛠️ Setup
1. **Dependencies:**
   ```bash
   pip install opencv-python numpy
