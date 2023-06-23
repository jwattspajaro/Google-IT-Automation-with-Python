### Classes and Methods Cheat Sheet (Optional)

#### Classes and Methods Cheat Sheet

In the past few videos, we’ve seen how to define classes and methods in Python. Here, you’ll find a run-down of everything we’ve covered, so you can refer to it whenever you need a refresher.

``` PYTHON
class ClassName:
    def method_name(self, other_parameters):
        body_of_method
```
Classes and Instances

- Classes define the behavior of all instances of a specific class.

- Each variable of a specific class is an instance or object.

- Objects can have attributes, which store information about the object.

- You can make objects do work by calling their methods.

- The first parameter of the methods (self) represents the current instance.

- Methods are just like functions, but they can only be used through a class.

#### Special methods

- Special methods start and end with __.

- Special methods have specific names, like __init__ for the constructor or __str__ for the conversion to string.

#### Documenting classes, methods and functions
- You can add documentation to classes, methods, and functions by using docstrings right after the definition. Like this:

``` PYTHON
class ClassName:
    """Documentation for the class."""
    def method_name(self, other_parameters):
        """Documentation for the method."""
        body_of_method
        
def function_name(parameters):
    """Documentation for the function."""
    body_of_function

```
----
### Hoja de referencia de clases y métodos (opcional)

#### Hoja de referencia de clases y métodos

En los últimos videos, hemos visto cómo definir clases y métodos en Python. Aquí encontrará un resumen de todo lo que hemos cubierto, para que pueda consultarlo cuando necesite un repaso.

``` PYTHON
class ClassName:
    def method_name(self, other_parameters):
        body_of_method
```
Clases e instancias

- Las clases definen el comportamiento de todas las instancias de una clase específica.

- Cada variable de una clase específica es una instancia u objeto.

- Los objetos pueden tener atributos, que almacenan información sobre el objeto.

- Puedes hacer que los objetos funcionen llamando a sus métodos.

- El primer parámetro de los métodos (self) representa la instancia actual.

- Los métodos son como funciones, pero solo se pueden usar a través de una clase.

#### Métodos especiales

- Los métodos especiales comienzan y terminan con __.

- Los métodos especiales tienen nombres específicos, como __init__ para el constructor o __str__ para la conversión a cadena.

#### Documentación de clases, métodos y funciones
- Puede agregar documentación a clases, métodos y funciones usando cadenas de documentación justo después de la definición. Como esto:
``` PYTHON
class ClassName:
    """Documentation for the class."""
    def method_name(self, other_parameters):
        """Documentation for the method."""
        body_of_method
        
def function_name(parameters):
    """Documentation for the function."""
    body_of_function

```
