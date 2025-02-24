import dlib
import cv2
import timeit

lista = []

# Função de redimensionamento
def redim(img, largura):
    alt = int(img.shape[0] / img.shape[1] * largura)
    img = cv2.resize(img, (largura, alt), interpolation=cv2.INTER_AREA)
    return img

def detectar_face():
    # Carregar detector de rosto HOG
    hog_face_detector = dlib.get_frontal_face_detector()

    # Capturar vídeo da webcam
    video_capture = cv2.VideoCapture(0)

    while True:
        # Ler um frame do vídeo
        sucesso, frame = video_capture.read()
        
        # Verificar se o frame foi capturado corretamente
        if not sucesso:
            break

        frame = redim(frame, 320)
        # Converter para escala de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar rostos
        faces = hog_face_detector(gray)

        # Desenhar retângulos ao redor dos rostos detectados
        frame_temp = frame.copy()
        for face in faces:
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Exibir o frame com os rostos detectados
        cv2.imshow("Rostos detectados", redim(frame_temp, 640))

        # Pressionar 'q' para sair
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

        # Liberar a captura e fechar as janelas
        video_capture.release()
    
cv2.destroyAllWindows()
iteracoes = 1
# Usando o timeit para medir o tempo de execução da função
tempo_execucao = timeit.timeit(detectar_face, number=iteracoes)
num_lista = round(tempo_execucao / iteracoes, 4) 
lista.append(num_lista)
print(f"Tempo total de execução: {tempo_execucao} segundos")
print(lista)