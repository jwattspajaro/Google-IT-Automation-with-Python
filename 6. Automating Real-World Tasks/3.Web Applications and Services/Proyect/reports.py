from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate(filename, title, additional_info, table_data):
  # Obtenemos un conjunto de estilos de muestra
  styles = getSampleStyleSheet()

  # Creamos un objeto SimpleDocTemplate
  report = SimpleDocTemplate(filename)

  # Creamos el título del informe y un párrafo con información adicional
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])

  # Definimos el estilo de la tabla
  table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]
  
  # Creamos la tabla con los datos y el estilo definidos
  report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

  # Creamos un espacio vacío para separar elementos
  empty_line = Spacer(1,20)

  # Construimos el informe
  report.build([report_title, empty_line, report_info, empty_line, report_table])
