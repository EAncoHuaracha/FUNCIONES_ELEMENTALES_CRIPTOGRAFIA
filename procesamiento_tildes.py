mapeo_tildes = {
    'á': 'a',
    'é': 'e',
    'í': 'i',
    'ó': 'o',
    'ú': 'u',
    'Á': 'A',
    'É': 'E',
    'Í': 'I',
    'Ó': 'O',
    'Ú': 'U',
}

def eliminar_tildes(texto, mapeo_tildes):
    texto_sin_tildes = []
    for caracter in texto:
        if caracter in mapeo_tildes:
            texto_sin_tildes.append(mapeo_tildes[caracter])
        else:
            texto_sin_tildes.append(caracter)
    
    texto_sin_tildes = ''.join(texto_sin_tildes)
    return texto_sin_tildes


archivo_entrada = 'PRACTICA_PRE.txt'
archivo_salida = 'PRACTICA_PRE.txt'

try:
    with open(archivo_entrada, 'r', encoding='utf-8') as file:
        contenido = file.read()

    contenido = eliminar_tildes(contenido, mapeo_tildes)

    with open(archivo_salida, 'w', encoding='utf-8') as file:
        file.write(contenido)

    print("Se realizó correctamente el proceso de sustitución.")
    
except FileNotFoundError:
    print(f"Error: No se pudo encontrar el archivo '{archivo_entrada}'")
    
except Exception as e:
    print(f"Ocurrió un error durante el proceso de sustitución: {str(e)}")