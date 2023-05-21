import emails
import reports 
import json
import locale
import sys
import collections
import operator
import os

def load_data(filename):
  # Carga el contenido de filename como un archivo JSON.
  with open(filename) as json_file:
    data = json.load(json_file)
  return data

def format_car(car):
  # Dado un diccionario de coches, devuelve un nombre formateado adecuadamente.
  return "{} {} ({})".format(car["car_make"], car["car_model"], car["car_year"])

def process_data(data):
  # Analiza los datos, buscando los valores máximos.
  # Devuelve una lista de líneas que resumen la información.
  locale.setlocale(locale.LC_ALL, "C.UTF-8")
  max_revenue = {"revenue": 0}
  max_sales = {"total_sales": 0}
  car_year_sales = collections.defaultdict(int)

  for item in data:
    # Calcula los ingresos generados por este modelo (precio * ventas totales)
    # Necesitamos convertir el precio de "$1234.56" a 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item

    # TODO: También maneja las ventas máximas
    if item["total_sales"] > max_sales["total_sales"]:
      max_sales = item

    # Suma las ventas de cada año de coche
    car_year_sales[item["car"]["car_year"]] += item["total_sales"]

  # TODO: También maneja el año de coche más popular
  popular_car_year = max(car_year_sales.items(), key=operator.itemgetter(1))

  summary = [
    "The {} generated the most revenue: ${}".format(format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}".format(format_car(max_sales["car"]), max_sales["total_sales"]),
    "The most popular year was {} with {} sales.".format(popular_car_year[0], popular_car_year[1])
  ]

  return summary

def cars_dict_to_table(car_data):
  # Convierte los datos en car_data en una lista de listas.
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data

def main(argv):
  # Procesa los datos JSON y genera un informe completo a partir de ellos.
  data = load_data("car_sales.json")
  summary = process_data(data)
  
  # TODO: convierte esto en un informe en PDF
  filename = "/tmp/cars.pdf"
  title = "Sales summary for last month"
  additional_info = "<br/>".join(summary)
  table_data = cars_dict_to_table(data)
  reports.generate(filename, title, additional_info, table_data)

  # TODO: envía el informe en PDF como un adjunto de correo electrónico
  sender = "automation@example.com"
  recipient = "{}@example.com".format(os.environ.get('USER'))
    # Define el asunto del correo
  subject = "Sales summary for last month"
  
  # Define el cuerpo del correo electrónico con el resumen
  body = "\n".join(summary)
  
  # Define la ruta del archivo adjunto (el informe en PDF)
  attachment_path = "/tmp/cars.pdf"
  
  # Genera el mensaje de correo electrónico con el archivo adjunto
  message = emails.generate(sender, recipient, subject, body, attachment_path)
  
  # Envía el mensaje de correo electrónico
  emails.send(message)
  
# Comprueba si este archivo se está ejecutando como el archivo principal (es decir, no se está importando desde otro script)
if __name__ == "__main__":
  main(sys.argv)
