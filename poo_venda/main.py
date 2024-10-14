from database.conexao import ConexaoMySQL
from models.produto import Produto
from models.categoria import Categoria
from services.carrinho import Carrinho

# Inicializando a conexão com o banco de dados
conexao_mysql = ConexaoMySQL()  # Não passe argumentos aqui
conexao_mysql.conectar()

# Criando categorias e salvando no banco
categoria_eletronicos = Categoria(1, "Eletrônicos")
categoria_eletronicos.salvar(conexao_mysql.conexao)

# Criando produtos e salvando no banco
produto1 = Produto(1, "Notebook", 4500, categoria_eletronicos.id_categoria)
produto1.salvar(conexao_mysql.conexao)

produto2 = Produto(2, "Smartphone", 1500, categoria_eletronicos.id_categoria)
produto2.salvar(conexao_mysql.conexao)

# Simulando um carrinho de compras
carrinho = Carrinho()
carrinho.adicionar_item(produto1, 1)
carrinho.adicionar_item(produto2, 2)

# Listando itens e total do carrinho
carrinho.listar_itens()
print(f"Total do carrinho: R$ {carrinho.calcular_total()}")

# Fechando a conexão com o banco de dados
conexao_mysql.fechar_conexao()
