# line_follower.py
import cv2, requests, numpy as np

API = "http://localhost:5003/line"
cap = cv2.VideoCapture(0)  # webcam (replace with IP cam if needed)

while True:
    ret, frame = cap.read()
    if not ret: break

    # Convert to grayscale + threshold
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

    # Focus only on bottom part of frame (region of interest)
    h, w = thresh.shape
    roi = thresh[h//2:, :]  

    # Find contours
    contours, _ = cv2.findContours(roi, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cmd = "HOLD"
    if contours:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        if M["m00"] > 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"]) + h//2  # adjust y back

            # Draw centroid
            cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

            # Decide command
            if cx < w//3:
                cmd = "LEFT"
            elif cx > 2*w//3:
                cmd = "RIGHT"
            else:
                cmd = "FORWARD"

    # Show command
    cv2.putText(frame, f"CMD: {cmd}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Send to server
    requests.post(API, json={"cmd": cmd})

    # Show frames
    cv2.imshow("Line Follower", frame)
    cv2.imshow("Threshold", roi)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
