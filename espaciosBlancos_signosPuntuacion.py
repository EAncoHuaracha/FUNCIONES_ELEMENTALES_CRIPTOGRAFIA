alfabeto_permitido = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

mapeo_minusculas = {
    'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g',
    'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n',
    'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u',
    'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'
}

def conv_minusculas(texto):
    texto_minusculas = []
    for caracter in texto:
        if caracter in mapeo_minusculas:
            texto_minusculas.append(mapeo_minusculas[caracter])
        else:
            texto_minusculas.append(caracter)
    return ''.join(texto_minusculas)

def contar_longitud_alfabeto(texto):

    for caracter in texto:
        if caracter in alfabeto_permitido:
            alfabeto_resultante.add(caracter)
    
    longitud_alfabeto = len(alfabeto_resultante)
    
    return longitud_alfabeto

def contar_elementos(texto):
    contador = 0
    for _ in texto:
        contador += 1
    return contador

def eliminar_espacios_y_puntuacion(texto):
    
    texto_filtrado = []
    alfabeto_resultante = set()
    
    # Recorrer cada caracter del texto
    for caracter in texto:
        if caracter in alfabeto_permitido:
            texto_filtrado.append(caracter)
            alfabeto_resultante.add(conv_minusculas(caracter))
    
    texto_filtrado = ''.join(texto_filtrado)
    longitud_alfabeto = contar_elementos(alfabeto_resultante)
    
    return texto_filtrado, alfabeto_resultante, longitud_alfabeto

archivo_entrada = 'PRACTICA_PRE.txt'
archivo_salida = 'PRACTICA_PRE.txt'

try:
    with open(archivo_entrada, 'r', encoding='utf-8') as file:
        contenido = file.read()

    contenido, alfabeto_resultante, longitud_alfabeto = eliminar_espacios_y_puntuacion(contenido)

    with open(archivo_salida, 'w', encoding='utf-8') as file:
        file.write(contenido)

    print("Se realizó correctamente el proceso de sustitución.")
    
    print("\nAlfabeto resultante:")
    print(alfabeto_resultante)

    print("\nLongitud del alfabeto resultante:")
    print(longitud_alfabeto)
    
except FileNotFoundError:
    print(f"Error: No se pudo encontrar el archivo '{archivo_entrada}'")
    
except Exception as e:
    print(f"Ocurrió un error durante el proceso de sustitución: {str(e)}")