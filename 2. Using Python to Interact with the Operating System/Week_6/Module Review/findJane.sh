#!/bin/bash

# Crear el archivo "oldFiles.txt"
> oldFiles.txt

# Obtener la lista de archivos que contienen " jane " en "../data/list.txt" y extraer la tercera columna
files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)

# Recorrer cada archivo en la lista
for f in $files; do
  # Verificar si el archivo existe en la ubicación $HOME$f
  if [ -e $HOME$f ]; then
    # Si el archivo existe, agregar la ruta completa al archivo "oldFiles.txt"
    echo $HOME$f >> oldFiles.txt
  fi
done
