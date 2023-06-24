#!/usr/bin/env python3

import operator

fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
sorted(fruit.items())
# Salida: sorted(fruit.items())

sorted(fruit.items(), key=operator.itemgetter(0))
# Salida: [('apples', 5), ('bananas', 7), ('oranges', 3), ('pears', 2)]

sorted(fruit.items(), key=operator.itemgetter(1))
# Salida: [('pears', 2), ('oranges', 3), ('apples', 5), ('bananas', 7)]

sorted(fruit.items(), key=operator.itemgetter(1), reverse=True)
# Salida: [('bananas', 7), ('apples', 5), ('oranges', 3), ('pears', 2)]

# En este código Python, se utiliza la función sorted() para ordenar los elementos del diccionario fruit.
# En la primera llamada a sorted(), los elementos del diccionario se ordenan en función de sus claves en orden ascendente. La salida muestra el resultado de la operación sorted(fruit.items()), que es una representación ordenada de los elementos del diccionario.
# En la segunda llamada a sorted(), los elementos del diccionario se ordenan en función de sus claves en orden ascendente utilizando operator.itemgetter(0) como clave de ordenamiento. La salida muestra una lista de tuplas ordenadas por clave en orden ascendente.
# En la tercera llamada a sorted(), los elementos del diccionario se ordenan en función de sus valores en orden ascendente utilizando operator.itemgetter(1) como clave de ordenamiento. La salida muestra una lista de tuplas ordenadas por valor en orden ascendente.
# En la cuarta llamada a sorted(), los elementos del diccionario se ordenan en función de sus valores en orden descendente utilizando operator.itemgetter(1) como clave de ordenamiento y especificando reverse=True. La salida muestra una lista de tuplas ordenadas por valor en orden descendente.
