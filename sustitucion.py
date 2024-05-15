mapeo_sustitucion = {
    'a': 'u', 
    'A': 'u',
    'h': 't', 
    'H': 't',
    'ñ': 'e', 
    'Ñ': 'e',
    'k': 'l', 
    'K': 'l',
    'v': 'f', 
    'V': 'f',
    'w': 'b', 
    'W': 'b',
    'z': 'y', 
    'Z': 'y',
    'r': 'p', 
    'R': 'p'
}

def sustituir(texto, alfabeto):
    resultado = []
    for caracter in texto:
        if caracter in alfabeto:
            resultado.append(alfabeto[caracter])
        else:
            resultado.append(caracter)
    return ''.join(resultado)

archivo_entrada = 'texto.txt'
archivo_salida = 'PRACTICA_PRE.txt'


try:
    with open(archivo_entrada, 'r', encoding='utf-8') as file:
        contenido = file.read()

    contenido = sustituir(contenido, mapeo_sustitucion)

    with open(archivo_salida, 'w', encoding='utf-8') as file:
        file.write(contenido)

    print("Se realizó correctamente el proceso de sustitución.")
    
except FileNotFoundError:
    print(f"Error: No se pudo encontrar el archivo '{archivo_entrada}'")
    
except Exception as e:
    print(f"Ocurrió un error durante el proceso de sustitución: {str(e)}")