import os
import requests

def send_feedback(directory):
    """
    Esta función recorre todos los archivos .txt en el directorio especificado,
    crea un diccionario a partir de su contenido y luego realiza una solicitud POST a un sitio web con el diccionario como JSON.
    Args:
        directory: Directorio donde se encuentran los archivos de retroalimentación.
    Returns:
        None
    """
    # Lista todos los archivos .txt en el directorio de retroalimentación
    for file in os.listdir(directory): 
        format = ["title","name","date","feedback"]
        content = {}

        # Abre cada archivo, lee las líneas y las guarda en el diccionario 'content'
        with open(f'{directory}/{file}', 'r') as txtfile:
            for index, line in enumerate(txtfile):
                line = line.replace("\n", "")
                content[format[index]] = line.strip('\n')

        # Realiza una solicitud POST a la dirección del sitio web con el diccionario 'content' como JSON
        response = requests.post("http://35.225.95.53/feedback/", json=content)

        # Comprueba si la solicitud POST ha tenido éxito
        if not response.ok:
            raise Exception(f"POST failed! | Status code: {response.status_code} | File: {file}")
        print("Feedback added!")

if __name__ == '__main__':
    dir = "/data/feedback/"
    send_feedback(dir)
