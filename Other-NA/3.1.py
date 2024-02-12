def decimal_to_binary(n):
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

def binary_addition(num1, num2):
    carry = 0
    result = ''

    # make num1 and num2 the same length by adding leading zeros
    length = max(len(num1), len(num2))
    num1 = num1.zfill(length)
    num2 = num2.zfill(length)

    # iterate through digits from right to left
    for i in range(length-1, -1, -1):
        digit_sum = carry + int(num1[i]) + int(num2[i])
        if digit_sum == 3:
            carry = 1
            result = '1' + result
        elif digit_sum == 2:
            carry = 1
            result = '0' + result
        else:
            carry = 0
            result = str(digit_sum) + result

    # if there's still a carry left, add it to the leftmost digit
    if carry == 1:
        result = '1' + result

    return result

def binary_subtraction(num1, num2):
    # Make sure num1 is greater than or equal to num2
    if int(num1, 2) < int(num2, 2):
        num1, num2 = num2, num1

    # Pad num2 with leading zeros if necessary
    num2 = num2.zfill(len(num1))

    # Perform binary subtraction
    result = ""
    borrow = 0
    for i in range(len(num1)-1, -1, -1):
        if int(num1[i]) - borrow < int(num2[i]):
            result = "1" + result
            borrow = 1
        else:
            result = "0" + result
            borrow = 0

    # Remove any leading zeros
    result = result.lstrip("0")

    # Add a leading zero if the result is empty
    if result == "":
        result = "0"

    return result

def booth_algorithm(num1, num2):
    # convert the numbers to lists of digits
    num1_list = [int(x) for x in num1]
    num2_list = [int(x) for x in num2]

    # initialize the accumulator and the product register
    accumulator = [0] * (len(num1_list) + 1)
    product = num1_list + [0]

    # initialize the multiplier to the rightmost bit of num2
    multiplier = 0

    # iterate through the bits of num2 from right to left
    for i in range(len(num2_list)-1, -1, -1):
        # set the new multiplier to the current bit of num2
        new_multiplier = num2_list[i]

        # check if the new multiplier is different from the old multiplier
        if new_multiplier != multiplier:
            # calculate the correction factor based on the old multiplier and the bit to the right of it
            if multiplier == 1 and accumulator[-1] == 0:
                correction_factor = 1
                for j in range(len(accumulator)):
                    accumulator[j] = (accumulator[j] + correction_factor) % 2
                    correction_factor = (accumulator[j] + correction_factor) // 2
            elif multiplier == 0 and accumulator[-1] == 1:
                correction_factor = -1
                for j in range(len(accumulator)):
                    accumulator[j] = (accumulator[j] + correction_factor) % 2
                    correction_factor = (accumulator[j] + correction_factor) // 2

            # update the multiplier
            multiplier = new_multiplier

        # shift the product and the accumulator right by one bit
        accumulator.insert(0, product[-1])
        product.insert(0, 0)
        accumulator.pop()
        product.pop()

    # convert the accumulator back to a binary string
    result_str = ''.join(str(x) for x in accumulator)

    return result_str


def binary_division(num1, num2):
    # Convert binary numbers to lists of digits
    num1_list = [int(x) for x in num1]
    num2_list = [int(x) for x in num2]

    # Initialize quotient and remainder
    quotient = []
    remainder = num1_list

    # Loop until remainder is less than divisor
    while len(remainder) >= len(num2_list):
        # Calculate trial quotient
        trial_quotient = [0] * (len(remainder) - len(num2_list)) + num2_list
        for i in range(len(trial_quotient), len(remainder)):
            trial_quotient.append(0)

        # Subtract divisor times trial quotient from remainder
        for i in range(len(remainder)):
            remainder[i] -= trial_quotient[i]
            if remainder[i] < 0:
                remainder[i] += 2
                remainder[i+1] -= 1

        # Add trial quotient to quotient
        quotient.append(1)
        while len(quotient) < len(remainder):
            quotient.insert(0, 0)

    # Convert quotient and remainder back to decimal format
    quotient_decimal = 0
    power = len(quotient) - 1
    for digit in quotient:
        quotient_decimal += digit * (2 ** power)
        power -= 1

    remainder_decimal = 0
    power = len(remainder) - 1
    for digit in remainder:
        remainder_decimal += digit * (2 ** power)
        power -= 1

    return quotient_decimal, remainder_decimal



def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1
    for digit in binary:
        decimal += int(digit) * (2 ** power)
        power -= 1
    return decimal

op = input("Enter operation (+, -, *, /): ")
#num1 = decimal_to_binary(int(input("Enter first number: ")))
#num2 = decimal_to_binary(int(input("Enter second number: ")))

if op == '+':
    num1 = decimal_to_binary(int(input("Enter first number: ")))
    num2 = decimal_to_binary(int(input("Enter second number: ")))
    result = binary_to_decimal(binary_addition(num1,num2))
    print(result)
elif op == '-':
    num1 = decimal_to_binary(int(input("Enter first number: ")))
    num2 = decimal_to_binary(int(input("Enter second number: ")))
    result = binary_to_decimal(binary_subtraction(num1,num2))
    print(result)
elif op == '*':
    def main():
        print("Booth's Algorithm for multiplication")

        print("Input Multiplicand M: ", end="")
        m = int(input())
        if m < 0:
            m = TwoComp(("{0:0%db}" % 8).format(m))  # Calculate the two's complement number of m
        else:
            m = ("{0:0%db}" % 8).format(m)  # Convert to bits and assign directly

        print("Input Multiplier Q: ", end="")
        q = int(input())
        if q < 0:
            q = TwoComp(("{0:0%db}" % 8).format(q))
        else:
            q = ("{0:0%db}" % 8).format(q)

        a = '00000000'
        q0 = list('0')
        q = list(a + q)
        for k in range(8):  # the code will run 8 times acc to Booth's algorithm

            if (q[-1] + q0[0]) == '00':
                q0[0] = q[-1]
                q = list(RightShift("".join(q)))


            elif (q[-1] + q0[0]) == '01':
                q = (list(add("".join(q[:8]), m))[-8:] + q[8:])
                q0[0] = q[-1]
                q = list(RightShift("".join(q)))


            elif (q[-1] + q0[0]) == '10':
                q = (list(add("".join(q[:8]), TwoComp(m)))[-8:] + q[8:])
                q0[0] = q[-1]
                q = list(RightShift("".join(q)))


            elif (q[-1] + q0[0]) == '11':
                q0[0] = q[-1]
                q = list(RightShift("".join(q)))

        print()
        print('RESULT')

        if (q[0] == '1'):
            result = TwoComp("".join(q[1:]))
            print(result)
            result = str(int(result, 2))
            print("-" + result)

        else:
            result = ("".join(q[1:]))
            print(int(result, 2))


    def add(x, y):  # function to carry out binary addition and returns the result as a string
        maxlen = max(len(x), len(y))

        # Normalize lengths
        x = x.zfill(maxlen)
        y = y.zfill(maxlen)
        result = ''
        carry = 0
        for i in range(maxlen - 1, -1, -1):  # reverse order range, decreasing by 1 in every iteration
            r = carry
            r += 1 if x[i] == '1' else 0
            r += 1 if y[i] == '1' else 0
            result = ('1' if r % 2 == 1 else '0') + result
            carry = 0 if r < 2 else 1
        if carry != 0: result = '1' + result
        result.zfill(maxlen)
        return result[-16:]


    def TwoComp(n):  # function that returns the 2s complement of the binary input, both input and output are strings
        li = list(n)
        for i in range(len(li)):
            li[i] = "0" if li[i] == "1" else "1"
        return add("".join(li), "1")


    def RightShift(a):  # function to carry out right shift
        a = list(a)
        for i in range(len(a) - 1, 0, -1):
            a[i] = a[i - 1]
        return "".join(a)


    main()
#elif op == '/':
    #result, remainder = (binary_division(num1,num2))
    #print(f"Remainder is : {remainder},result is: {result}")

#print(result)

