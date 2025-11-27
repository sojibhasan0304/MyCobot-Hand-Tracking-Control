import cv2
import mediapipe as mp
from pymycobot.mycobot import MyCobot
import time

# Connect to MyCobot
mycobot = MyCobot('COM22')  # or '/dev/ttyAMA0' for Raspberry Pi
mycobot.send_angles([0,0,0,0,0,0],20)
time.sleep(2)  # Let it initialize
base_angle=0

# MediaPipe setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Helper function to map coordinates to angles
def map_range(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# Start webcam
cap = cv2.VideoCapture(1)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue

        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                image_height, image_width, _ = image.shape

                wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
                wrist_x = int(wrist.x * image_width)
                wrist_y = int(wrist.y * image_height)

                # Map wrist position to angle ranges (for shoulder or base)
                base_angle = map_range(wrist_x, 0, image_width, -90, 90)
                shoulder_angle = map_range(wrist_y, 0, image_height, -135, 135)

                print(f"Wrist X: {wrist_x}, Y: {wrist_y} → Base: {base_angle}, Shoulder: {shoulder_angle}")

                

                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow('Hand Tracking', image)
        # Control the robot (use dummy values for other joints)
        mycobot.send_angles([base_angle, 0, 0, 0, 0, 0], 20)

        
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
