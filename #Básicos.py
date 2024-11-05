import os

#1. Ler um Arquivo de Texto
# Programa para ler e exibir o conteúdo de "mensagem.txt"

with open("mensagem.txt", "r") as arquivo:
    conteudo = arquivo.read()

print(conteudo)

#2. Escrever em um Arquivo de Texto

frase = input("Digite uma frase: ")
with open("frase_usuario.txt", "w") as arquivo:
    arquivo.write(frase)
print("Frase salva em 'frase_usuario.txt'.")

#3. Contar Linhas e Palavras

with open("texto.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    num_linhas = len(linhas)
    num_palavras = sum(len(linha.split()) for linha in linhas)
print(f"Linhas: {num_linhas}, Palavras: {num_palavras}")


#4. Copiar Conteúdo de um Arquivo

with open("origem.txt", "r") as origem, open("copia.txt", "w") as copia:
    copia.write(origem.read())
print("Conteúdo copiado para 'copia.txt'.")

#5. Adicionar Conteúdo a um Arquivo

frase = input("Digite uma frase: ")
with open("anotacoes.txt", "a") as arquivo:
    arquivo.write(frase + "\n")
print("Frase adicionada a 'anotacoes.txt'.")


#6. Substituir Palavras em um Arquivo

with open("texto.txt", "r") as arquivo:
    conteudo = arquivo.read()
conteudo_modificado = conteudo.replace("Python", "programação")
with open("texto_modificado.txt", "w") as novo_arquivo:
    novo_arquivo.write(conteudo_modificado)
print("Palavras substituídas e salvas em 'texto_modificado.txt'.")

#7. Listar Arquivos em um Diretório

diretorio = input("Informe o caminho do diretório: ")
arquivos = os.listdir(diretorio)
for arquivo in arquivos:
    print(arquivo)

#8. Combinar Vários Arquivos

with open("texto_completo.txt", "w") as completo:
    for nome_arquivo in ["parte1.txt", "parte2.txt", "parte3.txt"]:
        with open(nome_arquivo, "r") as parte:
            completo.write(parte.read())
print("Conteúdo combinado em 'texto_completo.txt'.")

#9. Extrair Informações Específicas

with open("pessoas.txt", "r") as arquivo:
    for linha in arquivo:
        nome = linha.split(",")[0].split(":")[1].strip()
        print(f"Nome: {nome}")

#10. Dividir Arquivo Grande em Partes Menores

with open("grande.txt", "r") as arquivo:
    for i, chunk in enumerate(iter(lambda: list(arquivo.readline() for _ in range(100)), [])):
        with open(f"parte{i+1}.txt", "w") as parte:
            parte.writelines(chunk)
print("Arquivo grande dividido em partes menores.")

#11. Ordenar Linhas de um Arquivo

with open("nomes.txt", "r") as arquivo:
    nomes = sorted(arquivo.readlines())
with open("nomes_ordenados.txt", "w") as arquivo_ordenado:
    arquivo_ordenado.writelines(nomes)
print("Nomes ordenados em 'nomes_ordenados.txt'.")

#12. Contar Ocorrências de Palavras

from collections import Counter

with open("texto.txt", "r") as arquivo:
    conteudo = arquivo.read()
contador = Counter(conteudo.split())
for palavra, frequencia in contador.items():
    print(f"{palavra}: {frequencia}")

#13. Arquivo de Log

from datetime import datetime

with open("dados.txt", "r") as dados, open("backup.txt", "a") as backup:
    backup.write(dados.read())
    backup.write(f"\nBackup realizado em {datetime.now()}\n")
print("Backup realizado com sucesso em 'backup.txt'.")

#14. Remover Linhas Vazias

with open("com_vazios.txt", "r") as arquivo:
    linhas = [linha for linha in arquivo if linha.strip()]
with open("sem_vazios.txt", "w") as arquivo_sem_vazios:
    arquivo_sem_vazios.writelines(linhas)
print("Linhas vazias removidas e salvas em 'sem_vazios.txt'.")

#15. Criação de um Registro de Usuário

nome = input("Nome: ")
idade = input("Idade: ")
email = input("Email: ")
with open("usuarios.txt", "a") as arquivo:
    arquivo.write(f"{nome}, {idade}, {email}\n")
print("Informações salvas em 'usuarios.txt'.")

#16. Criptografar e Descriptografar um Arquivo
# Criptografar
with open("secreto.txt", "r") as arquivo:
    conteudo = arquivo.read()
conteudo_criptografado = ''.join(chr(ord(char) + 1) for char in conteudo)
with open("criptografado.txt", "w") as criptografado:
    criptografado.write(conteudo_criptografado)
print("Arquivo criptografado salvo em 'criptografado.txt'.")

# Descriptografar
with open("criptografado.txt", "r") as arquivo:
    conteudo_criptografado = arquivo.read()
conteudo_descriptografado = ''.join(chr(ord(char) - 1) for char in conteudo_criptografado)
print("Conteúdo descriptografado:", conteudo_descriptografado)

#17. Manipular Arquivo Binário

with open("imagem.jpg", "rb") as imagem, open("imagem_copia.jpg", "wb") as copia:
    copia.write(imagem.read())
print("Imagem copiada para 'imagem_copia.jpg'.")

#18. Validação de Dados em um Arquivo

with open("dados.csv", "r") as dados, open("erros.csv", "w") as erros:
    for linha in dados:
        nome, idade, email = linha.strip().split(", ")
        if not idade.isdigit() or int(idade) <= 0 or "@" not in email:
            erros.write(linha)
print("Linhas inválidas salvas em 'erros.csv'.")