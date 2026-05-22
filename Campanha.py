class Campanha:
    def __init__(self, titulo, descricao, data_inicio, data_fim, orcamento, criado_por):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__data_inicio = data_inicio
        self.__data_fim = data_fim
        self.__orcamento = orcamento
        self.__criado_por = criado_por

    def gettitulo(self):
        return self.__titulo

    def getdescricao(self):
        return self.__descricao

    def getdata_inicio(self):
        return self.__data_inicio

    def getdata_fim(self):
        return self.__data_fim

    def getorcamento(self):
        return self.__orcamento

    def getcriado_por(self):
        return self.__criado_por

    def to_dict(self):
        return {
            "Titulo": self.__titulo,
            "Descricao": self.__descricao,
            "Data Inicio": self.__data_inicio,
            "Data Fim": self.__data_fim,
            "Orcamento": self.__orcamento,
            "Criado Por": self.__criado_por
        }
