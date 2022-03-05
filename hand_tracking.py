import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
cTime = 0
pTime = 0
flag_kleinfinger = False
flag_set_true = False

while True:
    success, img=cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # print(handLms.landmark[20].x)
            enum_landmarks = enumerate(handLms.landmark)
            dict_landmarks = list(enum_landmarks)
            h,w,c=img.shape
            #for id,lm in enumerate(handLms.landmark):
                # print(id,lm )
            #    cx,cy = int(lm.x*w),int(lm.y*h)
            #    print(id,cx,cy)
            #    cv2.putText(img, str(id), (cx,cy), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0,0,0), 2)
            
            if handLms.landmark[20].y < handLms.landmark[19].y < handLms.landmark[18].y < handLms.landmark[10].y < handLms.landmark[11].y  < handLms.landmark[12].y  :
                # cv2.putText(img, 'Kleinfinger', (int(dict_landmarks[20][1].x*w), int(dict_landmarks[20][1].y*h)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
                cv2.putText(img, 'Kleinfinger', (int(handLms.landmark[20].x*w), int(handLms.landmark[20].y*h)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)

                flag_kleinfinger = True
            else:
                # cv2.putText(img, 'down-finger', (int(dict_landmarks[20][1].x*w), int(dict_landmarks[20][1].y*h)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1)
                flag_kleinfinger = False
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
            if flag_kleinfinger:
                if not flag_set_true:
                    print("Kleinfinger")
                    flag_set_true = True
            else:
                if flag_set_true:
                    print("downfinger")
                    flag_set_true = False

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX_SMALL,3,(255,0,255),2)


    cv2.imshow("img", img)
    cv2.waitKey(1)
    if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break