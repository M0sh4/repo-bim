import csv

def dividir_csv_27_archivos(archivo_entrada, filas_por_archivo=1730, numero_archivos=27):
    """
    Toma un archivo CSV y lo divide en 27 partes (por defecto),
    cada una con la cabecera idéntica y 'filas_por_archivo' filas diferentes.
    """
    
    with open(archivo_entrada, 'r', encoding='utf-8', newline='') as f_in:
        reader = csv.reader(f_in)
        
        # Leer la cabecera (asumiendo que la primera línea es la cabecera)
        header = next(reader)  # primera línea
        
        # Convertir el resto de filas en una lista
        # (puedes leerlas de manera distinta si el archivo es muy grande)
        all_rows = list(reader)
        
        # Verificar que hay suficientes filas
        total_filas = len(all_rows)
        requerido = filas_por_archivo * numero_archivos
        
        if total_filas < requerido:
            print(f"Advertencia: El archivo solo tiene {total_filas} filas de datos y "
                  f"se requieren {requerido} para 27 archivos con {filas_por_archivo} filas cada uno.")
            # Puedes decidir si detener o manejarlo de otra manera
            # return
        
        # Iniciar un índice para ir cortando
        start_idx = 0
        
        for i in range(numero_archivos):
            # Calcular el rango de filas para este archivo
            end_idx = start_idx + filas_por_archivo
            rows_chunk = all_rows[start_idx:end_idx]
            
            # Nombrar el archivo de salida, por ejemplo: parte_01.csv, parte_02.csv, etc.
            nombre_salida = f"parte_{i+1:02d}.csv"
            
            with open(nombre_salida, 'w', encoding='utf-8', newline='') as f_out:
                writer = csv.writer(f_out)
                
                # Escribir la cabecera
                writer.writerow(header)
                
                # Escribir las filas correspondientes
                writer.writerows(rows_chunk)
            
            print(f"Archivo '{nombre_salida}' creado con {len(rows_chunk)} filas de datos.")
            
            # Actualizar el índice de inicio para la siguiente iteración
            start_idx = end_idx

if __name__ == "__main__":
    archivo_csv = "load_test_Data.csv"  # Ajusta la ruta a tu archivo CSV
    dividir_csv_27_archivos(archivo_csv)
