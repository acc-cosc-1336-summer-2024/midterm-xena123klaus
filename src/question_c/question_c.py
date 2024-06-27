def is_prime(z):
    if z <= 1:
        return False
    if z == 2:
        return True
    if z % 2 == 0:
        return False
    for i in range(3, int(z**0.5)+1, 2):
        if z % i == 0:
            return False
    return True

def main():
    while True:
        user_input = input("Enter a number to check if it is prime or 'q' to quit: ")
        if user_input.lower() == 'q':
            print("Goodbye")
            break
        try:
            number = int(user_input)
            if is_prime(number):
                print(number, "Is a prime number")
            else:
                print(number, "Is not a prime number")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit: ")

    
