import matplotlib.pyplot as plt
import csv
from datetime import datetime

archivo_csv = r'C:\Users\jeans\Documents\chatbot\data\data_et\data_processed.csv'

def graph_chart_values(nit):
    fechas_y_valores_por_nit = []

    try:
        with open(archivo_csv, 'r') as archivo:
            csv_reader = csv.reader(archivo)
            next(csv_reader)  # Omite la primera fila si contiene encabezados

            for fila in csv_reader:
                (
                    _, _, nit_de_la_entidad, _, _, _,
                    _, _, _, _,
                    _, _, valor_contrato, _, _,
                    _, _, fecha_de_firma_del_contrato, _, _,
                    _, _, _
                ) = fila

                if nit_de_la_entidad == nit:
                    # Formatea la fecha
                    fecha_firma_date = datetime.strptime(fecha_de_firma_del_contrato, "%m/%d/%Y").strftime("%Y-%m-%d")

                    # Agrega las fechas y valores relevantes a la lista
                    fechas_y_valores_por_nit.append({
                        'fecha_firma': fecha_firma_date,
                        'valor_contrato': float(valor_contrato)
                    })

    except FileNotFoundError:
        print("Error: El archivo CSV no se encuentra.")
    except Exception as e:
        print("Ocurrió un error inesperado:", str(e))
        return []

    return fechas_y_valores_por_nit

def graph_chart(nit):
    fechas_y_valores_por_nit = graph_chart_values(nit)

    if not fechas_y_valores_por_nit:
        print("No se encontraron datos para el NIT proporcionado.")
        return

    # Extrae las fechas y valores de la lista de diccionarios
    fechas = [item['fecha_firma'] for item in fechas_y_valores_por_nit]
    valores = [item['valor_contrato'] for item in fechas_y_valores_por_nit]

    # Genera la gráfica de barras
    plt.figure(figsize=(10, 6))
    plt.bar(fechas, valores)
    plt.xlabel('Fecha de Firma del Contrato')
    plt.ylabel('Valor del Contrato')
    plt.title(f'Gráfico de Barras para NIT {nit}')
    plt.xticks(rotation=90)# Puedes ajustar el valor para obtener el espaciado deseado
    plt.xticks(range(0, len(fechas), 1))
    plt.tight_layout()

    # Muestra la gráfica
    plt.show()


