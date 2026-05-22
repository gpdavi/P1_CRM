
from Dados import Dados
class Usuario:
    def __init__ (self, nomeusuario, senha, email, cargo):
        self.__nomeusuario = nomeusuario
        self.__senha = senha
        self.__email = email
        self.__cargo = cargo

    def getusuario(self):
        return self.__nomeusuario
    
    def setusuario(self, nomeusuario):
        self.nomeusuario = nomeusuario

    def getsenha(self):
        return self.__senha
    
    def setsenha(self, senha):
        self.__senha = senha

    def getemail(self):
        return self.__email
    
    def setemail(self, email):
        self.__email = email

    def getcargo(self):
        return self.__cargo

    def setcargo(self, cargo):
        match cargo:
            case "1":
                self.__cargo = "Gerente"
            case "2":
                self.__cargo = "Vendedor"


    def to_dict(self):
        usuario = {
                "Nome de Usuario": self.__nomeusuario, 
                "Senha": self.__senha, 
                "Email": self.__email, 
                "Cargo": self.__cargo}
        return usuario
        