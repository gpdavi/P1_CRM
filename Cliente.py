class Cliente:
    def __init__(self, nome, email, telefone, cidade, valor, status):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__cidade = cidade
        self.__valor = valor
        self.__status = status
    
    def getnome(self):
        return self.__nome
    
    def setnome(self, nome):
        self.__nome = nome

    def getemail(self):
        return self.__email
    
    def setemail(self, email):
        self.__email = email
    
    def gettelefone(self):
        return self.__telefone
    
    def settelefone(self, telefone):
        self.__telefone = telefone
      
    def getcidade(self):
        return self.__cidade
    
    def getvalor(self):
        return self.__valor
    
    def getstatus(self):
        return self.__status
    
    def setstatus(self, status):
        match status:
            case 1:
                return "Lead"
            case 2:
                return "Em contato" 
            case 3:
                return "Negociando"
            case 4:
                return "Fechado"
            case 5:
                return "Perdido"
    
    def to_dict(self):
        cliente = {
                "Nome": self.__nome, 
                "Email": self.__email, 
                "Telefone": self.__telefone, 
                "Cidade": self.__cidade, 
                "Valor": self.__valor, 
                "Status": self.__status}
        return cliente

    