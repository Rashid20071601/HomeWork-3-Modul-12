# Импорт библиотек
import unittest
from main import runner_and_tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        # Инициализация общего атрибута для хранения результатов
        cls.all_results = {}

    def setUp(self):
        # Создание объектов бегунов для использования в тестах
        self.Usain = runner_and_tournament.Runner('Усэйн', 10)
        self.Andrey = runner_and_tournament.Runner('Андрей', 9)
        self.Nick = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        # Вывод всех результатов после выполнения всех тестов
        for key, value in cls.all_results.items():
            print(key, list(value))

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_usain_nick(self):
        """Тест для турнира с Усэйном и Ником"""
        # Создание турнира с участниками и старт забега
        tournament = runner_and_tournament.Tournament(90, self.Usain, self.Nick)
        results = tournament.start()

        # Проверка, что последним финишировавшим является Ник
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == 'Ник')

        # Сохранение результатов турнира
        self.all_results['usain_nick'] = results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_andrey_nick(self):
        """Тест для турнира с Андреем и Ником"""
        # Создание турнира с участниками и старт забега
        tournament = runner_and_tournament.Tournament(90, self.Andrey, self.Nick)
        results = tournament.start()

        # Проверка, что последним финишировавшим является Ник
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == 'Ник')

        # Сохранение результатов турнира
        self.all_results['andrey_nick'] = results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_usain_andrey_nick(self):
        """Тест для турнира с Усэйном, Андреем и Ником"""
        # Создание турнира с участниками и старт забега
        tournament = runner_and_tournament.Tournament(90, self.Usain, self.Andrey, self.Nick)
        results = tournament.start()

        # Проверка, что последним финишировавшим является Ник
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == 'Ник')

        # Сохранение результатов турнира
        self.all_results['usain_andrey_nick'] = results
