import time
from utils.game_controller import (
    move_right,
    move_left,
    rotate_right,
    soft_drop,
    hard_drop,
    hold_piece,
)

# Separate action timestamps for each hand
last_action_time = {"Right": 0, "Left": 0}
ACTION_DELAY = 0.6


def interpret_gesture(landmarks, hand_type):
    """Detects gestures for both hands independently using all finger positions."""

    global last_action_time
    current_time = time.time()

    if current_time - last_action_time[hand_type] < ACTION_DELAY:
        return

    wrist = landmarks[0]
    thumb_tip, thumb_ip, thumb_mcp = landmarks[4], landmarks[3], landmarks[2]
    index_tip, index_pip, index_mcp = landmarks[8], landmarks[6], landmarks[5]
    middle_tip, middle_pip, middle_mcp = landmarks[12], landmarks[10], landmarks[9]
    ring_tip, ring_pip, ring_mcp = landmarks[16], landmarks[14], landmarks[13]
    pinky_tip, pinky_pip, pinky_mcp = landmarks[20], landmarks[18], landmarks[17]

    if hand_type == "Right":
        # --- Soft Drop (Index Finger points down, All Other Fingers above index) ---
        if (
            index_tip.y > wrist.y  # Index is lower than the wrist
            and index_tip.y > middle_mcp.y
            and index_tip.y > ring_mcp.y
            and index_tip.y > pinky_mcp.y
        ):
            print(
                "[DEBUG] Gesture Detected → Soft Drop (Index Lower Than Wrist AND Finger Bases)"
            )
            soft_drop()

        # --- Rotate Right (Index Finger Up, Other Fingers Neutral) ---
        elif (
            index_tip.y < wrist.y
            and index_tip.y < middle_tip.y
            and thumb_tip.y > index_tip.y
            and ring_tip.y > index_tip.y
            and pinky_tip.y > index_tip.y
            and index_tip.z < wrist.z
        ):
            print("[DEBUG] Gesture Detected → Rotate Right (Index Finger Raised)")
            rotate_right()

        # --- Move Right (Swipe Index Right, Thumb Below Index) ---
        elif (
            index_tip.x > wrist.x
            and thumb_tip.y < index_tip.y
            and thumb_tip.x < index_tip.x
            and index_tip.z < wrist.z
        ):
            print("[DEBUG] Gesture Detected → Move Right (Index Swipe Right)")
            move_right()

        # --- Move Left (Swipe Index Left, Thumb Below Index) ---
        elif (
            index_tip.x < wrist.x
            and thumb_tip.y < index_tip.y
            and thumb_tip.x > index_tip.x
            and index_tip.z < wrist.z
        ):
            print("[DEBUG] Gesture Detected → Move Left (Index Swipe Left)")
            move_left()

    if hand_type == "Left":
        # --- Hold Piece (All Fingers Down, Forming a Fist) ---
        if (
            pinky_tip.y > pinky_mcp.y
            and index_tip.y > index_mcp.y
            and middle_tip.y > middle_mcp.y
            and ring_tip.y > ring_mcp.y
        ):
            print("[DEBUG] Gesture Detected → Hold Piece (Fist Gesture)")
            hold_piece()

        # --- Hard Drop (All Fingers Fully Extended) ---
        elif (
            thumb_tip.y < thumb_mcp.y
            and index_tip.y < index_mcp.y
            and middle_tip.y < middle_mcp.y
            and ring_tip.y < ring_mcp.y
            and pinky_tip.y < pinky_mcp.y
            and index_tip.z < wrist.z
        ):
            print("[DEBUG] Gesture Detected → Hard Drop (All Fingers Raised)")
            hard_drop()

    last_action_time[hand_type] = current_time
