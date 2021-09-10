
frase=input("Ingrese palabra a determinar si es palindromo:\n") # rotor rotor

def palindromo_secuencias(secuencia): 
    secuencia = secuencia.lower() 
    secuencia = secuencia.replace(' ', '')
    longitud = len(secuencia)
    if longitud % 2 == 0:
        izquierda = secuencia[:longitud // 2]
        derecha = secuencia[longitud // 2:]
    else:
        izquierda = secuencia[:longitud // 2]
        derecha = secuencia[longitud // 2 + 1:]
    if izquierda == derecha[::-1]:
        print("Es Palíndromo")
    else: print("No es Palíndromo")

palindromo_secuencias(frase)
