# import os
#
# # Ruta de la carpeta donde se encuentran los archivos
# carpeta = os.path.join(os.path.dirname(__file__), "training\\usb_female")
#
# # Obtener una lista de los nombres de los archivos en la carpeta
# archivos = os.listdir(carpeta)
#
# # Iterar sobre cada archivo en la lista
# for i, nombre_archivo in enumerate(archivos):
#     # Construir el nuevo nombre del archivo (aquí puedes aplicar cualquier lógica de renombrado)
#     nuevo_nombre = f"usb_female ({i + 1}).jpg"
#
#     # Construir la ruta completa del archivo antiguo y el nuevo nombre
#     ruta_antigua = os.path.join(carpeta, nombre_archivo)
#     ruta_nueva = os.path.join(carpeta, nuevo_nombre)
#     try:
#         # Renombrar el archivo
#         os.rename(ruta_antigua, ruta_nueva)
#     except FileExistsError:
#         pass


# MAIN FILE
# THIS IS THE EXEC NN FILE

from flask import Flask, render_template, jsonify, Response, request
# from flask_cors import CORS
import cv2
from keras.models import load_model
import numpy as np

app = Flask(__name__, static_url_path='/src', static_folder='src')

model = load_model('modelo.h5')


@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', message='No file part')
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', message='No selected file')
        if file:
            img_bytes = file.split(',')[1]
            img = cv2.imdecode(np.fromstring(img_bytes.decode('base64'), np.uint8), cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (64, 64))
            img = np.array(img).reshape(-1, 64, 64, 1)
            prediction = model.predict(img)
            classes = ['usb_female', 'usb_male', 'hdmi_female', 'hdmi_male', 'plug_type_a_female', 'plug_type_a_male',
                       'plug_type_c_male', 'plug_type_c_female', 'vga_male', 'vga_female', 'ethernet_female',
                       'ethernet_male']
            prediction_class = classes[np.argmax(prediction)]
            return render_template('result.html', predicted_class=prediction_class)
    return render_template('index2.html')


if __name__ == "__main__":
    app.run(debug=True)
