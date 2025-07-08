

def show_menu():
    print("\n DO YOUR CALCULATION")
    print("Please choose an operation:")
    print("1  Addition")
    print("2  Subtraction")
    print("3  Multiplication")
    print("4  Division")
    print("5  Exit")

def get_inputs():
    try:
        num1 = float(input(" Enter the first number: "))
        num2 = float(input(" Enter the second number: "))
        return num1, num2
    except ValueError:
        print("  That wasn't a number. Try again.")
        return None, None

def calculator():
    while True:
        show_menu()
        choice = input("➡️ Select an option (1-5): ")

        if choice in ['1', '2', '3', '4']:
            num1, num2 = get_inputs()
            if num1 is None or num2 is None:
                continue

            if choice == '1':
                print(f" {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f" {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f" {num1} × {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f" {num1} ÷ {num2} = {num1 / num2}")
                else:
                    print(" You can't divide by zero!")

        elif choice == '5':
            print(" shut down")
            break
        else:
            print(" That's an invalid choice. Please pick a number from 1 to 5.")

if __name__ == "__main__":
    calculator()
