class Endereco:
    def __init__(self, logradouro, bairro, cidade, estado, cep):
        self._id_endereco = None
        self._logradouro = logradouro
        self._bairro = bairro
        self._cidade = cidade
        self._estado = estado
        self._cep = cep

    # ID do Endereço
    @property
    def id_endereco(self):
        return self._id_endereco

    @id_endereco.setter
    def id_endereco(self, id_endereco):
        self._id_endereco = id_endereco

    # Logradouro
    @property
    def logradouro(self):
        return self._logradouro

    @logradouro.setter
    def logradouro(self, logradouro):
        self._logradouro = logradouro

    # Bairro
    @property
    def bairro(self):
        return self._bairro

    @bairro.setter
    def bairro(self, bairro):
        self._bairro = bairro

    # Cidade
    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, cidade):
        self._cidade = cidade

    # Estado
    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    # CEP
    @property
    def cep(self):
        return self._cep

    @cep.setter
    def cep(self, cep):
        self._cep = cep


