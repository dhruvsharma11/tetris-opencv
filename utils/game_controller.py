import pyautogui


def move_right():
    """Press right arrow key to move piece right."""
    pyautogui.press("right")


def move_left():
    """Press left arrow key to move piece left."""
    pyautogui.press("left")


def rotate_right():
    """Press up arrow key to rotate piece right."""
    pyautogui.press("up")


def rotate_left():
    """Press 'Z' key to rotate piece left."""
    pyautogui.press("z")


def soft_drop():
    """Press down arrow key to soft drop."""
    pyautogui.press("down")


def hard_drop():
    """Press space key for hard drop."""
    pyautogui.press("space")


def hold_piece():
    """Press 'C' key to hold piece."""
    pyautogui.press("c")
