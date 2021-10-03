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
    def __init__(self):
        self.i=1

    def start(self, inpt):
        '''
        Function start
        :param inpt: a string of 4 characters separated by a space
                    the first character is the choice of action:
                         1 - count the number of permutations
                         2 - count the number of combinations
                         3 - count the number of placements
                         4 - calculate the probability of an event
                         5 - calculate the probability using the Bernouli formula
                         6 - calculate the probability by Poisson's formula
                    second character - n
                    the third character is m, if there is no such character then "."
                    the fourth character is n, if there is no such character then "."
        :return: result, if the input is incorrect then -1
        '''

        fc = FormulasCombinatorics()
        ft = FormulasTerver(fc)
        inpt = inpt.split(' ')

        if inpt[0] == '0':
            exit()
        elif inpt[0] == '1':
            return fc.permutations(int(inpt[1]))
        elif inpt[0] == '2':
            return fc.combination(int(inpt[1]),int(inpt[2]))
        elif inpt[0] == '3':
            return fc.accommodation(int(inpt[1]), int(inpt[2]))
        elif inpt[0] == '4':
            return ft.probability(int(inpt[1]), int(inpt[2]))
        elif inpt[0] == '5':
            return ft.bernoulli(int(inpt[1]), int(inpt[2]), float(inpt[3]))
        elif inpt[0] == '6':
            return ft.poisson(int(inpt[1]), int(inpt[2]), float(inpt[3]))
        else:
            return -1
