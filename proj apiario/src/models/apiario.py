class Apiario:
    def __init__(self, nome_apiario, localizacao, tamanho, id_apicultor):
        self._nome_apiario = nome_apiario
        self._localizacao = localizacao
        self._tamanho = tamanho
        self._id_apicultor = id_apicultor

    # Nome do Apiário
    @property
    def nome_apiario(self):
        return self._nome_apiario

    @nome_apiario.setter
    def nome_apiario(self, novo_nome_apiario):
        self._nome_apiario = novo_nome_apiario

    # Localização
    @property
    def localizacao(self):
        return self._localizacao

    @localizacao.setter
    def localizacao(self, nova_localizacao):
        self._localizacao = nova_localizacao

    # Tamanho
    @property
    def tamanho(self):
        return self._tamanho

    @tamanho.setter
    def tamanho(self, novo_tamanho):
        self._tamanho = novo_tamanho

    # ID do Apicultor
    @property
    def id_apicultor(self):
        return self._id_apicultor

    @id_apicultor.setter
    def id_apicultor(self, novo_id_apicultor):
        self._id_apicultor = novo_id_apicultor



# apiario = Apiario()
