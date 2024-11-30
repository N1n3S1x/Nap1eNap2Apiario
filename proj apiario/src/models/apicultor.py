class Apicultor:
    def __init__(self, nome_apicultor, endereco=None, numero=None, complemento=None, email=None, telefone=None):
        """
        Inicializa um objeto Apicultor.

        :param nome_apicultor: Nome do apicultor (obrigatório)
        :param endereco: ID do endereço (referência à tabela endereco)
        :param numero: Número do endereço
        :param complemento: Complemento do endereço
        :param email: E-mail do apicultor
        :param telefone: Telefone do apicultor
        """
        self._id_apicultor = None  # Será gerado automaticamente pelo banco de dados
        self._nome_apicultor = nome_apicultor
        self._endereco = endereco
        self._numero = numero
        self._complemento = complemento
        self._email = email
        self._telefone = telefone

    # ID do Apicultor
    @property
    def id_apicultor(self):
        return self._id_apicultor

    @id_apicultor.setter
    def id_apicultor(self, id_apicultor):
        self._id_apicultor = id_apicultor

    # Nome do Apicultor
    @property
    def nome_apicultor(self):
        return self._nome_apicultor

    @nome_apicultor.setter
    def nome_apicultor(self, nome_apicultor):
        self._nome_apicultor = nome_apicultor

    # Endereço (ID do endereço)
    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    # Número
    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    # Complemento
    @property
    def complemento(self):
        return self._complemento

    @complemento.setter
    def complemento(self, complemento):
        self._complemento = complemento

    # E-mail
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    # Telefone
    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone



