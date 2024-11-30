class OperacoesBanco:
    def __init__(self, conexao):
        """
        Inicializa a classe de operações com uma conexão ao banco de dados.
        :param conexao: Objeto de conexão ao banco de dados (ConexaoBanco).
        """
        self.conexao = conexao.conexao

    def inserir(self, tabela, colunas, valores):
        """
        Insere um novo registro em uma tabela.
        :param tabela: Nome da tabela.
        :param colunas: Lista de colunas para inserção.
        :param valores: Lista de valores correspondentes às colunas.
        """
        try:
            cursor = self.conexao.cursor()
            query = f"INSERT INTO {tabela} ({', '.join(colunas)}) VALUES ({', '.join(['%s'] * len(valores))})"
            cursor.execute(query, valores)
            self.conexao.commit()
            print(f"Registro inserido com sucesso na tabela '{tabela}'.")
            cursor.close()
        except Exception as e:
            print(f"Erro ao inserir registro na tabela '{tabela}': {e}")

    def buscar_por_id(self, tabela, id_coluna, id_valor):
        """
        Busca um registro em uma tabela pelo ID.
        :param tabela: Nome da tabela.
        :param id_coluna: Nome da coluna de ID.
        :param id_valor: Valor do ID a ser buscado.
        :return: Dicionário com os dados do registro ou None se não encontrado.
        """
        try:
            cursor = self.conexao.cursor(dictionary=True)
            query = f"SELECT * FROM {tabela} WHERE {id_coluna} = %s"
            cursor.execute(query, (id_valor,))
            registro = cursor.fetchone()
            cursor.close()
            return registro
        except Exception as e:
            print(f"Erro ao buscar registro na tabela '{tabela}': {e}")
            return None

    def atualizar(self, tabela, id_coluna, id_valor, dados):
        """
        Atualiza um registro em uma tabela.
        :param tabela: Nome da tabela.
        :param id_coluna: Nome da coluna de ID.
        :param id_valor: Valor do ID a ser atualizado.
        :param dados: Dicionário com as colunas e valores a serem atualizados.
        """
        try:
            cursor = self.conexao.cursor()
            set_clause = ", ".join([f"{coluna} = %s" for coluna in dados.keys()])
            valores = list(dados.values()) + [id_valor]
            query = f"UPDATE {tabela} SET {set_clause} WHERE {id_coluna} = %s"
            cursor.execute(query, valores)
            self.conexao.commit()
            print(f"Registro atualizado com sucesso na tabela '{tabela}'.")
            cursor.close()
        except Exception as e:
            print(f"Erro ao atualizar registro na tabela '{tabela}': {e}")

    def excluir(self, tabela, id_coluna, id_valor):
        """
        Exclui um registro de uma tabela pelo ID.
        :param tabela: Nome da tabela.
        :param id_coluna: Nome da coluna de ID.
        :param id_valor: Valor do ID a ser excluído.
        """
        try:
            cursor = self.conexao.cursor()
            query = f"DELETE FROM {tabela} WHERE {id_coluna} = %s"
            cursor.execute(query, (id_valor,))
            self.conexao.commit()
            print(f"Registro excluído com sucesso da tabela '{tabela}'.")
            cursor.close()
        except Exception as e:
            print(f"Erro ao excluir registro da tabela '{tabela}': {e}")