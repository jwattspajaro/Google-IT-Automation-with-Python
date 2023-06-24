def character_frequency(filename):
    '''Cuenta la frecuencia de cada carácter en el archivo dado.'''
    try:
        with open(filename) as f:  # Abre el archivo en un contexto de lectura
            characters = {}  # Diccionario para almacenar los caracteres y su frecuencia

            # Itera sobre cada línea del archivo
            for line in f:
                # Itera sobre cada carácter de la línea
                for char in line:
                    characters[char] = characters.get(char, 0) + 1  # Incrementa la frecuencia del carácter

            return characters  # Devuelve el diccionario con la frecuencia de los caracteres

    except OSError:
        return None  # Si ocurre un error al abrir el archivo, devuelve None
