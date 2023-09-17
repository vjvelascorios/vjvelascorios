import os
import random

# Ruta al archivo que contiene tu documento
documento_path = '/home/vjvelascorios/Documentos/GitHub/vjvelascorios/README.md'

# Ruta al directorio de imágenes
imagenes_dir = '/home/vjvelascorios/Documentos/GitHub/vjvelascorios/figures/'

# Leer el contenido del documento
with open(documento_path, 'r') as file:
    contenido = file.read()

# Buscar la etiqueta '{{IMAGEN}}' en el contenido
if '{{IMAGEN}}' in contenido:
    # Obtener la lista de archivos de imágenes en el directorio "images/"
    imagenes = [f for f in os.listdir(imagenes_dir) if os.path.isfile(os.path.join(imagenes_dir, f))]

    # Seleccionar una imagen al azar
    imagen_aleatoria = random.choice(imagenes)

    # Reemplazar '{{IMAGEN}}' con la nueva imagen en el documento
    nuevo_contenido = contenido.replace('{{IMAGEN}}', f'![Random photo here]({imagen_aleatoria})')

    # Escribir el contenido actualizado de vuelta al documento
    with open(documento_path, 'w') as file:
        file.write(nuevo_contenido)

    print(f'Se ha cambiado la imagen a: {imagen_aleatoria}')
else:
    print('La etiqueta {{IMAGEN}} no se encontró en el documento.')

