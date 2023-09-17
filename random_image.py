import os
import random

# Ruta al documento
documento_path = '/home/vjvelascorios/Documentos/GitHub/vjvelascorios/README.md'

# Imágenes
imagenes_dir = '/home/vjvelascorios/Documentos/GitHub/vjvelascorios/figures/'

# Leer el contenido del documento
with open(documento_path, 'r') as file:
    contenido = file.read()

# Obtener la lista de archivos de imágenes en el directorio "images/"
imagenes = [f for f in os.listdir(imagenes_dir) if os.path.isfile(os.path.join(imagenes_dir, f))]

# Seleccionar una imagen al azar
imagen_aleatoria = random.choice(imagenes)

# Reemplazar la antigua línea de la imagen en el documento con la nueva imagen
nuevo_contenido = contenido.replace('![Random photo here](figures/yes.jpeg)', f'![Random photo here]({imagen_aleatoria})')

# Escribir el contenido actualizado de vuelta al documento
with open(documento_path, 'w') as file:
    file.write(nuevo_contenido)

print(f'Se ha cambiado la imagen a: {imagen_aleatoria}')
