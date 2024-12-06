from lab5 import PKIManager


def print_menu():
    print("\nChoose an option:")
    print("1. Generate CA (Root Certificate Authority)")
    print("2. Generate User Certificate")
    print("3. Sign a File")
    print("4. Verify File Signature")
    print("5. Exit")


def run():
    pki = PKIManager()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                pki.generate_ca()

            elif choice == "2":
                username = input("Enter the username for the certificate: ")
                pki.generate_user_certificate(username)

            elif choice == "3":
                username = input("Enter the username for signing: ")
                file_path = input("Enter the file path to sign: ")
                pki.sign_file(username, file_path)

            elif choice == "4":
                username = input("Enter the username for verification: ")
                file_path = input("Enter the file path to verify: ")
                signature_path = input("Enter the signature file path: ")
                pki.verify_signature(username, file_path, signature_path)

            elif choice == "5":
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please select a valid option.")

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    run()