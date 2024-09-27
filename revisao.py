# 1. Criação e Manipulação de Listas
lista_numeros = [random.randint(1, 100) for _ in range(10)]
print("Lista de Números:", lista_numeros)
print("Maior Número:", max(lista_numeros))
print("Menor Número:", min(lista_numeros))

# 2. Operações com Listas
frutas = []
for _ in range(5):
    fruta = input("Digite o nome de uma fruta: ")
    frutas.append(fruta)

fruta_busca = input("Informe uma fruta para verificar se está na lista: ")
if fruta_busca in frutas:
    print(f"{fruta_busca} está na lista.")
else:
    print(f"{fruta_busca} não está na lista.")

# 3. Manipulação de Listas com Laços
def calcular_media(numeros):
    return sum(numeros) / len(numeros)

lista_numeros = [random.randint(1, 100) for _ in range(10)]
print("Média dos números:", calcular_media(lista_numeros))

# 4. Listas Aninhadas
pessoas = [
    ["Alice", 30, "São Paulo"],
    ["Bob", 25, "Rio de Janeiro"],
    ["Carlos", 22, "Belo Horizonte"]
]

for pessoa in pessoas:
    print(f"Nome: {pessoa[0]}, Idade: {pessoa[1]}, Cidade: {pessoa[2]}")

# 5. Remoção de Duplicatas
numeros = input("Digite uma lista de números separados por vírgula: ")
lista_numeros = list(map(int, numeros.split(',')))
lista_sem_duplicatas = list(set(lista_numeros))
print("Lista sem duplicatas:", lista_sem_duplicatas)

#Exercícios de Dicionários python

# 6. Criação e Acesso a Dicionários
dias_da_semana = {}
for dia in ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]:
    horas = int(input(f"Digite as horas trabalhadas na {dia}: "))
    dias_da_semana[dia] = horas

total_horas = sum(dias_da_semana.values())
print("Total de horas trabalhadas na semana:", total_horas)

# 7. Atualização de Dicionários
notas_alunos = {}
for _ in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    notas_alunos[nome] = nota

aluno_consulta = input("Digite o nome do aluno para consultar a nota: ")
if aluno_consulta in notas_alunos:
    print(f"A nota de {aluno_consulta} é {notas_alunos[aluno_consulta]}.")
    atualizar = input("Deseja atualizar a nota? (s/n): ")
    if atualizar.lower() == 's':
        nova_nota = float(input("Digite a nova nota: "))
        notas_alunos[aluno_consulta] = nova_nota
        print(f"Nota atualizada para {aluno_consulta}: {nova_nota}.")
else:
    print("Aluno não encontrado.")

# 8. Iteração sobre Dicionários
estoque = {"Produto A": 10, "Produto B": 0, "Produto C": 5}

def verificar_estoque(produto):
    if produto in estoque:
        return estoque[produto]
    else:
        return None

produto_busca = input("Digite o nome do produto a verificar: ")
quantidade = verificar_estoque(produto_busca)
if quantidade is not None:
    print(f"{quantidade} unidades de {produto_busca} estão disponíveis.")
else:
    print("Produto não encontrado.")

# 9. Conversão entre Listas e Dicionários
paises = ["Brasil", "Argentina", "Chile"]
capitais = ["Brasília", "Buenos Aires", "Santiago"]
dicionario_paises = dict(zip(paises, capitais))
print("Dicionário de Países e Capitais:", dicionario_paises)

# 10. Dicionário Aninhado
estudantes = {
    "Alice": {"Matemática": 8.5, "Português": 7.0, "Ciências": 9.0},
    "Bob": {"Matemática": 5.5, "Português": 6.0, "Ciências": 7.5}
}

aluno = input("Digite o nome do estudante para alterar a nota: ")
disciplina = input("Digite a disciplina: ")
nova_nota = float(input("Digite a nova nota: "))
if aluno in estudantes and disciplina in estudantes[aluno]:
    estudantes[aluno][disciplina] = nova_nota
    print(f"Nota de {aluno} em {disciplina} atualizada para {nova_nota}.")
else:
    print("Estudante ou disciplina não encontrados.")

#Exercícios de Funções

# 11. Função com Listas
def soma_pares(lista):
    return sum(num for num in lista if num % 2 == 0)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Soma dos números pares:", soma_pares(numeros))

# 12. Função que Trabalha com Dicionários
def produto_mais_caro(dicionario):
    return max(dicionario, key=dicionario.get)

produtos = {"Produto A": 10.50, "Produto B": 20.00, "Produto C": 15.75}
print("Produto mais caro:", produto_mais_caro(produtos))

# 13. Função com Parâmetros Opcionais
def multiplicar_lista(lista, numero=1):
    return [x * numero for x in lista]

print(multiplicar_lista([1, 2, 3, 4]))
print(multiplicar_lista([1, 2, 3, 4], 3))

# 14. Função que Modifica Dicionários
def atualizar_estoque(estoque, produto_vendido, quantidade_vendida):
    if produto_vendido in estoque:
        if estoque[produto_vendido] >= quantidade_vendida:
            estoque[produto_vendido] -= quantidade_vendida
            return f"Estoque atualizado: {estoque[produto_vendido]} unidades restantes."
        else:
            return "Quantidade vendida excede o estoque disponível."
    else:
        return "Produto não encontrado."

estoque_produtos = {"Produto A": 10, "Produto B": 5}
print(atualizar_estoque(estoque_produtos, "Produto A", 3))

# 15. Combinação de Listas, Dicionários e Funções
def media_estudantes(lista_estudantes):
    medias = {}
    for estudante in lista_estudantes:
        medias[estudante['nome']] = sum(estudante['notas']) / len(estudante['notas'])
    return medias

lista_estudantes = [
    {"nome": "Alice", "notas": [8, 7, 9]},
    {"nome": "Bob", "notas": [6, 5, 7]}
]
print("Médias dos estudantes:", media_estudantes(lista_estudantes))

# 16. Funções Recursivas
def busca_binaria(lista, elemento):
    if len(lista) == 0:
        return False
    meio = len(lista) // 2
    if lista[meio] == elemento:
        return True
    elif lista[meio] < elemento:
        return busca_binaria(lista[meio+1:], elemento)
    else:
        return busca_binaria(lista[:meio], elemento)

numeros_ordenados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Número 5 encontrado?", busca_binaria(numeros_ordenados, 5))


# Sistema de Gerenciamento de Estoque de Livros

biblioteca = {}

def cadastrar_livro(titulo, autor, genero, quantidade, codigo):
    biblioteca[codigo] = {'titulo': titulo, 'autor': autor, 'genero': genero, 'quantidade': quantidade}

def buscar_livro(codigo):
    return biblioteca.get(codigo, None)

def atualizar_estoque(codigo, quantidade):
    if codigo in biblioteca:
        biblioteca[codigo]['quantidade'] = quantidade
        return True
    return False

def remover_livro(codigo):
    return biblioteca.pop(codigo, None)

def listar_livros():
    return list(biblioteca.values())


cadastrar_livro("1984", "George Orwell", "Ficção", 10, "001")


livro_encontrado = buscar_livro("001")
if livro_encontrado:
    print(f"Livro encontrado: {livro_encontrado['titulo']}")

for livro in listar_livros():
    print(f"{livro['titulo']} - {livro['autor']}")
