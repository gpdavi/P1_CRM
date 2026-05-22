class Oportunidade:
    def __init__(self, vendedor, cliente, data_inicio, data_fim, valor, campanha=None):
        self.__vendedor = vendedor
        self.__cliente = cliente
        self.__data_inicio = data_inicio
        self.__data_fim = data_fim
        self.__valor = valor
        self.__campanha = campanha 
        self.__status = "Pendente" 

    def getstatus(self):
        return self.__status

    def setstatus(self, status):
        self.__status = status

    def getvendedor(self):
        return self.__vendedor

    def getcliente(self):
        return self.__cliente

    def getdata_inicio(self):
        return self.__data_inicio

    def getdata_fim(self):
        return self.__data_fim

    def getvalor(self):
        return self.__valor

    def getcampanha(self):
        return self.__campanha

    def to_dict(self):
        return {
            "Vendedor": self.__vendedor,
            "Cliente": self.__cliente,
            "Data Inicio": self.__data_inicio,
            "Data Fim": self.__data_fim,
            "Valor": self.__valor,
            "Campanha": self.__campanha,
            "Status": self.__status
        }
