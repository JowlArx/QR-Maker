#QR MAKER
import qrcode

def generar_qr(url, nombre_archivo):
    # Crear un objeto QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Añadir datos al código QR
    qr.add_data(url)
    qr.make(fit=True)
    
    # Crear una imagen del código QR
    imagen_qr = qr.make_image(fill_color="black", back_color="white")
    
    # Guardar la imagen con el nombre especificado
    imagen_qr.save(nombre_archivo)

# Ejemplo de uso
if __name__ == "__main__":
    url = input("Ingrese una URL: ")
    nombre_archivo = input("Ingrese el nombre del archivo: ") + ".png"
    generar_qr(url, nombre_archivo)
    print(f"Se ha generado el código QR en el archivo: {nombre_archivo}")
