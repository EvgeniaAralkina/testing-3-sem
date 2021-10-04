import codecs

class BackGame:

    def __init__(self):
        self.cities = [line.rstrip('\n').rstrip('\r') for line in codecs.open("city.txt", encoding='utf-8')]
        self.named = ["Москва"]

    def checkAnsw(self, city1, city2):
        if city1[-1] == 'ь' or city1[-1] == 'ъ' or city1[-1] == 'ы':
            city1 = city1[:-1]
        if city1[-1] == city2.lower()[0] and self.cities.count(city2) and self.named.count(city2) == 0:
            self.named.append(city2)
            return 1
        else:
            return 0


def main():
    bg = BackGame()
    names = []
    names.append(input("Введите имя 1-го игрока: "))
    names.append(input("Введите имя 2-го игрока: "))
    city0 = "Москва"
    n = 0
    print("Игра начинаетя!\nМосква")
    while 1:
        city1 = input('{name}, введите название города: '.format(name=names[n % 2]))
        if bg.checkAnsw(city0, city1) == 0:
            print("Такого города нет!")
            print('игрок {name}, выиграл(а)!'.format(name=names[n % 1]))
            return 0
        city0 = city1
        n+=1

main()