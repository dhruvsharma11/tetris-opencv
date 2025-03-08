import cv2
from utils.hand_tracker import HandTracker
from utils.gesture_interpreter import interpret_gesture
import mediapipe as mp

# Initialize hand tracking
hand_tracker = HandTracker()
cap = cv2.VideoCapture(0)

# Load MediaPipe for handedness detection
mp_hands = mp.solutions.hands

# https://tetris.com/play-tetris

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip frame horizontally for a mirror effect (to detect correct hand)
    frame = cv2.flip(frame, 1)

    # Detect hand landmarks
    results = hand_tracker.detect_hand(frame)

    if results.multi_hand_landmarks:
        for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
            handedness = (
                results.multi_handedness[i].classification[0].label
            )  # "Left" or "Right"

            interpret_gesture(hand_landmarks.landmark, handedness)

            # Draw hand landmarks
            mp.solutions.drawing_utils.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
            )

            # Display text
            cv2.putText(
                frame,
                f"{handedness} Hand Detected",
                (10, 50 + i * 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
            )

    cv2.imshow("Tetris Hand Controller - Dual Hand", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
