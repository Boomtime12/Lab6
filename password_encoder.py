# Ryan Demolina

def main():
    while True:
        print("Menu")
        print("-" * 13)
        print("1. Encode \n2. Decode\n3. Quit")
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!")
        elif user_input == 2:
            pass
        elif user_input == 3:
            break


def encode(password):
    new_pass = ""
    for char in password:
        new_pass += str((int(char) + 3) % 10)
    return new_pass


if __name__ == "__main__":
    main()
