from Labs.Year3.Cryptography.Lab3.vigenere_cipher import VigenereCipher

def main():
    cipher = VigenereCipher()

    while True:
        print("\nVigenère Cipher Algorithm")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "3":
            print("Exiting program...")
            break

        if choice not in ["1", "2"]:
            print("Invalid choice. Please select 1, 2, or 3.")
            continue

        if choice == "1":
            prompt = f"Enter the text to encrypt: "
        else:
            prompt = f"Enter the text to decrypt: "

        text = cipher.validate_input(prompt)
        key = cipher.validate_input("Enter the key (minimum 7 characters): ")

        if choice == "1":
            result = cipher.encrypt(text, key)
        else:
            result = cipher.decrypt(text, key)

        if result.startswith("Error"):
            print(f"\n{result}")
        else:
            print(f"\nResult: {result}")


if __name__ == "__main__":
    main()
