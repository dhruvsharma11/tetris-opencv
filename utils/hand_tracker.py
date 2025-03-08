import cv2
import mediapipe as mp


class HandTracker:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5
        )
        self.mp_draw = mp.solutions.drawing_utils

    def detect_hand(self, frame):
        """Detects hand and returns landmarks + handedness info."""
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)
        return results
