#!/usr/bin/env python3

import re

line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
# Utiliza una expresión regular para buscar el patrón específico en la línea
# Encuentra "ticky: INFO: Created ticket " seguido de cualquier combinación de palabras y espacios
# La expresión regular captura este patrón en un grupo
# El resultado es un objeto de coincidencia que muestra el índice de inicio y fin de la coincidencia, y la propia coincidencia
result_info = re.search(r"ticky: INFO: ([\w ]*) ", line)
print(result_info)

line = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"
# Utiliza una expresión regular similar para buscar el patrón específico en la línea
# Encuentra "ticky: ERROR: Error creating ticket " seguido de cualquier combinación de palabras y espacios
# La expresión regular captura este patrón en un grupo
# El resultado es un objeto de coincidencia que muestra el índice de inicio y fin de la coincidencia, y la propia coincidencia
result_error = re.search(r"ticky: ERROR: ([\w ]*) ", line)
print(result_error)
