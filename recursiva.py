def potencia(base, expoente):
    if expoente == 0:
        return 1
    return base * potencia(base, expoente - 1)
potencia(5, 2)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def conta_digitos(numero):
    if abs(numero) < 10:  
        return 1
    return 1 + conta_digitos(numero // 10)

def e_palindromo(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return e_palindromo(string[1:-1])

