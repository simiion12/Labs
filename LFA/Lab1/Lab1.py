import random
class Grammar:
    def __init__(self, VN, VT, P, S):
        self.VN = VN # non terinals
        self.VT = VT # terminals
        self.P = P # production rules
        self.S = S # strat symbol

    def generateValidStrings(self, count):
        def generateFromSymbol(symbol):
            if symbol in self.VT:
                return symbol
            else:
                production = random.choice(self.P[symbol])
                return ''.join(generateFromSymbol(s) for s in production)

        valid_strings = []
        for _ in range(count):
            valid_strings.append(generateFromSymbol(self.S))
        return valid_strings

    def toFiniteAutomaton(self):
        Q = self.VN.union({'X'})  # States of the FA are the non-terminals of the grammar plus an additional state X
        Sigma = self.VT  # Alphabet of the FA is the set of terminals of the grammar
        Delta = {}  # Transition function
        q0 = {self.S}  # Initial state is the start symbol of the grammar
        F = {'X'}  # Set of final states

        # Initialize Delta with empty sets for all state-symbol pairs
        for state in Q:
            for symbol in Sigma:
                Delta[(state, symbol)] = set()

        # Construct transition function Delta
        for non_terminal, productions in self.P.items():
            for production in productions:
                # In this case, it adds a transition to state 'X' in the transition function Delta.
                if len(production) == 1 and production[0] in self.VT:
                    Delta[(non_terminal, production[0])].add('X')
                # In this case, it adds a transition to the second symbol in the production.
                elif len(production) == 2 and production[0] in self.VT:
                    Delta[(non_terminal, production[0])].add(production[1])
                # In this case, it adds a transition to the non-terminal symbol itself.
                elif len(production) == 1 and production[0] in self.VN:
                    Delta[(non_terminal, '')].add(production[0])  # it signifies a transition from a non-terminal to an empty string
                    F.add(production[0])  # Production is a final state

        return FiniteAutomaton(Q, Sigma, Delta, q0, F)


class FiniteAutomaton:
    def __init__(self, Q, Sigma, Delta, q0, F):
        self.Q = Q  # Set of states
        self.Sigma = Sigma  # Alphabet
        self.Delta = Delta  # Transition function
        self.q0 = q0  # Initial state
        self.F = F  # Set of final states

    def stringBelongToLanguage(self, w):
        currentStates = self.q0
        for letter in w:
            # nextStates is initialized as an empty set
            nextStates = set()
            for state in currentStates:
                # If there is a transition defined for the current state-symbol pair in Delta,
                # the next states are updated with the set of possible next states.
                if (state, letter) in self.Delta:
                    nextStates.update(self.Delta[(state, letter)])
            currentStates = nextStates
        #  returns True if any of the currentStates are also final states (F)
        return any(state in self.F for state in currentStates)


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

# Generate 5 valid strings
valid_strings = grammar.generateValidStrings(5)
print("Generated strings:")
for s in valid_strings:
    print(s)

print("-------------------------------------------------------------")

# Test Finite Automaton functionality
finiteAutomaton = grammar.toFiniteAutomaton()
print(finiteAutomaton.Q)
print(finiteAutomaton.Sigma)
print(finiteAutomaton.Delta)
for state, symbol in finiteAutomaton.Delta:
    print(state, symbol, finiteAutomaton.Delta[(state, symbol)])
print(finiteAutomaton.F)
listOfStrings = ["bbb", "ababab", "acaaaabb", "ababababab", "abb"]
for word in listOfStrings:
    print(f'{word} can be obtained via the state transition: {finiteAutomaton.stringBelongToLanguage(word)}')



"""
# Define the finite automaton (FA)
FA = FiniteAutomaton(
    Q={'B', 'X', 'D', 'S'},          # Set of states
    Sigma={'a', 'b', 'c'},           # Alphabet
    Delta={                           # Transition function
        ('B', 'a'): {'S'},
        ('B', 'b'): {'D'},
        ('B', 'c'): {'B'},
        ('X', 'a'): set(),
        ('X', 'b'): set(),
        ('X', 'c'): set(),
        ('D', 'a'): {'D'},
        ('D', 'b'): {'X'},
        ('D', 'c'): set(),
        ('S', 'a'): {'B'},
        ('S', 'b'): {'B'},
        ('S', 'c'): set()
    },
    q0={'B'},                        # Initial state
    F={'X'}                          # Set of final states
)
"""