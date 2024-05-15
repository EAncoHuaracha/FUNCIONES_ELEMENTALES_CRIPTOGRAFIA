alfabeto_permitido = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def frecuencias(archivo):
    tabla_frecuencias = {letra: 0 for letra in alfabeto_permitido}
    
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            contenido = file.read()
        
        for caracter in contenido:
            if caracter in tabla_frecuencias:
                tabla_frecuencias[caracter] += 1
        
        frecuencias_ordenadas = sorted(tabla_frecuencias.items(), key=lambda x: x[1], reverse=True)
        
        print("Caracteres de mayor frecuencia:")
        for i in range(5):
            letra, frecuencia = frecuencias_ordenadas[i]
            print(f"{letra}: {frecuencia}")
        
        return tabla_frecuencias
    
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{archivo}'")
        return None
    except Exception as e:
        print(f"Ocurrió un error durante el cálculo de frecuencias: {str(e)}")
        return None

archivo_generado = 'PRACTICA_PRE.txt'
resultados_frecuencias = frecuencias(archivo_generado)

if resultados_frecuencias:
    print("\nTabla de frecuencias:")
    for letra in alfabeto_permitido:
        print(f"{letra}: {resultados_frecuencias[letra]}")
