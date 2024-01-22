"""
Description: Script to write in a Database the data processed and get it from SECOP
"""

import sqlalchemy
from sqlalchemy import create_engine, text
import os
import csv
import pymysql
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from dotenv import load_dotenv

#Loads the variables from the .env file into the environment, making them accessible to this application
load_dotenv()

pymysql.install_as_MySQLdb()

print(sqlalchemy.__version__)
print(os.getcwd())

def escribir_bd():
    # Construye la URL de conexión
    #mysqlConnString = 'mysql://usrProyecto:password@ec2-3-226-169-30.compute-1.amazonaws.com/DBPR202120'
    
    database_name = os.getenv("TEST")
    secret_database = os.getenv("admin")
    #print(f"database: {database_name}")
    #print(f"Secret: {secret_database}")
    mysqlConnString = f"mysql+pymysql://root:{secret_database}@localhost:3306/{database_name}"

    ### database connection
    # Crea el motor de SQLAlchemy con la URL de conexión
    engine = create_engine(mysqlConnString)

    # Abre y lee el archivo CSV
    try:
        with open(r'C:\Users\jeans\Documents\chatbot\data\data_et\data_processed.csv', 'r') as archivo_csv:
            csv_reader = csv.reader(archivo_csv)
            next(csv_reader)  # Omite la primera fila si contiene encabezados

            #Itera sobre las filas del archivo CSV e inserta los datos en la base de datos
            for fila in csv_reader:
                #Desempaqueta los valores de la fila
                                
                (
                    nivel_entidad, nombre_entidad, nit_entidad, departamento_entidad, municipio_entidad, 
                    estado_proceso, modalidad, objeto_contrato, objeto_proceso, tipo_de_contrato, 
                    numero_contrato, numero_proceso, valor_contrato, nombre_razon_social, url_contrato,
                    origen, documento_proveedor, fecha_firma, fecha_inicio, fecha_fin, 
                    year_firma, month_firma, fecha_firma_yyyymm
                ) = fila
                
                
                fecha_firma_date = datetime.strptime(fecha_firma, "%m/%d/%Y").strftime("%Y-%m-%d")
                documento_proveedor_str =  "'"+ str(documento_proveedor) + "'"
                year_firma_str = "'"+ str(year_firma) + "'"
                month_firma_str = "'"+ str(month_firma) + "'"
                

                #Formatea la consulta SQL con los valores
                query = text(f"""
                    INSERT INTO contrato (
                        nivel_entidad, nombre_entidad, nit_entidad, departamento_entidad, municipio_entidad, 
                        estado_proceso, modalidad, objeto_contrato, objeto_proceso, tipo_de_contrato, 
                        numero_contrato, numero_proceso, valor_contrato, nombre_razon_social, url_contrato, 
                        origen, documento_proveedor, fecha_firma, fecha_inicio, fecha_fin, 
                        year_firma, month_firma, fecha_firma_yyyymm
                    ) VALUES (
                        '{nivel_entidad}', '{nombre_entidad}', '{nit_entidad}', '{departamento_entidad}', '{municipio_entidad}',
                        '{estado_proceso}', '{modalidad}', '{objeto_contrato}', '{objeto_proceso}', '{tipo_de_contrato}',
                        '{numero_contrato}', '{numero_proceso}', {float(valor_contrato)}, '{nombre_razon_social}', '{url_contrato}',
                        '{origen}', {documento_proveedor_str}, '{fecha_firma_date}', '{fecha_inicio}', '{fecha_fin}', 
                        {year_firma_str}, {month_firma_str}, '{fecha_firma_yyyymm}'
                    )
                """)

                # Ejecuta la consulta SQL
                with engine.connect() as conexion:
                    conexion.execute(query)
                    conexion.commit()  # Confirma la transacción
            # query = text("Select * from contrato")
            # with engine.connect() as conexion:
            #     conexion.execute(query)


        print("Inserción de datos completada con éxito.")

    except FileNotFoundError:
        print("Error: El archivo CSV no se encuentra.")
    except SQLAlchemyError as e:
        print("Error de SQLAlchemy:", e)
        print(query)
        print(documento_proveedor_str)
        print(type(documento_proveedor_str))
    except Exception as e:
        print("Ocurrió un error inesperado:", str(e))


if __name__ == '__main__':
    escribir_bd()

