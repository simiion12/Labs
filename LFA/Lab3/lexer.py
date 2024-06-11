import re  # Importing regular expression library
from my_token import *  # Importing everything from my_token.py

# POSITION
class Position:
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx # Index
        self.ln = ln  # Line number
        self.col = col # Column number
        self.fn = fn  # File name
        self.ftxt = ftxt  # Full text of the file

    # Moving to the next character
    def advance(self, current_char):
        self.idx += 1  # Moving to next character
        self.col += 1  # Moving to next column

        if current_char == '\n':
            self.ln += 1  # Moving to next line
            self.col = 0  # Reset column number

        return self

    # Copying the current position
    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)

# LEXER
class Lexer:
    def __init__(self, fn, text):
        self.fn = fn # File name
        self.text = text  # Input text
        self.pos = Position(-1, 0, -1, fn, text)  # Starting position
        self.current_char = None  # Current character
        self.advance()  # Move to the first character

    def advance(self):
        self.pos.advance(self.current_char)  # Move to the next position
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None  # Update current character

    # Peeks at the next character.
    def peek(self):
        peek_pos = self.pos.idx + 1
        if peek_pos < len(self.text):
            return self.text[peek_pos]
        return None

    # Lexing the input text
    def make_tokens(self):
        tokens = []

        while self.current_char is not None:
            if self.current_char in ' \t':
                self.advance()
            elif re.match(r'\d', self.current_char):
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                # Peek at the next character to determine if this is the start of a comment
                if self.peek() == '/' or self.peek() == '*':
                    self.skip_comment()
                else:
                    tokens.append(Token(TT_DIV))
                    self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.advance()
            elif self.current_char == '{':
                tokens.append(Token(TT_LBRACE))
                self.advance()
            elif self.current_char == '}':
                tokens.append(Token(TT_RBRACE))
                self.advance()
            elif self.current_char == ';':
                tokens.append(Token(TT_SEMICOLON))
                self.advance()
            elif self.current_char == ',':
                tokens.append(Token(TT_COMMA))
                self.advance()
            elif self.current_char == '=':
                tokens.append(Token(TT_ASSIGN))
                self.advance()
            elif self.current_char == '"':
                tokens.append(self.make_string())
            elif self.current_char == '\n':
                tokens.append(Token(TT_NEWLINE))
                self.advance()
            elif re.match(r'[a-zA-Z_]', self.current_char):
                tokens.append(self.make_identifier())
            else:
                self.advance()

        tokens.append(Token(TT_EOF))  # Adding end of file token
        return tokens

    # Making a number token
    def make_number(self):
        num_str = ''
        while self.current_char is not None and re.match(r'\d|\.', self.current_char):
            num_str += self.current_char
            self.advance()

        if '.' in num_str:
            return Token(TT_FLOAT, float(num_str))
        else:
            return Token(TT_INT, int(num_str))

    def make_string(self):
        string = ''
        self.advance()
        while self.current_char is not None and self.current_char != '"':
            string += self.current_char
            self.advance()
        self.advance()  # Closing quote
        return Token(TT_STRING, string)

   # Making an identifier token
    def make_identifier(self):
        id_str = ''
        while self.current_char is not None and re.match(r'[a-zA-Z0-9_]', self.current_char):
            id_str += self.current_char
            self.advance()

        if id_str in KEYWORDS:
            return Token(TT_KEYWORD, id_str)
        return Token(TT_IDENTIFIER, id_str)

    # Skipping comments
    def skip_comment(self):
        if self.current_char == '/':
            self.advance()
            if self.current_char == '/':
                # Single-line comment, skip until the end of line
                while self.current_char and self.current_char != '\n':
                    self.advance()
                self.advance()  # Move past the newline character
            elif self.current_char == '*':
                # Multi-line comment, skip until '*/'
                depth = 1
                self.advance()  # Move past the '*' character
                while depth > 0:
                    if self.current_char == '*' and self.peek() == '/':
                        depth -= 1
                        self.advance()
                        self.advance()  # Move past the '*' and '/' characters
                    elif self.current_char == '\n':
                        self.advance()  # Move past the newline character
                    elif self.current_char:
                        self.advance()  # Move past other characters inside comments
                    else:
                        raise Exception("Unterminated multi-line comment")
            else:
                # This is not a comment, rewind to the previous character
                self.pos.advance(self.current_char)

# Running the lexer
def run(fn, text):
    lexer = Lexer(fn, text)
    tokens = lexer.make_tokens()
    return tokens
