import time
from utils.game_controller import (
    move_right,
    move_left,
    rotate_right,
    rotate_left,
    soft_drop,
    hard_drop,
    hold_piece,
)

last_action_time = 0
ACTION_DELAY = 0.2


def interpret_gesture(landmarks, hand_type):
    """Detects gestures and maps them to Tetris actions based on hand type."""
    global last_action_time
    current_time = time.time()

    if current_time - last_action_time < ACTION_DELAY:
        return
    wrist = landmarks[0]
    index_tip = landmarks[8]
    thumb_tip = landmarks[4]
    pinky_tip = landmarks[20]

    if hand_type == "Right":
        # Right hand controls movement & rotation
        if index_tip.x > wrist.x + 0.1:  # Move Right
            move_right()
        elif index_tip.x < wrist.x - 0.1:  # Move Left
            move_left()
        elif index_tip.y < wrist.y - 0.1:  # Rotate Right (index finger raised)
            rotate_right()
        elif thumb_tip.y < wrist.y - 0.1:  # Rotate Left (thumb raised)
            rotate_left()
        elif index_tip.y > wrist.y + 0.1:  # Soft Drop
            soft_drop()

    elif hand_type == "Left":
        # Left hand controls hold piece + hard drop
        if pinky_tip.y > wrist.y + 0.1:  # Hold Piece (fist)
            hold_piece()
        elif all(
            [finger.y < wrist.y for finger in landmarks[4:21:4]]
        ):  # Hard Drop (all fingers raised)
            hard_drop()

    last_action_time = current_time
