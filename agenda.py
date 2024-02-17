
def adicionar_contato(nome, telefone, email):
  data.append({"nome": nome, "telefone": telefone, "email": email,"favorito": False})
  print("Contato adicionado com sucesso!")
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
    print(data)
  else:
    print("Opção inválida")