import unittest
from cityGame import BackGame


class CheckAnswerTest(unittest.TestCase):

# все правильно
    def test1(self):
        bg = BackGame()
        result = bg.checkAnsw("Москва", "Астрахань")
        self.assertEqual(result, 1)

# название города 2 некорректно, но последняя и первая буквы совпадают
    def test2(self):
        bg = BackGame()
        result = bg.checkAnsw("Амстердам", "Мск")
        self.assertEqual(result, 0)

# последняя буква города 1 несовпадает с первой буквой города 2, но название города 2 корректно
    def test3(self):
        bg = BackGame()
        result = bg.checkAnsw("Амстердам", "Екатеринбург")
        self.assertEqual(result, 0)

# последняя и первая буквы городов не совпадают, название города 2 несуществует
    def test4(self):
        bg = BackGame()
        result = bg.checkAnsw("Амстердам", "Екб")
        self.assertEqual(result, 0)