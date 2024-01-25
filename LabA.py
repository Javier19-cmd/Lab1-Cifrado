import unicodedata

def limpiar_texto(texto):
    texto = texto.lower()
    # Eliminar tildes
    texto = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode("utf-8")
    texto_limpio = ''.join(e for e in texto if e.isalpha() or e.isspace())
    return texto_limpio



# ejemplo = "Hola, ¿cómo estás?"

# print(limpiar_texto(ejemplo))

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

ejemplo = "Hola, ¿cómo estás?"
desplazamiento = 3

limpio = limpiar_texto(ejemplo)
cifrado = cifrado_caesar(limpio, desplazamiento)

print("Cifrado César: ", cifrado)

descifrado = descifrado_caesar(cifrado, desplazamiento)
print("Descifrado César: ", descifrado)