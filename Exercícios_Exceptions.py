#1
def divisao():
    numero_1 = int(input("insira um numero"))
    numero_2 = int(input("insira um numero"))
    divisao = numero_1 / numero_2
    print (divisao)

try:
    divisao()

except ZeroDivisionError:
    print("Erro: Divisão por zero. Não é possível calcular .")

except ValueError:
    print("Erro: Valor inválido. Certifique-se de digitar um número válido.")


#2
cores = {
    'vermelho': (255, 0, 0),
    'verde': (0, 255, 0),
    'azul': (0, 0, 255)
}

try:
    
    nome_cor = input("Digite o nome de uma cor (vermelho, verde, azul): ").lower()
    
    valor_rgb = cores[nome_cor]
    
   
    print(f"O valor RGB de '{nome_cor}' é: {valor_rgb}")

except KeyError:
    print("Erro: Cor não encontrada no dicionário.")

    #3
numero = int(input('insira um numero'))


try:
   
    if numero > 10:
        print ('número é válido')

except ValueError:
   print('Erro: digitar um número válido.')

else:
   print('o programa foi executado com sucesso')

finally:
   print('Programa encerrado')



#4
def verificar_senha(senha):
    
    if len(senha) < 8:
        return False
    
    
    tem_numero = False
    for caractere in senha:
        if caractere.isdigit():  
            tem_numero = True
            break
    
    return tem_numero


senha = "Senu"
try:
    if verificar_senha(senha):
        print("Senha válida")


except ValueError:
    print("Erro:")


#5
def realizar_transferencia(saldo, valor_transferencia):
    if valor_transferencia > saldo:
        raise ValueError("Saldo insuficiente para realizar a transferência.")
    
   
    saldo -= valor_transferencia
    return saldo


try:
    saldo = float(input("Digite o saldo da sua conta: R$ "))
    valor_transferencia = float(input("Digite o valor da transferência: R$ "))
    
   
    novo_saldo = realizar_transferencia(saldo, valor_transferencia)
    
    print(f"Transferência realizada com sucesso! Seu novo saldo é: R$ {novo_saldo:.2f}")
    
except ValueError as e:
    print(f"Erro: {e}")

