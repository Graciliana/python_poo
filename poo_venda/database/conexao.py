import pymysql
import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()


class ConexaoMySQL:
    def __init__(self):
        # Carrega os dados de conexão do arquivo .env
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.db = os.getenv("DB_NAME")
        self.conexao = None

    def conectar(self):
        try:
            self.conexao = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db,  # Aqui usamos 'database' em vez de 'db'
            )
            print("Conexão com o banco de dados estabelecida!")
        except Exception as e:
            print(f"Erro ao conectar no banco de dados: {e}")

    def fechar_conexao(self):
        if self.conexao:
            self.conexao.close()
            print("Conexão com o banco de dados encerrada.")
