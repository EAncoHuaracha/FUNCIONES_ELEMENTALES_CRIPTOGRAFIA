def preprocess_utf8(texto):
    texto_utf8 = ""

    for caracter in texto:
        if caracter == '\n':
            texto_utf8 += '\n'
        else:
            valor_unicode = ord(caracter)

            if valor_unicode < 128:
                texto_utf8 += f"\\u{valor_unicode:02x}"
            elif valor_unicode < 2048:
                byte1 = 0xc0 | (valor_unicode >> 6)
                byte2 = 0x80 | (valor_unicode & 0x3f)
                texto_utf8 += f"\\u{byte1:02x}\\u{byte2:02x}"
            else:
                byte1 = 0xe0 | (valor_unicode >> 12)
                byte2 = 0x80 | ((valor_unicode >> 6) & 0x3f)
                byte3 = 0x80 | (valor_unicode & 0x3f)
                texto_utf8 += f"\\u{byte1:02x}\\u{byte2:02x}\\u{byte3:02x}"

    return texto_utf8

archivo_entrada = 'texto.txt'
    
try:
    with open(archivo_entrada, 'r', encoding='utf-8') as file:
        contenido = file.read()

    contenido_procesado = preprocess_utf8(contenido)

    archivo_salida = 'texto_utf8.txt'
    with open(archivo_salida, 'w', encoding='utf-8') as file:
        file.write(contenido_procesado)

    print(f"Se ha preprocesado el archivo y guardado como '{archivo_salida}' con caracteres en formato UTF-8, conservando los saltos de línea.")

except FileNotFoundError:
    print(f"Error: No se pudo encontrar el archivo '{archivo_entrada}'")

except Exception as e:
    print(f"Ocurrió un error durante el proceso de preprocesamiento: {str(e)}")
