from PIL import Image
import argparse

def redimensionar_imagen(ruta_entrada, ruta_salida):
    """
    Redimensiona una imagen a 148x177 píxeles y la guarda
    """
    try:
        imagen = Image.open(ruta_entrada)
        # Redimensionar a 148 ancho x 177 alto
        tamaño_objetivo = (148, 177)
        imagen_redimensionada = imagen.resize(tamaño_objetivo)
        imagen_redimensionada.save(ruta_salida)
        print(f"Imagen redimensionada y guardada en: {ruta_salida}")
    except Exception as e:
        print(f"Error al procesar la imagen: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Redimensiona imágenes a 148x177 píxeles')
    parser.add_argument('entrada', help='Ruta de la imagen de entrada')
    parser.add_argument('salida', help='Ruta para guardar la imagen redimensionada')
    
    args = parser.parse_args() # Comentario4
    
    redimensionar_imagen(args.entrada, args.salida)