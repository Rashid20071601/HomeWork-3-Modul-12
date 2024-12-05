import unittest
import test_tournament
import test_runner


runTS = unittest.TestSuite()

runTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_tournament.TournamentTest))
runTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner.RunnerTest))


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(runTS)