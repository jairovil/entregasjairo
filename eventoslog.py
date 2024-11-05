#Exercício: Registro de Log de Eventos
from datetime import datetime

def registrar_evento():
    descricao = input("Digite a descrição do evento: ")
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    registro = f"{data_hora} - Evento: {descricao}\n"
    try:
        with open("sistema_log.txt", "a") as arquivo:
            arquivo.write(registro)
        print("Evento registrado com sucesso!")
    except Exception as e:
        print(f"Erro ao registrar o evento: {e}")

def visualizar_log():
    try:
        with open("sistema_log.txt", "r") as arquivo:
            conteudo = arquivo.read()
            if conteudo:
                print("Log de eventos:")
                print(conteudo)
            else:
                print("O log está vazio.")
    except FileNotFoundError:
        print("Arquivo de log não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o log: {e}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Registrar novo evento")
        print("2. Visualizar log de eventos")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            registrar_evento()
        elif opcao == "2":
            visualizar_log()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
