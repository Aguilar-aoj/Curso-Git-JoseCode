import os

# Ruta del directorio con los archivos
directorio = 'C:/Users/Saimon/Pictures/Screenshots'

# Obtener la lista de archivos en el directorio
archivos = os.listdir(directorio)

# Filtrar solo los archivos que terminan en .png
archivos_png = [archivo for archivo in archivos if archivo.endswith('.png')]

# Renombrar los archivos
for i, archivo in enumerate(archivos_png, start=1):
    ruta_actual = os.path.join(directorio, archivo)
    nuevo_nombre = os.path.join(directorio, f'{i}.png')
    os.rename(ruta_actual, nuevo_nombre)

print("Los archivos han sido renombrados correctamente.")