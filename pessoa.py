class Pessoa:

    def __init__(self, nome: str, CPF: str, email: str, celular: str) -> None:
        self.nome = nome
        self.CPF = CPF
        self.email = email
        self.celular = celular
    
    def imprimir(self) -> dict:
        return {
            'nome': self.nome,
            'CPF': self.CPF,
            'email': self.email,
            'celular': self.celular
        }
