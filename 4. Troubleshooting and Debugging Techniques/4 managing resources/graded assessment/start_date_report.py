#!/usr/bin/env python3

import csv
import datetime
import requests

def download_file(url):
    """Descarga el archivo desde la URL dada y devuelve sus líneas."""
    response = requests.get(url, stream=True)
    lines = []

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def get_start_date():
    """Obtiene de manera interactiva la fecha de inicio para consultar."""

    print()
    print('Obteniendo la primera fecha de inicio para consultar.')
    print()
    print('La fecha debe ser posterior al 1 de enero de 2018')
    year = int(input('Ingrese un valor para el año: '))
    month = int(input('Ingrese un valor para el mes: '))
    day = int(input('Ingrese un valor para el día: '))
    print()

    return datetime.datetime(year, month, day)

def get_same_or_newer(data, start_date):
    """Devuelve los empleados que comenzaron en la fecha dada o la más cercana posterior."""
    min_date = datetime.datetime.today()
    min_date_employees = []

    for row in data:
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')

        if row_date < start_date:
            continue

        if row_date < min_date:
            min_date = row_date
            min_date_employees = []

        if row_date == min_date:
            min_date_employees.append("{} {}".format(row[0], row[1]))

    return min_date, min_date_employees

def list_newer(data, start_date):
    while start_date < datetime.datetime.today():
        start_date, employees = get_same_or_newer(data, start_date)
        print("Comenzado el {}: {}".format(start_date.strftime("%b %d, %Y"), employees))
        start_date += datetime.timedelta(days=1)

def main():
    start_date = get_start_date()
    FILE_URL = "https://storage.googleapis.com/gwg-hol-assets/gic215/employees-with-date.csv"
    data = download_file(FILE_URL)
    reader = csv.reader(data[1:])  # Omitir la primera línea (encabezados)
    data_list = list(reader)
    data_list.sort(key=lambda x: x[3])  # Ordenar los datos por fecha de inicio
    list_newer(data_list, start_date) 

if __name__ == "__main__":
    main()
