import csv
import os

import qrcode

# 
archivo_csv = 'basededatosempleados.csv'
columna_cedula = 'Cedula'
columna_nombre = 'Nombre'
directorio_salida = 'codigos_qr'

def generar_codigos_qr(nombreArchivo, columna_cedula, columna_nombre, dir_salida):

    if not os.path.exists(dir_salida):
        os.makedirs(dir_salida)
        print(f"Carpeta '{dir_salida}' creada con exito!.")

    try:
        with open(nombreArchivo, mode="r",encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for fila in reader:
                cedula = fila[columna_cedula].strip()
                nombre = fila[columna_nombre].strip()

                datos_qr = f"(cedula)"

                #configurar QR

                qr = qrcode.QRCode(
                version = 1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size = 10,
                border = 4

                )

                #Añadir datos al QR

                qr.add_data(datos_qr)
                qr.make(fit=True)

                #Crear la imagen del QR

                img = qr.make_image(fill_color="black",back_color="white")

                #Guardar imagen del QR

                nombreArchivo = os.path.join(dir_salida, f"{cedula}.png")
                img.save(nombreArchivo)
    except Exception as error:
        print(f"Error al generar codigo QR {error}")

generar_codigos_qr(archivo_csv, columna_cedula, columna_nombre, directorio_salida)
