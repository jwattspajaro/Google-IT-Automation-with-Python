#!/usr/bin/env python3

import operator

fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
# Ordena los elementos del diccionario según las claves (orden predeterminado)
# El resultado es una lista de tuplas ordenadas alfabéticamente por las claves
sorted(fruit.items())
# Output: sorted(fruit.items())

# Ordena los elementos del diccionario según las claves utilizando operator.itemgetter(0)
# El resultado es una lista de tuplas ordenadas alfabéticamente por las claves
sorted(fruit.items(), key=operator.itemgetter(0))
# Output: [('apples', 5), ('bananas', 7), ('oranges', 3), ('pears', 2)]

# Ordena los elementos del diccionario según los valores utilizando operator.itemgetter(1)
# El resultado es una lista de tuplas ordenadas por los valores de forma ascendente
sorted(fruit.items(), key=operator.itemgetter(1))
# Output: [('pears', 2), ('oranges', 3), ('apples', 5), ('bananas', 7)]

# Ordena los elementos del diccionario según los valores utilizando operator.itemgetter(1) y en orden descendente
# El resultado es una lista de tuplas ordenadas por los valores de forma descendente
sorted(fruit.items(), key=operator.itemgetter(1), reverse=True)
# Output: [('bananas', 7), ('apples', 5), ('oranges', 3), ('pears', 2)]
