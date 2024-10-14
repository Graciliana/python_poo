class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        self.itens.append((produto, quantidade))

    def remover_item(self, produto):
        self.itens = [item for item in self.itens if item[0] != produto]

    def listar_itens(self):
        print("Itens no carrinho:")
        for produto, quantidade in self.itens:
            print(
                f"{produto.nome} - Quantidade: {quantidade} - Preço Unitário: R$ {produto.preco}"
            )

    def calcular_total(self):
        total = sum(produto.preco * quantidade for produto, quantidade in self.itens)
        return total
