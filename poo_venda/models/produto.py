class Produto:
    def __init__(self, id_produto, nome, preco, categoria_id):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco
        self.categoria_id = categoria_id

    def salvar(self, conexao):
        cursor = conexao.cursor()
        sql = "INSERT INTO produtos (id_produto, nome, preco, categoria_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (self.id_produto, self.nome, self.preco, self.categoria_id))
        conexao.commit()
        print(f"Produto '{self.nome}' salvo com sucesso no banco de dados.")

    def __str__(self):
        return f"Produto: {self.nome}, Preço: R$ {self.preco}, Categoria ID: {self.categoria_id}"
