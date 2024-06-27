def get_person_category(age):
    if age < 0 or age > 125:
        return "Invalid number"
    elif age <= 1:
        return "infant"
    elif age < 13:
        return "child"
    elif age < 20:
        return "teenager"
    else:
        return "adult"
    
def main():
    while True:
        user_input = input("Enter a person's age or 'q' to quit: ")
        if user_input.lower() == 'q' :
            print("Goodbye")
            break
        try:
            age = int(user_input)
            print(get_person_category(age))
        except ValueError:
            print("Invalid input. PLease enter a valid age or 'q' to quit. ")

            
