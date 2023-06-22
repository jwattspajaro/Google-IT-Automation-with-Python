### ¡Felicitaciones! ¡Aprobaste!
Calificación recibida 100 %
Para Aprobar 80 % o más

#### 1. Pregunta 1
Let’s test your knowledge of using dot notation to access methods and attributes in an object. Let’s say we have a class called Birds. Birds has two attributes: color and number. Birds also has a method called count() that counts the number of birds (adds a value to number). Which of the following lines of code will correctly print the number of birds? Keep in mind, the number of birds is 0 until they are counted!

⬜  bluejay.number = 0

    print(bluejay.number)


⬜ print(bluejay.number.count())


☑️ bluejay.count()

    print(bluejay.number)


⬜ print(bluejay.number)

✅  Correcto
    Nice job! We must first call the count() method, which will populate the number attribute, allowing us to print number and receive a correct response.

Creating new instances of class objects can be a great way to keep track of values using attributes associated with the object. The values of these attributes can be easily changed at the object level. The following code illustrates a famous quote by George Bernard Shaw, using objects to represent people. Fill in the blanks to make the code satisfy the behavior described in the quote.

``` PYTHON
# "Si tienes una manzana y yo tengo una manzana y cambiamos estas manzanas, 
# tú y yo seguiremos teniendo una manzana cada uno. Pero si tienes una idea y yo 
# tengo una idea y cambiamos estas ideas, entonces cada uno de nosotros tendrá dos ideas."
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
    # Aquí, a pesar de la cita de G.B. Shaw, nuestros personajes han comenzado con
    # diferentes cantidades de manzanas para poder observar mejor los resultados.
    # Vamos a hacer que Martin y Johanna intercambien TODAS sus manzanas entre sí.
    # Pista: ¿cómo intercambiarías los valores de las variables para que "you" y "me"
    # intercambien TODAS sus manzanas entre sí?
    # ¿Necesitas una variable temporal para almacenar uno de los valores?
    # Es posible que necesites más de una línea de código para hacer eso, lo cual está bien.
    you.apples, me.apples = me.apples, you.apples
    return you.apples, me.apples

def exchange_ideas(you, me):
    # "you" y "me" compartirán nuestras ideas entre nosotros.
    # ¿Qué operaciones deben realizarse para que cada objeto reciba
    # el número compartido de ideas?
    # Pista: ¿cómo asignarías el número total de ideas a
    # cada atributo de ideas? ¿Necesitas una variable temporal para almacenar
    # la suma de ideas, o puedes encontrar otra manera?
    # Utiliza tantas líneas de código como necesites aquí.
    you.ideas += me.ideas
    me.ideas += you.ideas - me.ideas
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna tiene {} manzanas y Martin tiene {} manzanas".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna tiene {} ideas y Martin tiene {} ideas".format(johanna.ideas, martin.ideas))

```

Output:

``` PYTHON
Johanna has 2 apples and Martin has 1 apples
Johanna has 2 ideas and Martin has 2 ideas
```

<br>

### Question 3

The City class has the following attributes: name, country (where the city is located), elevation (measured in meters), and population (approximate, according to recent statistics). Fill in the blanks of the max_elevation_city function to return the name of the city and its country (separated by a comma), when comparing the 3 defined instances for a specified minimal population. For example, calling the function for a minimum population of 1 million: max_elevation_city(1000000) should return "Sofia, Bulgaria".

``` PYTHON
# define una clase básica de ciudad
class City:
    name = ""
    country = ""
    elevation = 0 
    population = 0

# crea una nueva instancia de la clase City y
# define cada atributo
city1 = City()
city1.name = "Cusco"
city1.country = "Perú"
city1.elevation = 3399
city1.population = 358052

# crea una nueva instancia de la clase City y
# define cada atributo
city2 = City()
city2.name = "Sofía"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# crea una nueva instancia de la clase City y
# define cada atributo
city3 = City()
city3.name = "Seúl"
city3.country = "Corea del Sur"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
    # Inicializa la variable que contendrá
    # la información de la ciudad con la elevación más alta
    return_city = City()

    # Evalúa la primera instancia para cumplir con los requisitos:
    # ¿la ciudad #1 tiene al menos min_population y
    # su elevación es la más alta evaluada hasta ahora?
    if city1.population > min_population and city1.elevation > return_city.elevation:
        return_city = city1
    # Evalúa la segunda instancia para cumplir con los requisitos:
    # ¿la ciudad #2 tiene al menos min_population y
    # su elevación es la más alta evaluada hasta ahora?
    if city2.population > min_population and city2.elevation > return_city.elevation:
        return_city = city2
    # Evalúa la tercera instancia para cumplir con los requisitos:
    # ¿la ciudad #3 tiene al menos min_population y
    # su elevación es la más alta evaluada hasta ahora?
    if city3.population > min_population and city3.elevation > return_city.elevation:
        return_city = city3

    # Formatea la cadena de retorno
    if return_city.name:
        return "{}, {}".format(return_city.name, return_city.country)
    else:
        return ""

print(max_elevation_city(100000))  # Debería imprimir "Cusco, Perú"
print(max_elevation_city(1000000))  # Debería imprimir "Sofía, Bulgaria"
print(max_elevation_city(10000000))  # Debería imprimir ""

```

Output:

``` PYTHON
Cusco, Peru
Sofia, Bulgaria
```

<br>

### Question 4

What makes an object different from a class?

⬜ An object represents and defines a concept

☑️  **An object is a specific instance of a class**
  
⬜An object is a template for a class

⬜ Objects don't have accessible variables

> Objects are an encapsulation of variables and functions into a single entity.

<br>

### Question 5

We have two pieces of furniture: a brown wood table and a red leather couch. Fill in the blanks following the creation of each Furniture class instance, so that the describe_furniture function can format a sentence that describes these pieces as follows: "This piece of furniture is made of {color} {material}"

``` PYTHON
class Furniture:
    color = ""
    material = ""

table = Furniture()
table.color = 'marrón'
table.material = 'madera'

couch = Furniture()
couch.color = 'rojo'
couch.material = 'cuero'

def describe_furniture(piece):
    return "Esta pieza de mobiliario está hecha de {} {}".format(piece.color, piece.material)

print(describe_furniture(table)) 
# Debería imprimir "Esta pieza de mobiliario está hecha de marrón madera"
print(describe_furniture(couch)) 
# Debería imprimir "Esta pieza de mobiliario está hecha de rojo cuero"

```

Output:

``` PYTHON
This piece of furniture is made of brown wood
This piece of furniture is made of red leather
```
