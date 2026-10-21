from python_5 import Funcionario
from python_5 import Gerente

if __name__ == '__main__':
    f1 = Funcionario('Paulo', 3000.00)
    print(f1)

    f2 = Funcionario('Ana')
    print(f2)

    print('\n--------------------------------')

    print('- Funcionario 1: \nNome:', f1.get_nome())
    print('Salario:', f1.get_salario())
    f1.set_nome('Vinicius')
    print('Nome alterado:', f1.get_nome())
    print('\n--------------------------------')

    print('- Funcionario 2: \nNome:', f2.get_nome())
    print('Salario:', f2.get_salario())
    f2.set_nome('Emily')
    print('Nome alterado:', f2.get_nome())




    gerente_1 = Gerente('Fabio', 2, 5000.00)
    gerente_2 = Gerente('Matheus', 4, 4700.00)

    print('\n--------------------------------')

    print('Gentente 1: \nNome', gerente_1.get_nome())
    print('Salario:', gerente_1.get_salario())
    gerente_1.set_salario(5000.00)
    print('Salario alterado:', gerente_1.get_salario())
    print('Subordinados:', gerente_1.get_qtd_funcionarios())

    print('\n--------------------------------')

    print('- Gerente 2: \nNome:', gerente_2.get_nome())
    print('Salario:', gerente_2.get_salario())

    print('Bonificação do funcionario 1:', f1.bonificacao())

    f1.mostra_dados()