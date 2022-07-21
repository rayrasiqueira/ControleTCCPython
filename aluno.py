from Pessoa import Pessoa
from Professor import Professor


class Aluno(Pessoa):

    def __init__(self, nome: str, CPF: str, email: str, celular: str, RA: str, titulo_tcc: str, orientador: Professor ) -> None:
        super().__init__(nome, CPF, email, celular)
        self.RA = RA
        self.titulo_tcc = titulo_tcc
        self.orientador = orientador
    
    def imprimir(self) -> dict:
        return {
            'nome': self.nome,
            'CPF': self.CPF,
            'email': self.email,
            'celular': self.celular,
            'RA': self.RA,
            'titulo_tcc': self.titulo_tcc,
            'orientador': self.orientador
        }
