import random

class Grammar:
    def __init__(self, VN, VT, P, S):
        self.VN = VN # non-terminals
        self.VT = VT # terminals
        self.P = P # production rules
        self.S = S # start symbol

    def classifyChomskyHierarchy(self):
        def type0(lhs):
            for symbol in lhs:
                if symbol in {'S', 'B', 'D'}:
                    return 0
            return 9

        def type1(lhs, rhs):
            if lhs == 'S' and rhs == 'l':
                return 1
            if len(lhs) <= len(rhs):
                return 1

        def type2(length):
            if length == 1:
                return 2
            else:
                return 1

        def type3_LL(rhs, lhs):
            counter = sum(1 for symbol in rhs if symbol in {'S', 'B', 'D'})
            if counter == 0:
                return 3
            else:
                return 2

        def type3_RL(rhs):
            counter = sum(1 for symbol in rhs if symbol in {'S', 'B', 'D'})
            if counter == 1 and rhs[-1] not in {'S', 'B', 'D'}:
                return 3
            else:
                return 2

        for lhs, productions in self.P.items():
            for rhs in productions:
                min_type = type0(lhs)
                if min_type == 0:
                    min_type = type1(lhs, rhs)
                if min_type == 1:
                    min_type = type2(len(lhs))
                if min_type == 2:
                    if rhs[0] in {'S', 'B', 'D'}:
                        min_type = type3_LL(rhs, lhs)
                    elif rhs[0] in {'a', 'b', 'c'}:
                        min_type = type3_RL(rhs)

                if min_type in {0, 1, 2, 3}:
                    return "Type " + str(min_type) + ": according to your function"
        return "No type found"

# Grammar variant 11
VN = {'S', 'B', 'D'}
VT = {'a', 'b', 'c'}
P = {
    'S': ['aB', 'bB'],
    'B': ['bD', 'cB', 'aS'],
    'D': ['b', 'aD']
}
S = 'S'


# Create an instance of Grammar
grammar = Grammar(VN, VT, P, S)

grammar_type = grammar.classifyChomskyHierarchy()
print("Grammar type according to Chomsky hierarchy:", grammar_type)


