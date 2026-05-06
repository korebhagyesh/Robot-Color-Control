import cv2
import socket
import numpy as np

# 1. Setup Network Connection
server_address = ('127.0.0.1', 5005)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

cap = cv2.VideoCapture(0)

print("--- Blue Finger Tracker Started ---")
print("Put BLUE TAPE on your index finger tip.")

while cap.isOpened():
    success, frame = cap.read()
    if not success: break

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Range for BRIGHT BLUE
    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([140, 255, 255])
    
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        largest = max(contours, key=cv2.contourArea)
        if cv2.contourArea(largest) > 200:
            M = cv2.moments(largest)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                x_normalized = cx / frame.shape[1]
                
                # Send position to Webots
                sock.sendto(str(x_normalized).encode(), server_address)
                
                # Visual feedback
                cv2.circle(frame, (cx, int(M["m01"] / M["m00"])), 15, (255, 0, 0), 2)

    cv2.imshow('Index Finger (Blue Tip) Control', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()