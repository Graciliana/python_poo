class Venda:
    def __init__(self, id_venda, total, data_venda):
        self.id_venda = id_venda
        self.total = total
        self.data_venda = data_venda

    def salvar(self, conexao):
        cursor = conexao.cursor()
        sql = "INSERT INTO vendas (id_venda, total, data_venda) VALUES (%s, %s, %s)"
        cursor.execute(sql, (self.id_venda, self.total, self.data_venda))
        conexao.commit()
        print(f"Venda ID {self.id_venda} salva com sucesso no banco de dados.")

    def __str__(self):
        return f"Venda ID: {self.id_venda}, Total: R$ {self.total}, Data: {self.data_venda}"
