from enum import Enum


class gesture(Enum):
    pinky_up = handLms.landmark[20].y < handLms.landmark[19].y < handLms.landmark[18].y < handLms.landmark[10].y < handLms.landmark[11].y  < handLms.landmark[12].y