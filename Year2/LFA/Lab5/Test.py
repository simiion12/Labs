from Lab5 import Grammar
import unittest

class TestLab5(unittest.TestCase):
    def setUp(self):
        self.grammar = Grammar()
        self.P1, self.P2, self.P3, self.P4, self.P5 = self.grammar.ReturnProductions()

    def test_remove_epsilon(self):
        result = {'S': ['B', 'dB', 'AB'], 'A': ['dS', 'd', 'aAaAb', 'aab'], 'B': ['a', 'aS', 'd', 'dS', 'aAaAb', 'aab'], 'D': ['Aba', 'ba']}
        for key in self.P1.keys():
            self.P1[key].sort()
            result[key].sort()
        self.assertEqual(self.P1, result)

    def test_eliminate_unit_prod(self):
        result = {'S': ['dB', 'AB', 'a', 'aS', 'd', 'dS', 'aAaAb', 'aab'], 'A': ['d', 'dS', 'aAaAb', 'aab'], 'B': ['a', 'aS', 'd', 'dS', 'aAaAb', 'aab'], 'D': ['Aba', 'ba']}
        self.assertEqual(self.P2, result)

    def test_eliminate_inaccesible(self):
        result = {'S': ['dB', 'AB', 'a', 'aS', 'd', 'dS', 'aAaAb', 'aab'], 'A': ['d', 'dS', 'aAaAb', 'aab'], 'B': ['a', 'aS', 'd', 'dS', 'aAaAb', 'aab']}

        self.assertEqual(self.P3, result)

    def test_remove_unprod(self):
        result = {'S': ['dB', 'AB', 'a', 'aS', 'd', 'dS', 'aAaAb', 'aab'], 'A': ['d', 'dS', 'aAaAb', 'aab'], 'B': ['a', 'aS', 'd', 'dS', 'aAaAb', 'aab']}

        self.assertEqual(self.P4, result)

    def test_transform_to_cnf(self):
        result = {'S': ['CD', 'AB', 'a', 'EF', 'd', 'CF', 'GH', 'EI'], 'A': ['d', 'CF', 'GH', 'EI'], 'B': ['a', 'EF', 'd', 'CF', 'GH', 'EI'], 'C': ['d'], 'D': ['B'], 'E': ['a'], 'F': ['S'], 'G': ['aA'], 'H': ['aAb'], 'I': ['ab']}

        self.assertEqual(self.P5, result)


if __name__ == '__main__':
    #unittest.main()

    print(TestLab5.P1)