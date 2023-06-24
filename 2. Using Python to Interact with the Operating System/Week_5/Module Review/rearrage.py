import re

def rearrange_name(name):
    result = re.search(r'^([\w .]*), ([\w .]*)$', name)
    if result == None:
        # Si no se encuentra una coincidencia, se devuelve el nombre original sin cambios
        return name

    # Se reorganiza el nombre en el formato "nombre_apellido"
    return '{} {}'.format(result[2], result[1])
