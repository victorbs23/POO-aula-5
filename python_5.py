class Funcionario:
    def __init__(self, nome, salario=0.0):
        self.nome = nome
        self.salario = salario

    def get_nome(self):
        return self.nome

    def get_salario(self):
        return self.salario

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_salario(self, novo_salario):
        self.salario = novo_salario

    def bonificacao(self):
        return (9/100) * self.salario

    def mostra_dados(self):
        print('Nome:', self.nome)
        print('Salario:', self.salario)


class Gerente(Funcionario):
    def __init__(self, nome, qtd_funcionarios, salario=0.0):
        super().__init__(nome, salario)

        self.qtd_funcionarios = qtd_funcionarios

    def get_qtd_funcionarios(self):
        return self.qtd_funcionarios

    def set_qtd_funcionarios(self, nova_qtd):
        self.qtd_funcionarios = nova_qtd

    def mostra_dados(self):
        print('Qtd. gerencia:', self.qtd_funcionarios)
