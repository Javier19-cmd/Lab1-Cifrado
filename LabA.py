import unicodedata

def limpiar_texto(texto):
    texto = texto.lower()
    # Eliminar tildes
    texto = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode("utf-8")
    texto_limpio = ''.join(e for e in texto if e.isalpha() or e.isspace())
    return texto_limpio

def distribucion_caracteres(texto_cifrado):
    # Inicializando un diccionario para almacenar las frecuencias de los caracteres
    frecuencias = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}
    
    # Calculando las frecuencias de los caracteres en el texto cifrado
    for char in texto_cifrado:
        if char.isalpha():
            frecuencias[char] += 1
    
    # Calculando el total de caracteres
    total_caracteres = sum(frecuencias.values())
    
    # Calculando las probabilidades
    probabilidades = {char: freq / total_caracteres for char, freq in frecuencias.items()}
    
    return probabilidades


# ejemplo = "Hola, ¿cómo estás?"

# print(limpiar_texto(ejemplo))

#####################################
#               Cifrado             #
#                César              #
#####################################

# Cifrado César.
def cifrado_caesar(texto, desplazamiento):
    texto = limpiar_texto(texto)
    resultado = ""
    for i in range(len(texto)):
        char = texto[i]
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            resultado += chr((ord(char) - ascii_offset + desplazamiento) % 27 + ascii_offset)
        else:
            resultado += char
    return resultado

def descifrado_caesar(texto, desplazamiento):
    return cifrado_caesar(texto, -desplazamiento)


print("#####################################")
print("#               Cifrado             #")
print("#                César              #")
print("#####################################")

ejemplo = "Hola, ¿cómo estás?"
desplazamiento = 3

limpio = limpiar_texto(ejemplo)
cifrado = cifrado_caesar(limpio, desplazamiento)

print("Cifrado César: ")
print(cifrado)

descifrado = descifrado_caesar(cifrado, desplazamiento)
print("Descifrado César: ")
print(descifrado)

probabilidades = distribucion_caracteres(descifrado)

# Imprimiendo las probabilidades
print("Probabilidades en César: ")
for char, prob in probabilidades.items():
    print(f"{char}: {prob}")

#####################################
#               Cifrado             #
#                Afín               #
#####################################
def cifrado_afin(texto, a, b):
    texto = limpiar_texto(texto)
    resultado = ""
    for char in texto:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            resultado += chr((a * (ord(char) - ascii_offset) + b) % 27 + ascii_offset)
        else:
            resultado += char
    return resultado

def descifrado_afin(texto, a, b):
    a_inv = pow(a, -1, 27)
    return cifrado_afin(texto, a_inv, -a_inv * b)

print("#####################################")
print("#               Cifrado             #")
print("#                Afín               #")
print("#####################################")

texto = "Hola, ¿cómo estás?"
a = 5
b = 8

texto_cifrado = cifrado_afin(texto, a, b)
print(texto_cifrado)

texto_descifrado = descifrado_afin(texto_cifrado, a, b)
print(texto_descifrado)

probabilidades = distribucion_caracteres(descifrado)

# Imprimiendo las probabilidades
print("Probabilidades en Afín: ")
for char, prob in probabilidades.items():
    print(f"{char}: {prob}")

#####################################
#               Cifrado             #
#              Vigenère             #
#####################################


def cifrado_vigenere(texto, clave):
    texto = limpiar_texto(texto)
    resultado = ""
    index_clave = 0
    for char in texto:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            desplazamiento = ord(clave[index_clave % len(clave)]) - ascii_offset
            resultado += chr((ord(char) - ascii_offset + desplazamiento) % 27 + ascii_offset)
            index_clave += 1
        else:
            resultado += char
    return resultado

def descifrado_vigenere(texto, clave):
    clave = clave.lower()
    clave = ''.join(chr((27 - (ord(c) - ord('a'))) % 27 + ord('a')) for c in clave)
    return cifrado_vigenere(texto, clave)

print("#####################################")
print("#               Cifrado             #")
print("#               Vigenère            #")
print("#####################################")

texto = "Hola, ¿cómo estás?"
clave = "clave"

texto_cifrado = cifrado_vigenere(texto, clave)
print("Texto cifrado: ")
print(texto_cifrado)

texto_descifrado = descifrado_vigenere(texto_cifrado, clave)
print("Texto descifrado: ")
print(texto_descifrado)

probabilidades = distribucion_caracteres(descifrado)

# Imprimiendo las probabilidades
print("Probabilidades en Vigenère: ")
for char, prob in probabilidades.items():
    print(f"{char}: {prob}")

#2. Análisis de frecuencias sobre un texto.
#3. Comparar con el análisis de frecuencias de un texto en español.


# menu = True

# while menu:
#     print("Bienvenid@ al cifrador")
#     print("1. Cifrado César")
#     print("2. Cifrado Afín")
#     print("3. Cifrado Vigenère")
#     print("4. Salir")
    
#     opcion = int(input("Ingrese una opción: "))
    
#     if opcion == 1:
#         texto = input("Ingrese el texto a cifrar: ")
#         desplazamiento = int(input("Ingrese el desplazamiento: "))
#         print("Texto cifrado: ")
#         print(cifrado_caesar(texto, desplazamiento))
#         print("Texto descifrado: ")
#         print(descifrado_caesar(texto, desplazamiento))
        
#     elif opcion == 2:
#         texto = input("Ingrese el texto a cifrar: ")
#         a = int(input("Ingrese el valor de a: "))
#         b = int(input("Ingrese el valor de b: "))
#         print("Texto cifrado: ")
#         print(cifrado_afin(texto, a, b))
#         print("Texto descifrado: ")
#         print(descifrado_afin(texto, a, b))
    
#     elif opcion == 3:
#         texto = input("Ingrese el texto a cifrar: ")
#         clave = input("Ingrese la clave: ")
#         print("Texto cifrado: ")
#         print(cifrado_vigenere(texto, clave))
#         print("Texto descifrado: ")
#         print(descifrado_vigenere(texto, clave))
    
#     elif opcion == 4:
#         menu = False
#         print("Gracias por usar el cifrador")