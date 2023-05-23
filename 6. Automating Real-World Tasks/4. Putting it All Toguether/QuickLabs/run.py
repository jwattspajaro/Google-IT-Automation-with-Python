import os
import requests
import re

desc_path = 'supplier-data/descriptions/'
image_path = 'supplier-data/images/'

text_files = sorted(os.listdir(desc_path))
jpeg_images = sorted([image_name for image_name in os.listdir(image_path) if image_name.endswith('.jpeg')])

list_content = []

for file in text_files:
    with open(os.path.join(desc_path, file), 'r') as f:
        data = {}
        contents = f.read().split("\n")[:3]
        contents[1] = int(re.search(r'\d+', contents[1]).group())

        data['name'], data['weight'], data['description'] = contents
        data['image_name'] = jpeg_images[len(list_content)]

        list_content.append(data)

for item in list_content:
    resp = requests.post('http://127.0.0.1:80/fruits/', json=item)
    if resp.status_code != 201:
        raise Exception('Error al hacer POST, estado={}'.format(resp.status_code))
    print('Creado ID de retroalimentación: {}'.format(resp.json()["id"]))

