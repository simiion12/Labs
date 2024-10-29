# Vigenère Cipher Implementation

This project implements the Vigenère cipher, a polyalphabetic substitution cipher that improves upon monoalphabetic ciphers by using multiple substitution alphabets. Unlike the Caesar cipher which uses a single shift value, the Vigenère cipher uses a keyword to determine multiple shift values, making it more resistant to frequency analysis attacks.

## Description

The Vigenère cipher works by using a series of interwoven Caesar ciphers based on the letters of a keyword. Each letter in the keyword determines how much to shift each letter in the plaintext.

### Mathematical Model

The cipher uses the following mathematical formulas:

- Encryption: `c_i = (m_i + k_i) mod 26`
- Decryption: `m_i = (c_i - k_i) mod 26`

Where:
- `c_i` is the ith letter of the ciphertext
- `m_i` is the ith letter of the plaintext
- `k_i` is the ith letter of the key (repeated as needed)

## Features

- Supports the English alphabet (A-Z)
- Input validation for both text and key
- Minimum key length requirement (7 characters)
- Automatic handling of spaces and case conversion
- Both encryption and decryption functionality
- User-friendly command-line interface

## Requirements

- Python 3.x

## Project Structure

```
├── vigenere_cipher.py    # Main cipher implementation class
└── main.py              # Command-line interface
```

## Usage

1. Run the program:
```bash
python main.py
```

2. Choose an operation:
   - 1: Encrypt
   - 2: Decrypt
   - 3: Exit

3. Enter your text and key when prompted
   - The key must be at least 7 characters long
   - Only letters A-Z are allowed (case insensitive)
   - Spaces are automatically removed

### Example

```
Vigenère Cipher Algorithm
1. Encrypt
2. Decrypt
3. Exit

Choose an option (1-3): 1
Enter the text to encrypt: HELLO WORLD
Enter the key (minimum 7 characters): KEYWORD
Result: RIJVS UYVJN
```

## Input Restrictions

- Only letters A-Z are allowed (case insensitive)
- Special characters, numbers, and non-English letters are not permitted
- The key must be at least 7 characters long
- Spaces in input text are automatically removed
- All input is converted to uppercase before processing

## Implementation Details

The implementation consists of two main files:

### vigenere_cipher.py
- Contains the `VigenereCipher` class
- Handles the core encryption/decryption logic
- Manages input validation and text preparation
- Implements the mathematical model of the cipher

### main.py
- Provides the command-line interface
- Handles user interaction and input/output
- Manages the program flow and operation selection

## Error Handling

The program includes comprehensive error handling for:
- Invalid character inputs
- Insufficient key length
- Invalid menu choices

## Limitations

- Only supports basic English alphabet (A-Z)
- Does not preserve spacing or punctuation in the output
- Does not support special characters or numbers

## Security Note

While historically significant, the Vigenère cipher is not considered cryptographically secure by modern standards. It should not be used for securing sensitive information in real-world applications.