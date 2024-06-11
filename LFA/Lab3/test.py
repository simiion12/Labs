from lexer import run

# Sample input text to lex
input_text = """
int main() {
    // This is a comment
    int x = 10;
    float y = 20.0;
    if (x > y) {
        return x;
    } else {
        return y;
    }
}
"""

# Running the lexer on the input text
tokens = run("<stdin>", input_text)

# Printing out the tokens
for token in tokens:
    print(token)
