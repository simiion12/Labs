# CONSTANTS
DIGITS = '0123456789'
KEYWORDS = {'if', 'while', 'return'}

# Token types
TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'
TT_IDENTIFIER = 'IDENTIFIER'
TT_STRING = 'STRING'
TT_COMMA = 'COMMA'
TT_ASSIGN = 'ASSIGN'
TT_EQUAL = 'EQUAL'
TT_LESS = 'LESS'
TT_GREATER = 'GREATER'
TT_LESS_EQUAL = 'LESS_EQUAL'
TT_GREATER_EQUAL = 'GREATER_EQUAL'
TT_CHAR = 'CHAR'
TT_EOF = 'EOF'
TT_SPACE = 'SPACE'
TT_NEWLINE = 'NEWLINE'
TT_COLON = 'COLON'
TT_KEYWORD = 'KEYWORD'
TT_SEMICOLON = 'SEMICOLON'
TT_LBRACE = 'LEFT_BRACE'
TT_RBRACE = 'RIGHT_BRACE'


# TOKENS
class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'  # Returning token type and value if available
        return f'{self.type}'
