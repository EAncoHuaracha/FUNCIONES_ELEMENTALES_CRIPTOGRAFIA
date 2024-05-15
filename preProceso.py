def my_lower(c):
    if 'A' <= c <= 'Z':
        return chr(ord(c) + (ord('a') - ord('A')))
    else:
        return c

def my_len(s):
    length = 0
    for char in s:
        if char != ' ':
            length += 1
    return length

def preprocess_text(texto):
    alfabeto_personalizado = {
        'a': 'X', 'b': 'Y', 'c': 'Z', 'd': 'A', 'e': 'B',
        'f': 'C', 'g': 'D', 'h': 'E', 'i': 'F', 'j': 'G',
        'k': 'H', 'l': 'I', 'm': 'J', 'n': 'K', 'o': 'L',
        'p': 'M', 'q': 'N', 'r': 'O', 's': 'P', 't': 'Q',
        'u': 'R', 'v': 'S', 'w': 'T', 'x': 'U', 'y': 'V',
        'z': 'W', ' ': ''
    }

    texto_procesado = []
    counter = 0
    for caracter in texto:
        caracter_minuscula = my_lower(caracter)
        nuevo_caracter = alfabeto_personalizado.get(caracter_minuscula, caracter)
        if nuevo_caracter != '':
            texto_procesado.append(nuevo_caracter)

            counter += 1
            if counter == 13:
                texto_procesado.append('EPIS')
                counter = 0

    texto_resultante = ''.join(texto_procesado)

    longitud_actual = my_len(texto_resultante)

    padding_needed = 5 - (longitud_actual % 5)
    if padding_needed != 5:
        texto_resultante += 'Z' * padding_needed

    longitud_actual = my_len(texto_resultante)
    print (f"Total de caracteres del texto procesado: {longitud_actual}")

    return texto_resultante

archivo_entrada = 'texto.txt'
archivo_salida = 'texto_procesado.txt'

try:
    with open(archivo_entrada, 'r', encoding='utf-8') as file:
        contenido = file.read()

    texto_procesado = preprocess_text(contenido)

    with open(archivo_salida, 'w', encoding='utf-8') as file:
        file.write(texto_procesado)

    print(f"Se ha preprocesado el archivo '{archivo_entrada}' y guardado como '{archivo_salida}' conforme a las especificaciones.")

except FileNotFoundError:
    print(f"Error: No se pudo encontrar el archivo '{archivo_entrada}'.")

except Exception as e:
    print(f"Ocurrió un error durante el procesamiento: {str(e)}")
