#write functions here, don't add input('') statements here!
def get_day_of_week(day):
    days = {1: "Monday" , 2: "Tuesday" , 3: "Wednesday" , 4: "Thursday" , 5: "Friday" , 6: "Saturday" , 7: "Sunday"}
    return days.get(day, "Invalid Number")

def main():
    while True:
        user_input = input("Enter a number between (1-7) to receive the day of the week, or 'q' to quit. ")
        if user_input.lower() == 'q' :
            print("Goodbye")
            break
        try:
            day_number = int(user_input)
            print(get_day_of_week(day_number))
        except ValueError:
            print("Invalid Number, Enter a number between 1-7 to receive the day of the week, or 'q' to quit. ")






