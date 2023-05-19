### Primero, debes verificar si las imágenes se han guardado en el directorio '/opt/icons/'. Para hacer esto, puedes usar el siguiente comando en tu terminal:
bash

    ls /opt/icons
    
Si ves una lista de archivos .jpeg, eso significa que tu script ha funcionado correctamente.

Luego, para verificar las propiedades de las imágenes (como el formato y el tamaño), puedes usar el módulo Image de PIL en la consola de Python. Aquí están los pasos que puedes seguir:
Abre la consola de Python ejecutando el siguiente comando en tu terminal:


    python3

Una vez que se abre la consola de Python, importa el módulo Image de PIL con el siguiente comando:


    from PIL import Image
    
Abre cualquier imagen del directorio '/opt/icons/' con el siguiente comando (reemplaza 'nombre_de_imagen.jpeg' con el nombre real de tu imagen):


    img = Image.open("/opt/icons/nombre_de_imagen.jpeg")
    
Finalmente, para ver el formato y el tamaño de la imagen, puedes usar el siguiente comando:

    img.format, img.size
    
Esto te dará el formato de la imagen (que debería ser 'JPEG') y el tamaño de la imagen (que debería ser (128, 128)).

Para salir de la consola de Python, simplemente puedes escribir exit() y presionar Enter.

Si todo se ve bien, entonces tu script ha funcionado correctamente. Si no, por favor comparte cualquier error que estés viendo para que podamos ayudarte a solucionarlo.

Primero, debes verificar si las imágenes se han guardado en el directorio '/opt/icons/'. Para hacer esto, puedes usar el siguiente comando en tu terminal:

    ls /opt/icons
    
Luego, para verificar las propiedades de las imágenes (como el formato y el tamaño), puedes usar el módulo Image de PIL en la consola de Python.
Abre la consola de Python ejecutando el siguiente comando en tu terminal:


    python3
    
Una vez que se abre la consola de Python, importa el módulo Image de PIL con el siguiente comando:


    from PIL import Image
    
Abre cualquier imagen del directorio '/opt/icons/' con el siguiente comando (reemplaza 'nombre_de_imagen.jpeg' con el nombre real de tu imagen):


    img = Image.open("/opt/icons/nombre_de_imagen.jpeg")
    
Finalmente, para ver el formato y el tamaño de la imagen, puedes usar el siguiente comando:


    img.format, img.size
