from unittest import TestCase


class Runner:

    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name




class Runner_Test(TestCase):

    def test_walk(self):
        tester = Runner("tester")
        for _ in range(10):
            tester.walk()
        self.assertEqual(tester.distance , 50)

    def test_run(self):
        tester = Runner("tester")
        for _ in range(10):
            tester.run()
        self.assertEqual(tester.distance, 100)

    def test_challenge(self):
        tester_1 = Runner("tester_1")
        tester_2 = Runner("tester_2")
        for _ in range(10):
            tester_1.walk()
            tester_2.run()
        self.assertNotEqual(tester_1.distance, tester_2.distance)