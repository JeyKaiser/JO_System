import pandas as pd
import os

def convert_xlsx_to_csv(xlsx_file_path, csv_file_path):
    try:
        # Leer el archivo Excel
        df = pd.read_excel(xlsx_file_path, engine='openpyxl')
        
        # Guardar como CSV con codificación UTF-8
        df.to_csv(csv_file_path, index=False, sep=',', encoding='utf-8')
        print(f"Archivo convertido exitosamente a {csv_file_path}")
    
    except FileNotFoundError:
        print(f"Error: El archivo {xlsx_file_path} no existe.")
    
    except PermissionError:
        print(f"Error: No se tiene permiso para escribir en {csv_file_path}.")
    
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    # Ruta del archivo .xlsx con cadenas sin formato o dobles barras
    xlsx_file_path = r"C:\Users\USUARIO\Desktop\parametros.xlsx"
    
    # Ruta del archivo .csv de salida
    csv_file_path = r"C:\Users\USUARIO\Desktop\Libro1.csv"
    
    # Llamar la función para convertir el archivo
    convert_xlsx_to_csv(xlsx_file_path, csv_file_path)
