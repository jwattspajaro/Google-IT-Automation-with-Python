### How to Use PIL for Working With Images
#### Como mencionamos, para el proyecto de este módulo, utilizará la biblioteca de imágenes de Python para procesar un montón de imágenes. Entonces, ¿cómo funciona eso?

Cuando usamos PIL, normalmente creamos objetos de imagen que contienen los datos asociados con las imágenes que queremos procesar. En estos objetos, operamos llamando a diferentes métodos que devuelven un nuevo objeto de imagen o modifican los datos en la imagen, y luego terminan guardando el resultado en un archivo diferente.

Por ejemplo, si quisiéramos cambiar el tamaño de una imagen y guardar la nueva imagen con un nuevo nombre, podríamos hacerlo con:

```python
12345
from PIL import Image
im = Image.open("example.jpg")
new_im = im.resize((640,480))
new_im.save("example_resized.jpg")

```

In this case, we're using the resize method that returns a new image with the new size, and then we save it into a different file. Or, if we want to rotate an image, we can use code like this:

5234

from PIL import Image
im = Image.open("example.jpg")
new_im = im.rotate(90)
new_im.save("example_rotated.jpg")

This method also returns a new image that we can then use to create the new rotated file. Because the methods return a new object, we can even combine these operations into just one line that rotates, resizes, and saves:

1234
from PIL import Image
im = Image.open("example.jpg")
im.rotate(180).resize((640,480)).save("flipped_and_resized.jpg")

There's a ton more that you can do with the PIL library. Have a look at the docs and try it on your computer! 
