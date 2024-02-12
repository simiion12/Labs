import sys
from collections import deque


class BigNumber:
    def init(self, number):
        self.number = deque(map(int, str(number)))

    def str(self):
        return ''.join(map(str, self.number))

    def len(self):
        return len(self.number)


def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        binary = str(remainder) + binary
    return binary


def binary_to_decimal(binary):
    decimal = 0
    for i, digit in enumerate(reversed(binary)):
        decimal += int(digit) * (2 ** i)
    return decimal


def add_binary(bin1, bin2):
    bin1_decimal = binary_to_decimal(bin1)
    bin2_decimal = binary_to_decimal(bin2)
    sum_decimal = bin1_decimal + bin2_decimal
    return decimal_to_binary(sum_decimal)


def subtract_binary(bin1, bin2):
    bin1_decimal = binary_to_decimal(bin1)
    bin2_decimal = binary_to_decimal(bin2)
    difference_decimal = bin1_decimal - bin2_decimal
    return decimal_to_binary(difference_decimal)


def multiply_binary(bin1, bin2):
    bin1_decimal = binary_to_decimal(bin1)
    bin2_decimal = binary_to_decimal(bin2)
    product_decimal = bin1_decimal * bin2_decimal
    return decimal_to_binary(product_decimal)


def divide_binary(bin1, bin2):
    bin1_decimal = binary_to_decimal(bin1)
    bin2_decimal = binary_to_decimal(bin2)
    if bin2_decimal == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    quotient_decimal = bin1_decimal // bin2_decimal
    return decimal_to_binary(quotient_decimal)


def calculate_absolute_error(approx_value, true_value):
    return abs(true_value - approx_value)


def calculate_relative_error(approx_value, true_value):
    return abs((true_value - approx_value) / true_value)


def main():
    while True:
        print("\nChoose an operation:")
        print("1. Convert decimal to binary")
        print("2. Convert binary to decimal")
        print("3. Add binary numbers")
        print("4. Subtract binary numbers")
        print("5. Multiply binary numbers")
        print("6. Divide binary numbers")
        print("7. Calculate absolute and relative error")
        print("8. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            decimal = int(input("Enter decimal number: "))
            print("Binary representation:", decimal_to_binary(decimal))
        elif choice == 2:
            binary = input("Enter binary number: ")
            print("Decimal representation:", binary_to_decimal(binary))
        elif choice == 3:
            bin1 = input("Enter first binary number: ")
            bin2 = input("Enter second binary number: ")
            print("Sum:", add_binary(bin1, bin2))
        elif choice == 4:
            bin1 = input("Enter first binary number: ")
            bin2 = input("Enter second binary number: ")
            print("Difference:", subtract_binary(bin1, bin2))
        elif choice == 5:
            bin1 = input("Enter first binary number: ")
            bin2 = input("Enter second binary number: ")
            print("Product:", multiply_binary(bin1, bin2))
        elif choice == 6:
            bin1 = input("Enter first binary number: ")
            bin2 = input("Enter second binary number: ")
            try:
                print("Quotient:", divide_binary(bin1, bin2))
            except ZeroDivisionError as e:
                print(e)
        elif choice == 7:
            approx_value = float(input("Enter the approximate value: "))
            true_value = float(input("Enter the true value: "))
            abs_error = calculate_absolute_error(approx_value, true_value)
            rel_error = calculate_relative_error(approx_value, true_value)
            print("Absolute error:", abs_error)
            print("Relative error:", rel_error)
        elif choice == 8:
            print("Exiting the program.")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()