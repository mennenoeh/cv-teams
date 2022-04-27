from enum import Enum

class Gesture(Enum):
    PINKY_UP = {"action" : "mute", "shortcut": ['ctrl', 'shift', 'm'], "landmark_nr": 20}
    INDEX_FINGER_UP = {"action" : "hand", "shortcut": ['ctrl', 'shift', 'k'], "landmark_nr": 8}
    THUMB_UP = {"action" : "thumbs up", "shortcut": ['ctrl', 'shift', 'k'], "landmark_nr": 4}
    THUMB_DOWN = {"action" : "thumbs down", "shortcut": ['ctrl', 'shift', 'k'], "landmark_nr": 4}
    NO_GESTURE = {"action" : "none", "landmark_nr": 0}

if __name__ == "__main__":
    print(Gesture.PINKY_UP.value["shortcut"]) # *
