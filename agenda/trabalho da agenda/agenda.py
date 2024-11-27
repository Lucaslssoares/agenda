agenda = [] # Lista para guardar os contatos

def mostrar_menu():
    print("\033[7;37;40mMenu da agenda: \033[m")
    print("\033[0;32;40m1. Incluir novo contato\033[m")
    print("\033[0;33;40m2. Buscar um contato\033[m")
    print("\033[0;34;40m3. Editar um contato\033[m")
    print("\033[0;35;40m4. Excluir um contato\033[m")
    print("\033[0;36;40m5. Listar todos os contatos\033[m")
    print("\033[0;31;40m6. Sair\033[m")

def incluir_contato():
    nome = input("Digite o seu nome completo: ")
    email = input("Digite o seu email: ")
    telefone = input("Digite o seu telefone: ")
    contato = {
        "Nome": nome,
        "Email": email,
        "Telefone": telefone
    }
    agenda.append(contato)
    print("Contato adicionado com sucesso!")

def buscar_contato():
    termo = input("Digite o seu nome, email ou telefone do contato que deseja buscar: ")
    contatos_encontrados = []
    for contato in agenda:
        if termo.lower() in contato["Nome"].lower() or termo.lower() in contato["Email"].lower() or termo in contato["Telefone"]:
            contatos_encontrados.append(contato)
    if contatos_encontrados:
        print("Contatos encontrados:")
        for contato in contatos_encontrados:
            print(f"Nome: {contato['Nome']}, Email: {contato['Email']}, Telefone: {contato['Telefone']}")
    else:
        print("Nenhum contato encontrado.")

def editar_contato():
    termo = input("Digite o nome, email ou telefone do contato que deseja editar: ")
    contatos_encontrados = []
    for i, contato in enumerate(agenda):
        if termo.lower() in contato["Nome"].lower() or termo.lower() in contato["Email"].lower() or termo in contato["Telefone"]:
            contatos_encontrados.append((i, contato))
    if contatos_encontrados:
        print("Contatos encontrados:")
        for i, contato in contatos_encontrados:
            print(f"Índice: {i}, Nome: {contato['Nome']}, Email: {contato['Email']}, Telefone: {contato['Telefone']}")
        indice = int(input("Digite o índice do contato que deseja editar: "))
        contato = contatos_encontrados[indice]
        novonome = input("Digite o novo nome completo (deixe em branco para não alterar): ")
        novoemail = input("Digite o novo email (deixe em branco para não alterar): ")
        novotelefone = input("Digite o novo telefone (deixe em branco para não alterar): ")
        if novonome:
            contato["Nome"] = novonome
        if novoemail:
            contato["Email"] = novoemail
        if novotelefone:
            contato["Telefone"] = novotelefone
        print("Contato atualizado com sucesso!!!")
    else:
        print("Nenhum contato encontrado.")

def excluir_contato():
    termo = input("Digite o nome, email ou telefone do contato que deseja excluir: ")
    contatos_encontrados = []
    for i, contato in enumerate(agenda):
        if termo.lower() in contato["Nome"].lower() or termo.lower() in contato["Email"].lower() or termo in contato["Telefone"]:
            contatos_encontrados.append((i, contato))
    if contatos_encontrados:
        print("Contatos encontrados:")
        for i, contato in contatos_encontrados:
            print(f"Índice: {i}, Nome: {contato['Nome']}, Email: {contato['Email']}, Telefone: {contato['Telefone']}")
        indice = int(input("Digite o índice do contato que deseja excluir: "))
        del agenda[contatos_encontrados[indice][0]]
        print("Contato excluído com sucesso!")
    else:
        print("Nenhum contato encontrado.")

def listar_contatos():
    if agenda:
        print("Lista de Contatos:")
        for i, contato in enumerate(agenda):
            print(f"Índice: {i}, Nome: {contato['Nome']}, Email: {contato['Email']}, Telefone: {contato['Telefone']}")
    else:
        print("A agenda está vazia.")

while True:
    mostrar_menu()
    opcao = input("Digite a opção desejada:")
    if opcao == "1":
        incluir_contato()
    elif opcao == "2":
        buscar_contato()
    elif opcao == "3":
        editar_contato()
    elif opcao == "4":
        excluir_contato()
    elif opcao == "5":
        listar_contatos()
    elif opcao == "6":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
