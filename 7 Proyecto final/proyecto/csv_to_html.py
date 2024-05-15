#!/usr/bin/env python3

import sys
import csv
import os

def process_csv(csv_file):
    """Convierte el contenido del archivo CSV en una lista de listas"""
    print("Procesando {}".format(csv_file))
    with open(csv_file,"r") as datafile:
        data = list(csv.reader(datafile))
    return data
    
def data_to_html(title, data):
    """Convierte una lista de listas en una tabla HTML"""

    # Encabezados HTML y estilo
    html_content = """
<html>
<head>
<style>
table {
  width: 25%;
  font-family: arial, sans-serif;
  border-collapse: collapse;
}

tr:nth-child(odd) {
  background-color: #dddddd;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}
</style>
</head>
<body>
"""

    # Añadir el encabezado con el título dado
    html_content += "<h2>{}</h2><table>".format(title)

    # Añadir cada fila en data como una fila en la tabla
    for i, row in enumerate(data):
        html_content += "<tr>"
        for column in row:
            if i == 0:
                html_content += "<th>{}</th>".format(column)
            else:
                html_content += "<td>{}</td>".format(column)
        html_content += "</tr>"

    html_content += """</tr></table></body></html>"""
    return html_content

def write_html_file(html_string, html_file):
    """Escribe el contenido HTML en un archivo"""

    # Comprueba si el archivo HTML ya existe
    if os.path.exists(html_file):
        print("{} ya existe. Sobrescribiendo...".format(html_file))

    with open(html_file,'w') as htmlfile:
        htmlfile.write(html_string)
    print("Tabla escrita correctamente en {}".format(html_file))

def main():
    """Verifica los argumentos de la línea de comandos y llama a la función de procesamiento"""

    # Verifica que se hayan incluido argumentos de línea de comandos
    if len(sys.argv) < 3:
        print("ERROR: ¡Falta argumento de línea de comandos!")
        print("Saliendo del programa...")
        sys.exit(1)
    
    # Abre los archivos
    csv_file = sys.argv[1]
    html_file = sys.argv[2]
    
    # Verifica que se incluyan las extensiones de archivo
    if ".csv" not in csv_file:
        print('¡Falta la extensión ".csv" en el primer argumento de línea de comandos!')
        print("Saliendo del programa...")
        sys.exit(1)
    
    if ".html" not in html_file:
        print('¡Falta la extensión ".html" en el segundo argumento de línea de comandos!')
        print("Saliendo del programa...")
        sys.exit(1)
    
    # Verifica que el archivo CSV exista
    if not os.path.exists(csv_file):
        print("{} no existe".format(csv_file))
        print("Saliendo del programa...")
        sys.exit(1)

    # Procesa los datos y los convierte en HTML
    data = process_csv(csv_file)
    title = os.path.splitext(os.path.basename(csv_file))[0].replace("_", " ").title()
    html_string = data_to_html(title, data)
    write_html_file(html_string, html_file)

if __name__ == "__main__":
    main()
