import cv2
import face_recognition


# Função de redimensionamento
def redim(img, largura):
    alt = int(img.shape[0] / img.shape[1] * largura)
    img = cv2.resize(img, (largura, alt), interpolation=cv2.INTER_AREA)
    return img



def detectar_faces(frame):

    frame = 'C:\Users\sofia\Downloads\face1.jpg'
    """ Detecta rostos na câmera, recorta e gera os encodings """
    # Carrega o classificador Haar Cascade
    df = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
    
    '''# Inicia a captura da webcam
    camera = cv2.VideoCapture(0)

    while True:
        sucesso, frame = camera.read()
            break'''

        frame = redim(frame, 640)  # Redimensiona para melhor visualização
        frame_pb = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Converte para tons de cinza

        # Detecta rostos na imagem
        faces = df.detectMultiScale(frame_pb, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

        # Para armazenar os encodings das faces detectadas
        face_encodings = []

        # Processa cada rosto detectado
        for (x, y, lar, alt) in faces:
            # Desenha um retângulo ao redor do rosto
            cv2.rectangle(frame, (x, y), (x + lar, y + alt), (0, 255, 255), 2)

            # Recorta a região do rosto na imagem original (BGR)
            face_img = frame[y:y + alt, x:x + lar]

            # Obtém o encoding do rosto
            face_encoding = find_face_recognition(face_img)

            if face_encoding is not None:
                face_encodings.append(face_encoding)

        # Exibe o frame com os rostos detectados
        cv2.imshow('Detector de Faces', frame)

        # Pressione 's' para sair
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

    # Libera a câmera e fecha as janelas
    camera.release()
    cv2.destroyAllWindows()

        if not sucesso:
    # Retorna os encodings das faces detectadas
    return face_encodings

#funcao que carrega uma imagenm, tranforma em sua correspondencia de 128 e retorna esse valor
def find_face_recognition(face_img):
    """ Recebe um frame (recorte do rosto), transforma em encoding de 128 dimensões e retorna """
    # O face_recognition espera imagens no formato RGB
    face_rgb = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)

    face_enc = face_recognition.face_encodings(face_rgb)

    return face_enc[0] if face_enc else None  # Retorna o encoding se houver rosto detectado


image_rec_1 = find_face_recognition('C:\Users\sofia\Downloads\face1.jpg')

print(image_rec_1)