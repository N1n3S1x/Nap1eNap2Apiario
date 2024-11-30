class OperacoesBanco:
    def __init__(self, conexao):
        """
        Inicializa a classe de operações com uma conexão ao banco de dados.
        :param conexao: Objeto de conexão ao banco de dados (ConexaoBanco).
        """
        self.conexao = conexao.conexao

    # Métodos para Endereço
    def cadastrar_endereco(self, endereco):
        """
        Cadastra um endereço na tabela 'endereco'.
        :param endereco: Objeto da classe Endereco.
        """
        try:
            cursor = self.conexao.cursor()
            query = """
                INSERT INTO endereco (logradouro, bairro, cidade, estado, cep)
                VALUES (%s, %s, %s, %s, %s)
            """
            valores = (
                endereco.get_logradouro(),
                endereco.get_bairro(),
                endereco.get_cidade(),
                endereco.get_estado(),
                endereco.get_cep(),
            )
            cursor.execute(query, valores)
            self.conexao.commit()
            print("Endereço cadastrado com sucesso!")
            cursor.close()
        except Exception as e:
            print(f"Erro ao cadastrar o endereço: {e}")

    def buscar_endereco(self, id_endereco):
        """
        Busca um endereço pelo ID.
        :param id_endereco: ID do endereço.
        :return: Dicionário com os dados do endereço ou None se não encontrado.
        """
        try:
            cursor = self.conexao.cursor(dictionary=True)
            query = "SELECT * FROM endereco WHERE id_endereco = %s"
            cursor.execute(query, (id_endereco,))
            endereco = cursor.fetchone()
            cursor.close()
            return endereco
        except Exception as e:
            print(f"Erro ao buscar o endereço: {e}")
            return None

    def atualizar_endereco(self, id_endereco, logradouro=None, bairro=None, cidade=None, estado=None, cep=None):
        """
        Atualiza os dados de um endereço.
        :param id_endereco: ID do endereço.
        :param logradouro: Novo logradouro (opcional).
        :param bairro: Novo bairro (opcional).
        :param cidade: Nova cidade (opcional).
        :param estado: Novo estado (opcional).
        :param cep: Novo CEP (opcional).
        """
        try:
            cursor = self.conexao.cursor()
            query = "UPDATE endereco SET "
            valores = []

            if logradouro:
                query += "logradouro = %s, "
                valores.append(logradouro)
            if bairro:
                query += "bairro = %s, "
                valores.append(bairro)
            if cidade:
                query += "cidade = %s, "
                valores.append(cidade)
            if estado:
                query += "estado = %s, "
                valores.append(estado)
            if cep:
                query += "cep = %s, "
                valores.append(cep)

            query = query.rstrip(", ") + " WHERE id_endereco = %s"
            valores.append(id_endereco)

            cursor.execute(query, tuple(valores))
            self.conexao.commit()
            print("Endereço atualizado com sucesso!")
            cursor.close()
        except Exception as e:
            print(f"Erro ao atualizar o endereço: {e}")

    def excluir_endereco(self, id_endereco):
        """
        Exclui um endereço pelo ID.
        :param id_endereco: ID do endereço.
        """
        try:
            cursor = self.conexao.cursor()
            query = "DELETE FROM endereco WHERE id_endereco = %s"
            cursor.execute(query, (id_endereco,))
            self.conexao.commit()
            print("Endereço excluído com sucesso!")
            cursor.close()
        except Exception as e:
            print(f"Erro ao excluir o endereço: {e}")

    # Métodos para Usuário
    def cadastrar_usuario(self, usuario):
        """
        Cadastra um usuário na tabela 'usuario'.
        :param usuario: Objeto da classe Usuario.
        """
        try:
            cursor = self.conexao.cursor()
            query = """
                INSERT INTO usuario (nome_apicultor, email, endereco)
                VALUES (%s, %s, %s)
            """
            valores = (
                usuario.get_nome(),
                usuario.get_email(),
                usuario.get_endereco_id(),
            )
            cursor.execute(query, valores)
            self.conexao.commit()
            print("Usuário cadastrado com sucesso!")
            cursor.close()
        except Exception as e:
            print(f"Erro ao cadastrar o usuário: {e}")

    def buscar_usuario(self, id_usuario):
        """
        Busca um usuário pelo ID.
        :param id_usuario: ID do usuário.
        :return: Dicionário com os dados do usuário ou None se não encontrado.
        """
        try:
            cursor = self.conexao.cursor(dictionary=True)
            query = "SELECT * FROM usuario WHERE id_usuario = %s"
            cursor.execute(query, (id_usuario,))
            usuario = cursor.fetchone()
            cursor.close()
            return usuario
        except Exception as e:
            print(f"Erro ao buscar o usuário: {e}")
            return None

    def atualizar_usuario(self, id_usuario, nome=None, email=None, endereco_id=None):
        """
        Atualiza os dados de um usuário.
        :param id_usuario: ID do usuário.
        :param nome: Novo nome (opcional).
        :param email: Novo email (opcional).
        :param endereco_id: Novo ID do endereço (opcional).
        """
        try:
            cursor = self.conexao.cursor()
            query = "UPDATE usuario SET "
            valores = []

            if nome:
                query += "nome_apicultor = %s, "
                valores.append(nome)
            if email:
                query += "email = %s, "
                valores.append(email)
            if endereco_id:
                query += "endereco = %s, "
                valores.append(endereco_id)

            query = query.rstrip(", ") + " WHERE id_usuario = %s"
            valores.append(id_usuario)

            cursor.execute(query, tuple(valores))
            self.conexao.commit()
            print("Usuário atualizado com sucesso!")
            cursor.close()
        except Exception as e:
            print(f"Erro ao atualizar o usuário: {e}")

    def excluir_usuario(self, id_usuario):
        """
        Exclui um usuário pelo ID.
        :param id_usuario: ID do usuário.
        """
        try:
            cursor = self.conexao.cursor()
            query = "DELETE FROM usuario WHERE id_usuario = %s"
            cursor.execute(query, (id_usuario,))
            self.conexao.commit()
            print("Usuário excluído com sucesso!")
            cursor.close()
        except Exception as e:
            print(f"Erro ao excluir o usuário: {e}")