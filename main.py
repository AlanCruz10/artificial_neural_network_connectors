import os

# Ruta de la carpeta donde se encuentran los archivos
carpeta = os.path.join(os.path.dirname(__file__), "training\\usb_female")

# Obtener una lista de los nombres de los archivos en la carpeta
archivos = os.listdir(carpeta)

# Iterar sobre cada archivo en la lista
for i, nombre_archivo in enumerate(archivos):
    # Construir el nuevo nombre del archivo (aquí puedes aplicar cualquier lógica de renombrado)
    nuevo_nombre = f"usb_female ({i + 1}).jpg"

    # Construir la ruta completa del archivo antiguo y el nuevo nombre
    ruta_antigua = os.path.join(carpeta, nombre_archivo)
    ruta_nueva = os.path.join(carpeta, nuevo_nombre)
    try:
        # Renombrar el archivo
        os.rename(ruta_antigua, ruta_nueva)
    except FileExistsError:
        pass



# # MAIN FILE
# # THIS IS THE EXEC NN FILE
#
# from flask import Flask, render_template, Response
# import cv2
# import pickle
# import mediapipe as mp
# import numpy as np
#
# app = Flask(__name__)
#
# model_dict = pickle.load(open('./data/models/model.p', 'rb'))
# model = model_dict['model']
#
# mp_hands = mp.solutions.hands
# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
#
# hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3, max_num_hands=2)
#
# cap = cv2.VideoCapture(0)
#
#
# def generate_frames():
#     while True:
#         ret, frame = cap.read()
#         frame = cv2.resize(frame, (800, 620))
#         H, W, _ = frame.shape
#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         results = hands.process(rgb_frame)
#         if results.multi_hand_landmarks:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 data_aux = []
#                 x_ = []
#                 y_ = []
#                 mp_drawing.draw_landmarks(
#                     frame,  # image to draw
#                     hand_landmarks,  # model output
#                     mp_hands.HAND_CONNECTIONS,  # hand connections
#                     mp_drawing_styles.get_default_hand_landmarks_style(),
#                     mp_drawing_styles.get_default_hand_connections_style())
#
#                 for i in range(len(hand_landmarks.landmark)):
#                     x = hand_landmarks.landmark[i].x
#                     y = hand_landmarks.landmark[i].y
#
#                     x_.append(x)
#                     y_.append(y)
#
#                 for i in range(len(hand_landmarks.landmark)):
#                     x = hand_landmarks.landmark[i].x
#                     y = hand_landmarks.landmark[i].y
#                     data_aux.append(x - min(x_))
#                     data_aux.append(y - min(y_))
#
#             x1 = int(min(x_) * W) - 10
#             y1 = int(min(y_) * H) - 10
#
#             x2 = int(max(x_) * W) - 10
#             y2 = int(max(y_) * H) - 10
#
#             prediction = model.predict([np.asarray(data_aux)])
#             print("prediction: ", prediction)
#
#             cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
#             cv2.putText(frame, str(prediction), (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
#                         cv2.LINE_AA)
#
#         ret, buffer = cv2.imencode('.jpg', frame)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/video_feed')
# def video_feed():
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
#
#
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8080)
