from Lab2 import FiniteAutomaton, FiniteAutomatonToRegularGrammar


# Using the provided FA
FA = FiniteAutomaton(
    Q={'q0', 'q1', 'q2', 'q3'},
    Sigma={'a', 'b', 'c'},
    Delta={
    ('q0', 'a'): {'q1'},
    ('q1', 'b'): {'q1', 'q2'},
    ('q2', 'c'): {'q3'},
    ('q3', 'a'): {'q1'},
    ('q0', 'b'): {'q2'}
        },
    q0={'q0'},
    F={'q3'}
)  # Added the final states set


DFA = FiniteAutomaton(
    Q={'q0', 'q1'},                    # Set of states
    Sigma={'0', '1'},                  # Alphabet
    Delta={('q0', '0'): {'q0'},        # Transition function
           ('q0', '1'): {'q1'},
           ('q1', '0'): {'q0'},
           ('q1', '1'): {'q1'}},
    q0={'q0'},                        # Initial state
    F={'q1'}                          # Set of final states
)

# Convert the provided FA to a regular grammar
regular_grammar_converter = FiniteAutomatonToRegularGrammar(FA)
regular_grammar = regular_grammar_converter.toRegularGrammar()
print("Regular grammar from the provided FA:")
print("VN:", regular_grammar.VN)
print("VT:", regular_grammar.VT)
for lhs, productions in regular_grammar.P.items():
    for rhs in productions:
        print(lhs, "->", rhs)
print("S:", regular_grammar.S)
print("------------------------------------------------------")

# Determine whether the provided FA is deterministic or not
is_deterministic = FiniteAutomaton.is_deterministic(FA)
if is_deterministic:
    print("The provided FA is deterministic.")
else:
    print("The provided FA is non-deterministic.")


