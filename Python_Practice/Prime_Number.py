def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Continuous loop to check numbers
while True:
    number = int(input("Enter a number (or type -1 to exit): "))
    if number == -1:  # Exit condition
        print("Terminating the program. Goodbye!")
        break
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
