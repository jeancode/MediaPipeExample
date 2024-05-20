import cv2
import mediapipe as mp

#ruta del video
ruta_video = './test.mp4'

#capturar video
cap = cv2.VideoCapture(ruta_video)

#inicializar
mp_hands =  mp.solutions.hands
hands =  mp_hands.Hands()



while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Fin del Video o error al leer el frame")
        break

    height, width, _ = frame.shape
    newHeight =  int(height / 2)
    newwidth = int(width / 2)

    # Redimensionar el fotograma al nuevo tamaño deseado
    new_video_resize = cv2.resize(frame, (newwidth,newHeight))

    #procesamo
    results  =  hands.process(new_video_resize)

    if results.multi_hand_landmarks:
        
        for hand_landmarks in results.multi_hand_landmarks:

            for point  in hand_landmarks.landmark:

                x,y = int(point.x * newwidth) , int(point.y * newHeight)

                cv2.circle(new_video_resize,(x,y),5,(0,255,50),-1)
                
            


    # Mostrar el fotograma con la mano izquierda detectada
    cv2.imshow("VIDEO", new_video_resize)

    # Salida del programa
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()