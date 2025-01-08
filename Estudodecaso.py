# PROJETO PYTHON
estoque = []


def exibir_menu():
    print("\n=== Sistema de Controle de Estoque ===")
    print("1. Adicionar Produto")
    print("2. Atualizar Produto")
    print("3. Excluir Produto")
    print("4. Visualizar Estoque")
    print("5. Sair")


def obter_preco():
    while True:
        try:
            preco = float(input("Preço do produto: R$ "))
            if preco < 0:
                raise ValueError("O preço não pode ser negativo.")
            return preco
        except ValueError:
            print("Por favor, insira um valor válido para o preço (somente números).")


def obter_quantidade():
    while True:
        try:
            quantidade = int(input("Quantidade em estoque: "))
            if quantidade < 0:
                raise ValueError("A quantidade não pode ser negativa.")
            return quantidade
        except ValueError:
            print("Por favor, insira um valor válido para a quantidade (somente números inteiros).")

def adicionar_produto():
    nome = input("Nome do produto: ").strip()
    preco = obter_preco()
    quantidade = obter_quantidade()
    
    for produto in estoque:
        if produto['nome'].lower() == nome.lower():
            print("Produto já existe no estoque. Use a opção de atualizar.")
            return
    
    
    estoque.append({"nome": nome, "preco": preco, "quantidade": quantidade})
    print("Produto adicionado com sucesso!")

def atualizar_produto():
    nome = input("Nome do produto para atualizar: ").strip()
    
   
    for produto in estoque:
        if produto['nome'].lower() == nome.lower():
            print("Produto encontrado! Insira os novos dados.")
            preco = obter_preco()
            quantidade = obter_quantidade()
            produto['preco'] = preco
            produto['quantidade'] = quantidade
            print("Produto atualizado com sucesso!")
            return
    
    print("Produto não encontrado no estoque.")

def excluir_produto():
    nome = input("Nome do produto para excluir: ").strip()
   
    for produto in estoque:
        if produto['nome'].lower() == nome.lower():
            estoque.remove(produto)
            print("Produto excluído com sucesso!")
            return
    
    print("Produto não encontrado no estoque.")


def visualizar_estoque():
    if not estoque:
        print("O estoque está vazio.")
    else:
        print("\n=== Estoque Atual ===")
        for produto in estoque:
            print(f"Nome: {produto['nome']}, Preço: R$ {produto['preco']:.2f}, Quantidade: {produto['quantidade']}")


def main():
    while True:
        exibir_menu()
        opcao = input("Selecione uma opção: ").strip()
        
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            atualizar_produto()
        elif opcao == "3":
            excluir_produto()
        elif opcao == "4":
            visualizar_estoque()
        elif opcao == "5":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
