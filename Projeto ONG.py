# Projeto ONG

from datetime import datetime

class Crianca:
    def __init__(self, nome, idade, responsavel, doenca=None):
        self.nome = nome
        self.idade = idade
        self.responsavel = responsavel
        self.atividades = []
        self.doenca = doenca
        self.data_entrada = datetime.now().strftime("%d/%m/%Y")

    def mostrar(self):
        print(f"Nome da Criança: {self.nome}")
        print(f"Idade da Criança: {self.idade}")
        print(f"Responsavel da Criança: {self.responsavel}")
        print(f"Doença/Condição: {self.doenca if self.doenca else 'Nenhuma Registrada'}")
        print(f"Atividades da Criança: {self.atividades if self.atividades else 'Nenhuma Atividade'}")
        print(f"Data do Registro: {self.data_entrada}")

class SistemaCadastro:
    def __init__(self):
        self.criancas = {}
        self.proximo_id = 1

    def cadastrar(self, nome, idade, responsavel, doenca=None):
        crianca_c = Crianca(nome, idade , responsavel, doenca)
        self.criancas[self.proximo_id] = crianca_c
        print(f"Criança {nome} Cadastrada com sucesso! (ID: {self.proximo_id})")
        self.proximo_id += 1

    def listar(self):
        for id, crianca in self.criancas.items():
            print(f"ID:{id}")
            crianca.mostrar()
            print("-" * 5)




sistema = SistemaCadastro()
sistema.cadastrar("julia", 4, "roberto")
sistema.cadastrar("Pedro", 7, "Ana", "Asma")

print("\n--- Listagem ---")
sistema.listar()