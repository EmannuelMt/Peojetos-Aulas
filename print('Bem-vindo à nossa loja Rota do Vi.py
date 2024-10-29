print('Bem-vindo à nossa loja Rota do Vinho!')

class Vinho:
    def __init__(self, nome, tipo, uva, safra, pais, preco):
        self.nome = nome
        self.tipo = tipo
        self.uva = uva
        self.safra = safra
        self.pais = pais
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - {self.tipo} - {self.uva} - {self.safra} - {self.pais} - R${self.preco:.2f}"

class CatalogoDeVinhos:
    def __init__(self):
        self.vinhos = []

    def adicionar_vinho(self, vinho):
        self.vinhos.append(vinho)

    def mostrar_catalogo(self):
        for vinho in self.vinhos:
            print(vinho)

    def filtrar_por_tipo(self, tipo):
        filtrados = [vinho for vinho in self.vinhos if vinho.tipo.lower() == tipo.lower()]
        return filtrados

    def filtrar_por_preco(self, preco_max):
        filtrados = [vinho for vinho in self.vinhos if vinho.preco <= preco_max]
        return filtrados

# Função para adicionar item ao carrinho
def add_item(carrinho, vinho, quantidade):
    if vinho.nome in carrinho:
        carrinho[vinho.nome]['quantidade'] += quantidade
    else:
        carrinho[vinho.nome] = {'quantidade': quantidade, 'preco': vinho.preco}
    print(f'{quantidade}x {vinho.nome} adicionado ao carrinho.')

# Criando o catálogo de vinhos
catalogo = CatalogoDeVinhos()

# Adicionando vinhos ao catálogo
catalogo.adicionar_vinho(Vinho("Cabernet Sauvignon Reserva", "Tinto", "Cabernet Sauvignon", 2018, "Chile", 79.90))
catalogo.adicionar_vinho(Vinho("Malbec Gran Reserva", "Tinto", "Malbec", 2019, "Argentina", 120.00))
catalogo.adicionar_vinho(Vinho("Chardonnay Premium", "Branco", "Chardonnay", 2020, "Brasil", 65.50))
catalogo.adicionar_vinho(Vinho("Merlot Suave", "Tinto", "Merlot", 2021, "Brasil", 45.90))
catalogo.adicionar_vinho(Vinho("Prosecco Brut", "Espumante", "Glera", 2021, "Itália", 89.99))
catalogo.adicionar_vinho(Vinho("Rosé Provence", "Rosé", "Grenache", 2022, "França", 95.00))
catalogo.adicionar_vinho(Vinho("Riesling Mosel", "Branco", "Riesling", 2019, "Alemanha", 130.00))

# Criando um carrinho de compras
carrinho = {}

# Menu de interação com o cliente
while True:
    print("\nO que você gostaria de fazer?")
    print("1. Ver catálogo completo")
    print("2. Filtrar vinhos por tipo")
    print("3. Filtrar vinhos por preço")
    print("4. Adicionar vinho ao carrinho")
    print("5. Ver carrinho")
    print("6. Finalizar compra")
    print("7. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\nCatálogo completo de vinhos:\n")
        catalogo.mostrar_catalogo()

    elif opcao == "2":
        tipo = input("Digite o tipo de vinho que deseja (Tinto, Branco, Rosé, Espumante): ")
        filtrados = catalogo.filtrar_por_tipo(tipo)
        if filtrados:
            print(f"\nVinhos do tipo {tipo}:\n")
            for vinho in filtrados:
                print(vinho)
        else:
            print(f"\nNenhum vinho encontrado do tipo {tipo}.")

    elif opcao == "3":
        preco_max = float(input("Digite o preço máximo: "))
        filtrados = catalogo.filtrar_por_preco(preco_max)
        if filtrados:
            print(f"\nVinhos até R${preco_max:.2f}:\n")
            for vinho in filtrados:
                print(vinho)
        else:
            print(f"\nNenhum vinho encontrado até R${preco_max:.2f}.")

    elif opcao == "4":
        nome_vinho = input("Digite o nome do vinho que deseja adicionar ao carrinho: ")
        quantidade = int(input("Digite a quantidade: "))
        vinho_encontrado = next((vinho for vinho in catalogo.vinhos if vinho.nome.lower() == nome_vinho.lower()), None)
        if vinho_encontrado:
            add_item(carrinho, vinho_encontrado, quantidade)
        else:
            print(f"Vinho {nome_vinho} não encontrado no catálogo.")

    elif opcao == "5":
        if carrinho:
            print("\nCarrinho de compras:")
            for item, detalhes in carrinho.items():
                print(f"{detalhes['quantidade']}x {item} - R${detalhes['preco']:.2f} cada")
        else:
            print("\nSeu carrinho está vazio.")

    elif opcao == "6":
        if carrinho:
            total = sum(detalhes['quantidade'] * detalhes['preco'] for detalhes in carrinho.values())
            print(f"\nTotal da compra: R${total:.2f}")
            print("Compra finalizada! Obrigado por escolher a Rota do Vinho.")
            break
        else:
            print("\nSeu carrinho está vazio. Adicione vinhos antes de finalizar a compra.")

    elif opcao == "7":
        print("Obrigado por visitar a Rota do Vinho. Até a próxima!")
        break

    else:
        print("Opção inválida. Tente novamente.")