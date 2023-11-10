# Importamos librerias para lecturas
import cv2
from pyzbar.pyzbar import decode
import numpy as np
import pyautogui, webbrowser
from time import sleep



# Creamos la videocaptura
cap = cv2.VideoCapture(0)
while True:
    nombre = input("Write your name Paps or 's' the end: ")
    if nombre.lower() == 's':
        break
    numero = input("Escribe tu numero con 52 1 al principio {}:".format(nombre))
# Vamos Max VERSTAPPEN
while True:
    # Leemos los frames
    ret, frame = cap.read()

    # Checamos los codigos QR
    for codes in decode(frame):
        # Extraemos info
        #info = codes.data

        # Decodidficamos
        info = codes.data.decode('utf-8')

        # Personalidades
        MAX = info[0:2]
        MAX = int(MAX)

        #  coordenadas
        pts = np.array([codes.polygon], np.int32)
        xi, yi = codes.rect.left, codes.rect.top

        # Redimensionamos
        pts = pts.reshape((-1,1,2))

        if MAX == 69:  # J->74 # E->69
            # Dibujamos
            cv2.polylines(frame, [pts], True, (255, 255, 0), 2)
            cv2.putText(frame, 'E0' + str(info[2:]), (xi - 15, yi - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 55, 0), 2)
            print(" El usuario es un poderosisimo INGENIERO  \n"
                  " Identificacion: E", str(info[2:]))

        if MAX == 71:  # F->70 # G->71
            # Sueña
            cv2.polylines(frame, [pts], True, (255, 0, 255), 2)
            cv2.putText(frame, 'G0' + str(info[2:]), (xi - 15, yi - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
            print(" El usuario es Stripper \n"
                  " Identificacion: G", str(info[2:]))

        if MAX == 83:  # C->99 # S->83
            # Sueña
            cv2.polylines(frame, [pts], True, (0, 255, 255), 2)
            cv2.putText(frame, 'S0' + str(info[2:]), (xi - 15, yi - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            print(" El usuario es un Bellako \n"
                  " Numero de Identificacion: S", str(info[2:]))

        if MAX == 65:  # C->99 # S->83
            # Sueña
            cv2.polylines(frame, [pts], True, (0, 255, 255), 2)
            cv2.putText(frame, 'A0' + str(info[2:]), (xi - 15, yi - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            print(" Identificacion: A", str(info[2:]))
        # Mostramos en pantalla
        print(info)
        webbrowser.open('https://web.whatsapp.com/send?phone=' + numero)

        sleep(10)

        for i in range(1):
            pyautogui.typewrite('Registro Exitoso, Cada dia mas Ingeniero' + info)
            pyautogui.press('enter')

    # se ve  FPS
    cv2.imshow(" LECTOR DE QR", frame)
    # leer el teclado
    t = cv2.waitKey(5)
    if t == 27:
        break

cv2.destroyAllWindows()
cap.release()

#Queremos un 10 un 10 un 10
