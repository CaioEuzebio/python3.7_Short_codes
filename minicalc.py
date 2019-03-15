ops = [1,2,3,4]
op = int(input("""Digite a operação: 
                    1 - Soma 
                    2 - Subtração 
                    3 - Divisão 
                    4 - Multiplicação  
                    Operação : """))
if op not in ops:
    print('Operacao invalida')
else:
    n1 = float(input('Digite o primeiro valor: ')); n2 = float(input('Digite o segundo valor: '))


class Calc:
    def __init__(self):
        self.sum1 = n1 + n2
        self.subt1 = n1 - n2
        self.div1 = n1 %n2
        self.mult1 = n1 * n2
calcular = Calc()
if op == 1:
    print('o Resultado da soma é: ', calcular.sum1)
elif op == 2:
    print('o Resultado da Subtração é: ', calcular.subt1)
elif op == 3:
    print('o Resultado é Divisão: ', calcular.div1)
else:
    op == 4
    print("o Resultado é Multiplicação: ", calcular.mult1)


