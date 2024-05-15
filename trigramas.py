def obtenerTrigramasDistancias(texto):
    trigramas = {}
    distancias = []

    def es_letra(caracter):
        return ('a' <= caracter <= 'z') or ('A' <= caracter <= 'Z')

    i = 0
    while i <= len(texto) - 3:
        trigrama = texto[i:i+3]

        if len(trigrama) == 3 and es_letra(trigrama[0]) and es_letra(trigrama[1]) and es_letra(trigrama[2]):
            if trigrama in trigramas:
                trigramas[trigrama].append(i)
            else:
                trigramas[trigrama] = [i]
            i += 3
        else:
            i += 1

    for trigrama, posiciones in trigramas.items():
        if len(posiciones) > 1:
            posiciones.sort() 
            for j in range(len(posiciones) - 1):
                distancia = posiciones[j+1] - posiciones[j]
                distancias.append((trigrama, distancia))

    distancias.sort(key=lambda x: x[1])

    primeros_caracteres = texto[:3]

    return trigramas, distancias, primeros_caracteres

archivo_entrada = 'PRACTICA_PRE.txt'

try:
    with open(archivo_entrada, 'r', encoding='utf-8') as file:
        contenido = file.read()

    trigramas_encontrados, distancias_trigramas, tres_primeros_caracteres = obtenerTrigramasDistancias(contenido)

    print("Trigramas encontrados:")
    for trigrama, posiciones in trigramas_encontrados.items():
        print(f"{trigrama}: {posiciones}")

    print("\nDistancias entre trigramas idénticos:")
    for trigrama, distancia in distancias_trigramas:
        print(f"{trigrama}: {distancia}")

except FileNotFoundError:
    print(f"Error: No se pudo encontrar el archivo '{archivo_entrada}'")

except Exception as e:
    print(f"Ocurrió un error durante el proceso: {str(e)}")
