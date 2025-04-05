import dlib
import cv2
import os
import json
import tkinter as tk
from tkinter import simpledialog

def redim(img, largura):
    if img is None:
        return None
    alt = int(img.shape[0] / img.shape[1] * largura)
    return cv2.resize(img, (largura, alt), interpolation=cv2.INTER_AREA)

def detect_face(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).astype("uint8")  
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return faces #retorna uma tupla do tipo num py contendo as coordenadas do rosto detectado 


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
# json_file = "frames.json"

face_count = 0
video_capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    sucesso, frame = video_capture.read()

    if not sucesso or frame is None:
        print('Erro ao capturar o frame')
        break

    frame = redim(frame, 900) 
    faces = detect_face(frame)         
    

    cv2.imshow("captura de video", frame)
    key =  cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    elif key == 13: 

        nome_facial = frame_dados_user("Informe seu nome")
        

        # if os.path.exists(json_file):
        #     try:
        #         with open(json_file, 'r') as file:
        #             frames = json.load(file)
        #     except json.JSONDecodeError:
        #         frames = {}
        # else:
        #     frames = {}

        # frames[nome_facial] = list(faces)

        # with open(json_file, 'w') as file:
                
        #     json.dump(frames, file, indent=4)  
        #     print(f"Rosto '{nome_facial}' salvo com sucesso!")     
            

            
        
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                face_count = save_cropped_face(frame, x, y, w, h, nome_facial, face_list)
            


video_capture.release()
cv2.destroyAllWindows()

print("Faces salvas na lista:")
for count, face in face_list:
    print(f"Rosto {count}: {face_list}")