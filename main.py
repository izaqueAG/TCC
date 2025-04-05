

import cv2
import face_recognition
import tkinter as tk
from tkinter import simpledialog

def redim(img, largura):
    if img is None:
        return None
    alt = int(img.shape[0] / img.shape[1] * largura)
    return cv2.resize(img, (largura, alt), interpolation=cv2.INTER_AREA)

def detect_face(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  
    face_detected = face_cascade.detectMultiScale(rgb, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in face_detected:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return face_detected #retorna uma tupla do tipo num py contendo as coordenadas do rosto detectado 

#funcao que carrega uma imagenm, tranforma em sua correspondencia de 128 e retorna esse valor
def find_face_recognition(faces, face_list):
    for faces in face_list:
        face_enc = face_recognition.face_encodings(faces)     

def save_cropped_face(frame, x, y, w, h, entrada_usuario, face_list):
    
    face = frame[y:y+h, x:x+w]
    
    face_list.append((entrada_usuario, face))
    print(f"Rosto {entrada_usuario}")
     

def frame_dados_user(mensagem):
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    entrada_usuario = simpledialog.askstring("entrada", mensagem)
    return entrada_usuario
    




    
face_list = []


face_count = 0
video_capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    sucesso, frame = video_capture.read()

    if not sucesso or frame is None:
        print('Erro ao capturar o frame')
        break

    frame = redim(frame, 900) 
    face_detected = detect_face(frame)         
    

    cv2.imshow("captura de video", frame)
    key =  cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    elif key == 13: 

        nome_facial = frame_dados_user("Informe seu nome")        

            
        
        if len(face_detected) > 0:
            for (x, y, w, h) in face_detected:
                face_count = save_cropped_face(face_detected, x, y, w, h, nome_facial, face_list)
            


video_capture.release()
cv2.destroyAllWindows()

print("Faces salvas na lista:")
for count, face in face_list:
    print(f"Rosto {count}: {face_list}")