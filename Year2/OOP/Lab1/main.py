class NarcissisticNumber:
    def __init__(self, number):
        self.number = number
        self.sum_of_powers = 0
        self.is_narcissistic = False

    def check(self):
        num_str = str(self.number)
        n = len(num_str)

        for digit_str in num_str:
            digit = int(digit_str)
            self.sum_of_powers += digit ** n

        if self.sum_of_powers == self.number:
            self.is_narcissistic = True

    def print_state(self):
        print(f"{self.number} is a narcissistic number: {self.is_narcissistic}")


if __name__ == "__main__":
    number = int(input("Choose a number to check if it's narcissistic: "))
    narcissistic_checker = NarcissisticNumber(number)
    narcissistic_checker.check()
    narcissistic_checker.print_state()

