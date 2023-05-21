#!/usr/bin/env python3

import os
from PIL import Image

# El camino (path) ya no necesita ser expandido.
path = 'supplier-data/images/'

for file in os.listdir(path):
    # Verificar si la extensión del archivo es '.tiff' 
    if os.path.splitext(file)[1] == '.tiff':
        # Convertir de RGBA a RGB y luego redimensionar la imagen.
        img = Image.open(os.path.join(path, file)).convert("RGB")

        filename = os.path.splitext(file)[0]  # obtener el nombre del archivo sin la extensión

        # Guardar la imagen procesada en el mismo directorio, pero con una extensión .jpeg
        img.resize((600, 400)).save(os.path.join(path, f"{filename}.jpeg") , 'jpeg')
