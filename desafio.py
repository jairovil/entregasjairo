import random  
import string  

def gerar_caractere():
    caracteres = string.ascii_letters + string.digits + string.punctuation  
    return random.choice(caracteres)

def gerar_senha_recursiva(tamanho):
    if tamanho <= 0:
        return ""
    else:
        return gerar_caractere() + gerar_senha_recursiva(tamanho - 1)

def cifra_de_cesar(caractere, deslocamento):
 
    if caractere.isalpha():
        base = ord('a') if caractere.islower() else ord('A')
        return chr((ord(caractere) - base + deslocamento) % 26 + base)
    elif caractere.isdigit():
        return chr((ord(caractere) - ord('0') + deslocamento) % 10 + ord('0'))
    else:
        return chr(ord(caractere) + deslocamento)

def criptografar_senha(senha):
    return ''.join(cifra_de_cesar(c, 3) for c in senha)

def aleatoria():
    tamanho = 8
    senha = gerar_senha_recursiva(tamanho)
    senha_criptografada = criptografar_senha(senha)

    print(f"Senha original: {senha}")
    print(f"Senha criptografada: {senha_criptografada}")

aleatoria()
