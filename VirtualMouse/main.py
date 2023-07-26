import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
hd = mp.solutions.hands.Hands()
dru = mp.solutions.drawing_utils
screen_w, screen_h = pyautogui.size()
index_y = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_h, frame_w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    output = hd.process(image=rgb_frame)  # Pass rgb_frame as the 'image' parameter

    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            dru.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=15, color=(0, 255, 255))
                    index_x = screen_w / frame_w * x
                    index_y = screen_h / frame_h * y
                    pyautogui.moveTo(index_x, index_y)
                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=15, color=(0, 255, 255))
                    thumb_x = screen_w / frame_w * x
                    thumb_y = screen_h / frame_h * y
                    if abs(index_y - thumb_y) < 20:
                        pyautogui.click()
                        pyautogui.sleep(1)
                if id == 20:
                    cv2.circle(img=frame, center=(x, y), radius=15, color=(0, 255, 255))
                    little_x = screen_w / frame_w * x
                    little_y = screen_h / frame_h * y
                    if abs(thumb_y - little_y) < 20:
                        pyautogui.rightClick()
                        pyautogui.sleep(1)
                if id == 12:
                    cv2.circle(img=frame, center=(x, y), radius=15, color=(0, 255, 255))
                    big_x = screen_w / frame_w * x
                    big_y = screen_h / frame_h * y
                    movement = int(abs(index_y - thumb_y))
                    if abs(index_y - big_y) < 10:
                        pyautogui.scroll(clicks=-movement)
                    elif abs(index_y - big_y) in range(10,20):
                        pyautogui.scroll(clicks=movement)

    cv2.imshow("Virtual Mouse", frame)
    cv2.waitKey(1)
