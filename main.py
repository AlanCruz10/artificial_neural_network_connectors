import os

# Ruta de la carpeta donde se encuentran los archivos
carpeta = os.path.join(os.path.dirname(__file__), "training\\vga_female")

# Obtener una lista de los nombres de los archivos en la carpeta
archivos = os.listdir(carpeta)

# Iterar sobre cada archivo en la lista
for i, nombre_archivo in enumerate(archivos):
    # Construir el nuevo nombre del archivo (aquí puedes aplicar cualquier lógica de renombrado)
    nuevo_nombre = f"vga_female ({i + 1}).jpg"

    # Construir la ruta completa del archivo antiguo y el nuevo nombre
    ruta_antigua = os.path.join(carpeta, nombre_archivo)
    ruta_nueva = os.path.join(carpeta, nuevo_nombre)
    try:
        # Renombrar el archivo
        os.rename(ruta_antigua, ruta_nueva)
    except FileExistsError:
        pass
