import random
def mastermind():
    #code = [random.choice([col1, col2, col3, col4, col5, col6]) for i in range(1)]
    code = [random.randint(1,6) for i in range(4)]
    code = ("".join(map(str, code)))
    print(code)
    guesses = 10
    print("You have", guesses, "guesses left.")
    guess = (input("Guess the number: "))
    if guess == code:
        print("You win!")
        return
    while guess != code:
        k = 0
        w = 0
        if guess != code:
            guesses -= 1
            for i in range(len(guess)):
                if guess[i] == code[i]:
                    k += 1
                    guess = guess.replace(guess[i], "i")
                elif guess[i] in code:
                    w += 1
            print("White", w, "Red", k)
            #print(code, guess)
            print("You have", guesses, "guesses left.")
            guess = input("Guess the number: ")
            if guess == code:
                print("You win!")
                break
            elif guesses == 0:
                print("You lose!")
                break
def mastermind2():
    #code = [random.choice([col1, col2, col3, col4, col5, col6]) for i in range(1)]
    code = input("Enter a 4 digit code: ")
    code = ("".join(map(str, code)))
    print(code)
    guesses = 10
    print("You have", guesses, "guesses left.")
    guess = (input("Guess the number: "))
    if guess == code:
        print("You win!")
        return
    while guess != code:
        k = 0
        w = 0
        if guess != code:
            guesses -= 1
            for i in range(len(guess)):
                if guess[i] == code[i]:
                    k += 1
                    guess = guess.replace(guess[i], "i")
                elif guess[i] in code:
                    w += 1
            print("White", w, "Red", k)
            #print(code, guess)
            print("You have", guesses, "guesses left.")
            guess = input("Guess the number: ")
            if guess == code:
                print("You win!")
                break
            elif guesses == 0:
                print("You lose!")
                break
print("Choose which game you want to play:")
print("Choose 1 for mastermind with computer and 2 for mastermind with human:")
game = int(input())
print("1=Red, 2=Yellow, 3=Indigo, 4=White, 5=Green, 6=Black")
if game == 1:
    mastermind()
elif game == 2:
    mastermind2()

