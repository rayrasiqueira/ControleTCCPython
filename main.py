from Aluno import Aluno
from Professor import Professor

professor: list = []
aluno: list = []
def menu():
    print('''
############ Controle de TCC ############

    1. Cadastrar professor
    2. Imprimir professor
    3. Consultar professor por nome
    4. Cadastrar aluno
    5. Imprimir aluno
    6. Consultar aluno por nome
    7. Finalizar
    ''')

def faixa():
    print("***"*12)

def buscar(nome: str, data:list):
    for posicao, item in enumerate(data):
        if item.nome == nome:
            return posicao
    return -1

def consultar(data: list, nome: str):
    posicao = buscar(nome, data)
    if posicao != -1:
        return data[posicao]
    else:
        return -1

if __name__ == '__main__':

    while True:
        try:
            menu()
            opcao = int(input("Informe a opção desejada: "))
            if opcao == 1:
                print("*** Cadastrar Professor ***\n")
                nome = input("Informe o nome: ")
                buscar_professor = consultar(data=professor, nome=nome)
                if buscar_professor != -1:
                    faixa()
                    print("\nProfessor ja cadastrado!\n")
                    faixa()
                else:
                    CPF = input("Informe o CPF: ")
                    email = input("Informe o email: ")
                    celular = input("Informe o celular: ")
                    titulacao = input("Informe o titulacao: ")
                    area_de_interesse = input("Informe o area de interesse: ")
                    professor_cadastrado = Professor(nome,CPF,email,celular,titulacao,area_de_interesse)
                    professor.append(professor_cadastrado)
                    faixa()
                    print("\nProfessor cadastrado com sucesso!\n")
                    faixa()

            elif opcao == 2:
                print("*** Professores cadastrados ***\n")
                print([item.imprimir() for item in professor])

            elif opcao == 3:
                print("*** Procurar professor ***\n")
                nome = input("Informe o nome: ")
                buscar_professor = consultar(data=professor, nome=nome)
                if buscar_professor != -1:
                    print("***"*30)
                    print(buscar_professor.imprimir(),"\n")
                else:
                    faixa()
                    print("\nProfessor não cadastrado!\n")
                    faixa()

            elif opcao == 4:
                print("*** Cadastrar Aluno ***\n")
                nome = input("Informe o nome: ")
                buscar_aluno = consultar(data=aluno, nome=nome)
                if buscar_aluno != -1:
                    faixa()
                    print("\nAluno ja cadastrado!\n")
                    faixa()
                else:
                    CPF = input("Informe o CPF: ")
                    email = input("Informe o email: ")
                    celular = input("Informe o celular: ")
                    RA = input("Informe o RA: ")
                    titulo_tcc = input("Informe o titulo do tcc: ")
                    orientador = input("Informe o professor orientador: ")
                    buscar_professor = consultar(data=professor, nome=orientador)
                    if buscar_professor != -1:
                        aluno_cadastrado = Aluno(nome,CPF,email,celular,RA,titulo_tcc, buscar_professor.imprimir())
                        aluno.append(aluno_cadastrado)
                        faixa()
                        print("\nAluno cadastrado com sucesso!\n")
                        faixa()
                    else:
                        faixa()
                        print("\nProfessor não cadastrado.")
                        print("Tente novamente!\n")
                        faixa()

            elif opcao == 5:
                print("*** Professores cadastrados ***\n")
                print([item.imprimir() for item in aluno])

            elif opcao == 6:
                print("*** Procurar Aluno ***\n")
                nome = input("Informe o nome: ")
                buscar_aluno = consultar(data=aluno, nome=nome)
                if buscar_aluno != -1:
                    print("***"*50)
                    print(buscar_aluno.imprimir(),"\n")
                else:
                    faixa()
                    print("\nAluno não cadastrado!\n")
                    faixa()

            elif opcao == 7:
                break
            
            else:
                print("\nInfome apenas números de [1-7]\n")

        except Exception as e:
            print("\nPor favor informe uma opção válida.\n")

