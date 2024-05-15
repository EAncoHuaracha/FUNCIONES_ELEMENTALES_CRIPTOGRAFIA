mapeo_mayusculas = {
    'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G',
    'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N',
    'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U',
    'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'
}

def mayusculas(texto):
    texto_mayusculas = []
    for caracter in texto:
        if caracter in mapeo_mayusculas:
            texto_mayusculas.append(mapeo_mayusculas[caracter])
        else:
            texto_mayusculas.append(caracter)
    return ''.join(texto_mayusculas)

archivo_entrada = 'PRACTICA_PRE.txt'
archivo_salida = 'PRACTICA_PRE.txt'

try:
    with open(archivo_entrada, 'r', encoding='utf-8') as file:
        contenido = file.read()

    contenido = mayusculas(contenido)

    with open(archivo_salida, 'w', encoding='utf-8') as file:
        file.write(contenido)

    print("Se realizó correctamente el proceso de sustitución.")
    
except FileNotFoundError:
    print(f"Error: No se pudo encontrar el archivo '{archivo_entrada}'")
    
except Exception as e:
    print(f"Ocurrió un error durante el proceso de sustitución: {str(e)}")