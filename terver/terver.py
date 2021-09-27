from math import exp

# факториал
def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n


class FormulasCombinatorics:

# перестановки
    def permutations(self, n):
        return fac(n)

# сочетания m из n
    def combination(self, n, m):
        return fac(n)/(fac(n-m)*fac(m))

# размещения
    def accommodation(self,n, m):
        return self.combination(n, m) * self.permutations(m)


class FormulasTerver:

    def __init__(self, formulasCombinatorics):
        self.formulasCombinatorics = formulasCombinatorics

# вероятность события (m - благоприятные, n - все)
    def probability(self, n, m):
        return m/n

# вероятность появления хотя бы одного из двух совместных событий A, B
    def addition_of_probabilities(self, a, b):
        return a + b - a*b

# Бернули
    def bernoulli(self, n, m, p):
        return self.formulasCombinatorics.combination(n, m) * pow(p, m) * pow(1-p, n-m)

# Пуассон
    def poisson(self, n, m, p):
        return (pow(n*p, m) / fac(m)) * exp(-n*p)


fc = FormulasCombinatorics()
ft = FormulasTerver(fc)
while 1:
    print('0 - выход\n'
          '1 - посчитать кол-во перестановок\n'
          '2 - посчитать кол-во сочетаний\n'
          '3 - посчитать кол-во размещений\n'
          '4 - посчитать вероятность события\n'
          '5 - поcчитать вероятность появления хотя бы одного из двух совместых событий\n'
          '6 - посчитать вероятность по формуле Бернули\n'
          '7 - посчитать вероятность по формуле Пуассона')
    inpt = int(input('    ->'))
    if inpt == 0:
        exit()
    elif inpt == 5:
        a = int(input('P(a) = '))
        b = int(input('P(b) = '))
        print('P(A) = ', ft.addition_of_probabilities(a, b))
    else:
        n = int(input('n = '))
        if inpt == 1:
            print('P = ', fc.permutations(n))
        else:
            m = int(input('m = '))
            if inpt == 2:
                print('C = ',fc.combination(n, m))
            elif inpt == 3:
                print('A = ', fc.accommodation(n, m))
            elif inpt == 4:
                print('P(A) = ', ft.probability(n, m))
            else:
                p = float(input('p = '))
                if inpt == 6:
                    print('P(A) = ', ft.bernoulli(n, m, p))
                elif inpt == 7:
                    print(ft.poisson(n, m, p))
                else:
                    print('ERROR')
