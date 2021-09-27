from math import exp
'''
This program is designed to help in solving problems of the theory of probability.
'''

# факториал
def fac(n):
    '''
    Function fac
    Returns the factorial of a number

    :param n: the number for which we are looking for the factorial, non-negative
    :return: factorial of n
    '''
    if n < 0:
        return -1
    if n == 0:
        return 1
    return fac(n-1) * n


class FormulasCombinatorics:
    '''
    Class FormulasCombinatorics containing combinatorial formulas
    '''

# перестановки
    def permutations(self, n):
        '''
        Function permutations
        Returns the number of permutations
        :param n: amount of elements, natural number
        :return: number of permutations, natural number
        '''
        if n > 0 and isinstance(n, int):
            return fac(n)
        else:
            return -1

# сочетания m из n
    def combination(self, n, m):
        '''
        Function combination
        Returns the number of combinations
        :param n: total number of objects, natural number
        :param m: number of objects in the sample, natural number
        :return: number of combinations, natural number
        '''
        if n > 0 and isinstance(n, int) and m > 0 and isinstance(m, int):
            return fac(n)/(fac(n-m)*fac(m))
        else: return -1

# размещения
    def accommodation(self, n, m):
        '''
        Function accommodation
        Returns the number of accommodations
        :param n: total number of objects, natural number
        :param m: number of objects in the sample, natural number
        :return: number of accommodations, natural number
        '''
        if n > 0 and isinstance(n, int) and m > 0 and isinstance(m, int):
            return self.combination(n, m) * self.permutations(m)
        else: return -1



class FormulasTerver:
    '''
    Class FormulasTerver containing formulas of probability theory
    '''

    def __init__(self, formulasCombinatorics):
        '''
        Initial function
        :param formulasCombinatorics: instance of class FormulasCombinatorics
        '''
        self.formulasCombinatorics = formulasCombinatorics

# вероятность события (m - благоприятные, n - все)
    def probability(self, n, m):
        '''
        Function probability
        Returns the probability of an event
        :param n: total amount(all events), non-negative
        :param m: favorable events, non-negative
        :return: probability of an event, non-negative, less than or equal to 1
        '''
        return (1 if m > n else m/n) if m > 0 and n > 0 else -1

# Бернули
    def bernoulli(self, n, m, p):
        '''
        Function bernoulli
        Returns the probability that event A will occur exactly k times out of n
        :param n: number of independent tests, natural number
        :param m: required number of repetitions, natural number
        :param p: probability of occurrence of event A in each trial, non-negative, less than or equal to 1
        :return: probability that event A will occur exactly k times out of n, non-negative, less than or equal to 1
        '''
        if n > 0 and isinstance(n, int) and m > 0 and isinstance(m, int) and 0 <= p <= 1:
            return self.formulasCombinatorics.combination(n, m) * pow(p, m) * pow(1-p, n-m)
        else: return -1

# Пуассон
    def poisson(self, n, m, p):
        '''
        Function poisson
        Returns the probability that event A will occur exactly k times out of n
        n is large and the probability is less than 0.1
        :param n: number of independent tests, natural number
        :param m: required number of repetitions, natural number
        :param p: probability of occurrence of event A in each trial, non-negative, less than or equal to 1
        :return: probability that event A will occur exactly k times out of n, non-negative, less than or equal to 1
        '''
        if n > 0 and isinstance(n, int) and m > 0 and isinstance(m, int) and 0 <= p <= 1:
            return (pow(n*p, m) / fac(m)) * exp(-n*p)
        else: return -1


class Show:
    '''
    class Show
    '''
    def start(self):
        '''
        Function start
        Displays a possible use case, takes input and displays the result
        :return: none
        '''
        fc = FormulasCombinatorics()
        ft = FormulasTerver(fc)

        while 1:
             print('0 - выход\n'
                   '1 - посчитать кол-во перестановок\n'
                    '2 - посчитать кол-во сочетаний\n'
                    '3 - посчитать кол-во размещений\n'
                    '4 - посчитать вероятность события\n'
                    '5 - посчитать вероятность по формуле Бернули\n'
                    '6 - посчитать вероятность по формуле Пуассона')
             inpt = int(input('    ->'))
             if inpt == 0:
                 exit()
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