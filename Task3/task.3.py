import random
import string

def generate_password(length):
    if length < 4:
        print(" Password length must be at least 4 characters .")
        return None


    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]


    all_chars = lowercase + uppercase + digits + symbols
    remaining_length = length - 4
    password += random.choices(all_chars, k=remaining_length)


    random.shuffle(password)

    return ''.join(password)

def main():
    print(" Generate password ")

    try:
        length = int(input(" Enter the desired password length (minimum 4): "))
        password = generate_password(length)
        if password:
            print(f"\n Your secure password is:  {password}")
    except ValueError:
        print(" Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
