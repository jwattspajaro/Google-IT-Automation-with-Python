import sys
import subprocess

# Obtener el nombre del archivo de la línea de comandos
file = sys.argv[1]

# Abrir el archivo en modo lectura
with open(file) as f:
    # Leer cada línea del archivo
    for line in f.readlines():
        # Eliminar los espacios en blanco al inicio y final de la línea
        source = line.strip()

        # Reemplazar 'jane' por 'jdoe' en el nombre de archivo
        destination = source.replace('jane', 'jdoe')

        # Ejecutar el comando 'mv' para renombrar el archivo
        subprocess.run(['mv', source, destination])

    # Cerrar el archivo
    f.close()
