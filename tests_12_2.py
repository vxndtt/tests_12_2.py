import unittest
from pprint import pprint
from runner_and_tournament import *


class TournamentTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        pprint(cls.all_results)

    def test_run1(self):
        t1 = Tournament(90, (self.runner1, self.runner3))
        results = t1.start()
        TournamentTest.all_results.append(results)
        self.assertTrue(results[2] == 'Ник')

    def test_run2(self):
        t2 = Tournament(90, (self.runner2, self.runner3))
        results = t2.start()
        TournamentTest.all_results.append(results)
        self.assertTrue(results[2] == 'Ник')

    def test_run3(self):
        t3 = Tournament(90, (self.runner1, self.runner2, self.runner3))
        results = t3.start()
        TournamentTest.all_results.append(results)
        self.assertTrue(results[2] == 'Ник')


if __name__ == '__main__':
    unittest.main()
