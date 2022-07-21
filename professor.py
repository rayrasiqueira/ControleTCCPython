from Pessoa import Pessoa


class Professor(Pessoa):

    def __init__(self, nome: str, CPF: str, email: str, celular: str, titulacao: str, area_de_interesse: str ) -> None:
        super().__init__(nome, CPF, email, celular)
        self.titulacao = titulacao
        self.area_de_interesse = area_de_interesse
    
    def imprimir(self) -> dict:
        return {
            'nome': self.nome,
            'CPF': self.CPF,
            'email': self.email,
            'celular': self.celular,
            'titulacao': self.titulacao,
            'area_de_interesse': self.area_de_interesse
        }
