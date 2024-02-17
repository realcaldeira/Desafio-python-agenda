
def adicionar_contato(nome, telefone, email):
  data.append({"nome": nome, "telefone": telefone, "email": email, "favorito": False})
  print("Contato adicionado com sucesso!")
  return

def visualizar_contatos(contato):
  for indice,contato in enumerate(data, start=1):
    print(f"{indice}. {contato['favorito']} - {contato['nome']} - {contato['telefone']} - {contato['email']}")
  return

def atualizar_contato(data, numero, nome, telefone, email):
    if int(numero) <= len(data):
        data[int(numero)-1] = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
        print("Contato atualizado com sucesso!")
    return

def marcar_contato(data, numero):
    if int(numero) <= len(data):
        data[int(numero)-1]["favorito"] = True
        print("Contato marcado com sucesso!")
    return

data = []

while True:
  print("1. Adicione um contato novo")
  print("2. Mostre todos os contatos")
  print("3. Atualize um contato")
  print("4. Marque um contato")
  print("5. Selecione um contato")
  print("6. Visualize os contatos marcados")
  print("7. Delete um contato")

  opcao = input("Digite a opção desejada: ")

  if opcao == "1":
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    adicionar_contato(nome, telefone, email)
  elif opcao == "2":
    visualizar_contatos(data)
  elif opcao == "3":
    numero = input("Digite o id do contato: ")
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    atualizar_contato(data, numero, nome, telefone, email)
  elif opcao == "4":
    numero = input("Digite o id do contato: ")
    marcar_contato(data, numero)
  elif opcao == "5":
    numero = input("Digite o id do contato: ")
    print(data[int(numero)-1])
  elif opcao == "6":
    for contato in data:
        if contato["favorito"]:
            print(contato)
  elif opcao == "7":
    numero = input("Digite o id do contato: ")
    if int(numero) <= len(data):
        data.pop(int(numero)-1)
        print("Contato deletado com sucesso!")
    else:
        print("Contato não encontrado!")
  else:
    print("Opção inválida")