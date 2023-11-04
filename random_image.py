import os
import random
import re

# Ruta al archivo que contiene tu documento
documento_path = '/home/vjvelascorios/Documentos/GitHub/vjvelascorios/README.md'

# Ruta al directorio de imágenes
imagenes_dir = '/home/vjvelascorios/Documentos/GitHub/vjvelascorios/figures/'

# Leer el contenido del documento
with open(documento_path, 'r') as file:
    contenido = file.read()

# Define el patrón de expresión regular para buscar la parte "![Random photo here](figures/tqmpatio.jpg)"
patron = r'!\[Random photo here\]\(figures/[^)]+\.(jpg|jpeg|png|gif|bmp|tiff)\)'

# Buscar el patrón en el contenido
coincidencia = re.search(patron, contenido)

# Si se encontró el patrón
if coincidencia:
    # Seleccionar una imagen al azar del directorio de imágenes
    imagen_aleatoria = random.choice(os.listdir(imagenes_dir))

    # Construir la ruta completa de la nueva imagen
    nueva_ruta_imagen = f'figures/{imagen_aleatoria}'

    # Reemplazar el patrón con la nueva imagen en el documento
    nuevo_contenido = re.sub(patron, f'![Random photo here]({nueva_ruta_imagen})', contenido)

    # Escribir el contenido actualizado de vuelta al documento
    with open(documento_path, 'w') as file:
        file.write(nuevo_contenido)

    print(f'Se ha cambiado la imagen a: {nueva_ruta_imagen}')
else:
    print('No se encontró el patrón en el documento.')

