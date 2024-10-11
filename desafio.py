# ------------------------------------------------------------------- #

def mostrar_menu():
    print("""✧ Escolha uma opção:
""")
    print("1 - Adicionar contato")
    print("2 - Visualizar contatos")
    print("3 - Editar contato")
    print("4 - Marcar/desmarcar favorito")
    print("5 - Listar favoritos")
    print("6 - Apagar contato")
    print("""0 - Sair
          """)

# ------------------------------------------------------------------- #

def adicionar_contato(contatos):
    nome = input("""
                ✧ Preencha as informações do contato:
                Nome: """)
    telefone = input("                Telefone: ")
    email = input("                Email: ")
    contatos.append({'nome': nome, 'telefone': telefone, 'email': email, 'favorito': False})

# ------------------------------------------------------------------- #

def visualizar_contatos(contatos):
    if not contatos:
        print("Lista de contatos vazia. :c")
        return

    for i, contato in enumerate(contatos):
        favorito = "★" if contato['favorito'] else "☆"
        print("""
✧ Seus contatos:""")
        print(f"{i + 1}. {contato['nome']} - {contato['telefone']} - {contato['email']} {favorito}")

# ------------------------------------------------------------------- #

def editar_contato(contatos):
    visualizar_contatos(contatos)
    indice = int(input("✧ Escolha o contato a editar: ")) - 1
    if 0 <= indice < len(contatos):
        contatos[indice]['nome'] = input("Novo nome: ")
        contatos[indice]['telefone'] = input("Novo telefone: ")
        contatos[indice]['email'] = input("Novo email: ")

# ------------------------------------------------------------------- #

def marcar_favorito(contatos):
    visualizar_contatos(contatos)
    indice = int(input("✧ Escolha o contato para marcar/desmarcar favorito: ")) - 1
    if 0 <= indice < len(contatos):
        contatos[indice]['favorito'] = not contatos[indice]['favorito']

# ------------------------------------------------------------------- #

def listar_favoritos(contatos):
    favoritos = [c for c in contatos if c['favorito']]
    visualizar_contatos(favoritos)
    if not favoritos:
        print("Lista de favoritos vazia. :c")

# ------------------------------------------------------------------- #

def apagar_contato(contatos):
    visualizar_contatos(contatos)
    indice = int(input("✧ Escolha o contato a apagar: ")) - 1
    if 0 <= indice < len(contatos):
        contatos.pop(indice)

# ------------------------------------------------------------------- #

def main():
    contatos = []
    while True:
        mostrar_menu()
        opcao = input("✧ Opção: ")
        if opcao == "1":
            adicionar_contato(contatos)
        elif opcao == "2":
            visualizar_contatos(contatos)
        elif opcao == "3":
            editar_contato(contatos)
        elif opcao == "4":
            marcar_favorito(contatos)
        elif opcao == "5":
            listar_favoritos(contatos)
        elif opcao == "6":
            apagar_contato(contatos)
        elif opcao == "0":
            break
        else:
            print("Opção inválida!! Tente novamente.")

# ------------------------------------------------------------------- #

main() # :D

# ------------------------------------------------------------------- #
