class VigenereCipher:
    def __init__(self):
        self.alphabet = {
            'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,
            'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
            'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17,
            'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
            'Y': 24, 'Z': 25
        }
        self.reverse_alphabet = {v: k for k, v in self.alphabet.items()}

    def validate_input(self, prompt):
        """Validate that input contains only allowed characters."""
        valid_chars = self.alphabet.keys()
        while True:
            text = input(prompt).upper().replace(" ", "")
            if all(char in valid_chars for char in text):
                return text
            else:
                print("Invalid input. Use only letters A-Z.")

    def validate_key(self, key):
        """Validate the key length and characters."""
        while True:
            try:
                key = input("Enter the key (minimum 7 characters): ")
                if len(key) < 7:
                    print("Key must be at least 7 characters long.")
                elif not self.validate_input(key):
                    print("Key contains invalid characters.")
                else:
                    return key
            except ValueError:
                print("Invalid input. Please enter again a valid key.")

    def encrypt(self, plaintext, key):
        """Encrypt the plaintext using Vigenère cipher."""

        plaintext = self.prepare_text(plaintext)
        key = self.prepare_text(key)

        ciphertext = ""
        key_length = len(key)

        for i in range(len(plaintext)):
            p_char = plaintext[i]
            k_char = key[i % key_length]

            # Get numerical values
            p_val = self.alphabet[p_char]
            k_val = self.alphabet[k_char]

            # Apply Vigenère formula: c_i = (p_i + k_i) mod 26
            c_val = (p_val + k_val) % 26

            # Convert back to letter
            ciphertext += self.reverse_alphabet[c_val]

        return ciphertext

    def decrypt(self, ciphertext, key):
        """Decrypt the ciphertext using Vigenère cipher."""

        ciphertext = self.prepare_text(ciphertext)
        key = self.prepare_text(key)

        plaintext = ""
        key_length = len(key)

        for i in range(len(ciphertext)):
            c_char = ciphertext[i]
            k_char = key[i % key_length]

            # Get numerical values
            c_val = self.alphabet[c_char]
            k_val = self.alphabet[k_char]

            # Apply Vigenère decryption formula: p_i = (c_i - k_i) mod 26
            p_val = (c_val - k_val) % 26

            # Convert back to letter
            plaintext += self.reverse_alphabet[p_val]

        return plaintext

    @staticmethod
    def prepare_text(text):
        """Remove spaces and convert to uppercase."""
        return ''.join(char.upper() for char in text if not char.isspace())
