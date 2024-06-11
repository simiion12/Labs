class Grammar:
    def __init__(self, VN, VT, P, S):
        self.VN = VN  # Non-terminals
        self.VT = VT  # Terminals
        self.P = P    # Production rules
        self.S = S    # Start symbol

class FiniteAutomaton:
    def __init__(self, Q, Sigma, Delta, q0, F):
        self.Q = Q        # Set of states
        self.Sigma = Sigma  # Alphabet
        self.Delta = Delta  # Transition function
        self.q0 = q0        # Initial state
        self.F = F          # Set of final states

    def is_deterministic(self):
        for state in self.Q:
            for symbol in self.Sigma:
                if len(self.Delta.get((state, symbol), [])) > 1:
                    return False
        return True


class FiniteAutomatonToRegularGrammar:
    def __init__(self, fa):
        self.fa = fa

    def toRegularGrammar(self):
        VN = self.fa.Q  # Non-terminals are the states of the FA
        VT = self.fa.Sigma  # Terminals are the alphabet of the FA
        P = {}  # Production rules

        for state, symbol in self.fa.Delta:
            next_states = self.fa.Delta[(state, symbol)]
            P[(state, symbol)] = P.get((state, symbol), []) + list(next_states)

        S = self.fa.q0  # Start symbol is the initial state of the FA
        return Grammar(VN, VT, P, S)


"""
for state in self.Q:: This loop iterates over each state in the set of states Q of the finite automaton.

for symbol in self.Sigma:: Within the outer loop, another loop iterates over each symbol in the alphabet Sigma of the finite automaton.

if len(self.Delta.get((state, symbol), [])) > 1:: Within the nested loops, it checks the length of the set of states that the finite automaton transitions to from the current state state on the input symbol symbol. Here, self.Delta.get((state, symbol), []) returns the set of next states for the transition from state on symbol. If the length of this set is greater than 1, it means that there are multiple possible transitions from state on symbol, violating the deterministic property.

If the condition in the if statement is met at any point during the nested loops, return False is executed, indicating that the automaton is not deterministic.

If the condition is never met, i.e., there is no state that has more than one transition on any input symbol, return True is executed at the end of the method, indicating that the automaton is deterministic.
"""