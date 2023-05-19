from PIL import Image
from glob import glob
import os

# Ruta de las imágenes
source_directory = "/home/student-01-1648c7ece53c/imagenes"

# Asegurarse de que el directorio de destino exista
destination_directory = "/opt/icons/"
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Iterar a través de cada archivo en el directorio de origen
for file in glob(os.path.join(source_directory, '*')):
    image = Image.open(file).convert('RGB')
    # print(image.format, image.size, image.mode) # Test

    # Rotar la imagen 90° en sentido horario
    rotated_image = image.rotate(-90)

    # Redimensionar la imagen de 192x192 a 128x128
    resized_image = rotated_image.resize((128, 128))

    # Guardar la imagen en el directorio de destino en formato .jpeg
    filename = os.path.basename(file)
    destination_path = os.path.join(destination_directory, os.path.splitext(filename)[0] + ".jpeg")
    resized_image.save(destination_path)

print('OK')
