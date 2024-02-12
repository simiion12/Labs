def m7(x):
    T1 = 1
    T2 = x
    T3 = 2*x**2 - 1
    T4 = 4*x**3 - 3*x
    T5 = 8*x**4 - 8*x**2 + 1
    T6 = 16*x**5 - 20*x**3 + 5*x
    T7 = 32*x**6 - 48*x**4 + 18*x**2 - 1

    return 0.7373*T1 + 0.3732*T2 - 0.1048*T3 - 0.2916*T4 - 0.0833*T5 + 0.0446*T6 + 0.0094*T7

# Get user input for x value
x = float(input("Enter a value for x: "))

# Compute m7(x)
result = m7(x)

# Print the result
print(f"The approximation of m7({x}) is {result}")
