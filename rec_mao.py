import cv2
import mediapipe as mp
import pyttsx3

video = cv2.VideoCapture(0)

hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
while True:
    check, img = video.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hand.process(imgRGB)
    handPoints = results.multi_hand_landmarks
    h, w, _ = img.shape
    pontos = []
    if handPoints:
        for points in handPoints:
            mpDraw.draw_landmarks(img, points, hand.HAND_CONNECTIONS)
            for id, cord in enumerate(points.landmark):
                cx, cy = int(cord.x*w), int(cord.y*h)
                #cv2.putText(img, str(id), (cx, cy+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                pontos.append((cx, cy))

        dedos = [8, 12, 16, 20]
        contador = 0
        if points:
            if pontos[4][0] < pontos[2][0]:
                contador += 1
            for x in dedos:
                if pontos[x][1] < pontos[x-2][1]:
                    contador += 1
        cv2.putText(img, str(contador), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 5)
        if contador == 0:
            text = "Você está com 0 dedos levantados"
            engine.say(text)
            engine.runAndWait()
        if contador == 1:
            text = "Você está com 1 dedo levantado"
            engine.say(text)
            engine.runAndWait()
        if contador == 2:
            text = "Você está com 2 dedos levantados"
            engine.say(text)
            engine.runAndWait()
        if contador == 3:
            text = "Você está com 3 dedos levantados"
            engine.say(text)
            engine.runAndWait()
        if contador == 4:
            text = "Você está com 4 dedos levantados"
            engine.say(text)
            engine.runAndWait()
        if contador == 5:
            text = "Você está com 5 dedos levantados"
            engine.say(text)
            engine.runAndWait()
    cv2.imshow("imagem", img)
    cv2.waitKey(1)