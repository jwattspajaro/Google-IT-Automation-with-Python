#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Verifica si el nombre de usuario recibido cumple con las condiciones requeridas."""
    # Comprueba si el nombre de usuario es una cadena
    if type(username) != str:
        raise TypeError("El nombre de usuario debe ser una cadena")
    # Comprueba si minlen es al menos 1
    if minlen < 1:
        raise ValueError("minlen debe ser al menos 1")

    # Los nombres de usuario no pueden ser más cortos que minlen
    if len(username) < minlen:
        return False

    # Los nombres de usuario solo pueden usar letras, números, puntos y guiones bajos
    if not re.match('^[a-z0-9._]*$', username):
        return False

    # Los nombres de usuario no pueden comenzar con un número
    if not username[0].isalpha():
        return False
    
    return True

# Prueba las validaciones de los usuarios
print(validate_user("blue.kale", 3))  # True
print(validate_user(".blue.kale", 3))  # Actualmente True, debería ser False
print(validate_user("red_quinoa", 4))  # True
print(validate_user("_red_quinoa", 4))  # Actualmente True, debería ser False
