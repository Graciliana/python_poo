class Categoria:
    def __init__(self, id_categoria, nome):
        self.id_categoria = id_categoria
        self.nome = nome

    def salvar(self, conexao):
        cursor = conexao.cursor()
        sql = "INSERT INTO categorias (id_categoria, nome) VALUES (%s, %s)"
        cursor.execute(sql, (self.id_categoria, self.nome))
        conexao.commit()
        print(f"Categoria '{self.nome}' salva com sucesso no banco de dados.")

    def __str__(self):
        return f"Categoria: {self.nome}"
