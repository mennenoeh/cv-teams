import cv2
import mediapipe as mp
import time
import os
# import mss
from PIL import Image
import pyautogui
from time import sleep
import win32gui
from gesture import Gesture
import wnd

MONITOR_NAME = "Teams Gesture Control"
WEBCAM_NR = 1 # zweite Cam benötig
SHOW_MONITOR = True
DEMO_MODE = False

cap = cv2.VideoCapture(WEBCAM_NR)
mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils


gesture = Gesture.NO_GESTURE

def get_img_from_cam():
    success, img=cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img, imgRGB

def get_gesture_from_lms(handLms) -> Gesture:
    gesture = None
    if handLms.landmark[20].y < handLms.landmark[19].y < handLms.landmark[18].y < handLms.landmark[10].y < handLms.landmark[11].y  < handLms.landmark[12].y  :
        gesture = Gesture.PINKY_UP
    elif handLms.landmark[8].y < handLms.landmark[7].y < handLms.landmark[6].y < handLms.landmark[5].y < handLms.landmark[19].y  < handLms.landmark[20].y  :
        gesture = Gesture.INDEX_FINGER_UP
    elif handLms.landmark[4].y < handLms.landmark[3].y < handLms.landmark[6].y :
        gesture = Gesture.THUMB_UP
    else:
        gesture = Gesture.NO_GESTURE
    
    return gesture

def draw_gesture_on_image(img, handLms, gesture: Gesture, mpHands) -> None:
    mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    h,w,c=img.shape
    cv2.putText(img, 
        str(gesture.value["action"]), 
        (int(handLms.landmark[gesture.value["landmark_nr"]].x*w), int(handLms.landmark[gesture.value["landmark_nr"]].y*h)), 
        cv2.FONT_HERSHEY_COMPLEX_SMALL, 
        fontScale=2, 
        color=(255,255,255), 
        thickness=2)


with mpHands.Hands(max_num_hands = 1, min_detection_confidence=0.8, min_tracking_confidence=0.8) as hands:
    while cap.isOpened():
        img, imgRGB = get_img_from_cam()
        results = hands.process(imgRGB)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                gesture_new = get_gesture_from_lms(handLms)
                
                if SHOW_MONITOR or DEMO_MODE:
                    draw_gesture_on_image(img=img, handLms=handLms, gesture=gesture_new, mpHands=mpHands)
            
            if gesture_new != gesture:
                    gesture = gesture_new
                    if gesture == Gesture.PINKY_UP:
                        if not DEMO_MODE:
                            wnd.set_recent_teams_window_active()
                            pyautogui.hotkey('ctrl', 'shift', 'm')
                        print(Gesture.PINKY_UP)
                    elif gesture == Gesture.INDEX_FINGER_UP:
                        if not DEMO_MODE:
                            wnd.set_recent_teams_window_active()
                            pyautogui.hotkey('ctrl', 'shift', 'k')
                        print(Gesture.INDEX_FINGER_UP)
                    elif gesture == Gesture.THUMB_UP:
                        if not DEMO_MODE:
                            wnd.set_recent_teams_window_active()
                            # screen_x, screen_y = print(pyautogui.locateCenterOnScreen("./img/reactions.png"))
                            # pyautogui.click(screen_x, screen_y)
                        print(Gesture.THUMB_UP)
                    elif gesture == Gesture.NO_GESTURE:
                        print(Gesture.NO_GESTURE)
    

        if SHOW_MONITOR or DEMO_MODE:
            cv2.imshow(MONITOR_NAME, img)
        cv2.waitKey(1)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            cap.release()
            break

