from keras.models import load_model
import cv2
import numpy as np

model = load_model('modelo.h5')

image_path = input("Por favor, ingrese la ruta de la imagen: ")

image_path = image_path.strip('"')

img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

img = cv2.resize(img, (64, 64))
img = np.array(img).reshape(-1, 64, 64, 1)

#HACER LA PREDICCION
prediction = model.predict(img)

#OBTENER LA CLASE PREDICHA
classes = ['usb_female', 'usb_male', 'hdmi_female', 'hdmi_male', 'plug_type_a_female', 'plug_type_a_male', 'plug_type_c_male', 'plug_type_c_female', 'vga_male', 'vga_female', 'ethernet_female', 'ethernet_male']
prediction_class = classes[np.argmax(prediction)]

print(f'la clase predicha es:{prediction_class}')
