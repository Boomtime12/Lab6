# Ryan Demolina

def main():
    while True:
        # Print menu
        print("Menu")
        print("-" * 13)
        print("1. Encode \n2. Decode\n3. Quit")
        user_input = int(input("Please enter an option: "))

        # Takes a password and encodes it
        if user_input == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!")

        # Decoded the encoded password
        elif user_input == 2:
            decoded = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}.")

        # Exit the program
        elif user_input == 3:
            break

        else:
            print("Invalid input!")


# Encodes the given password
def encode(password):
    new_pass = ""
    # Goes through each number in the password and converts it to encoded number
    for char in password:
        new_pass += str((int(char) + 3) % 10)
    return new_pass

def decode(password):
    decoded = ""
    i = 0
    while i < len(password):
        if password[i] == "9":
            decoded += "6"
        if password[i] == "8":
            decoded += "5"
        if password[i] == "7":
            decoded += "4"
        if password[i] == "6":
            decoded += "3"
        if password[i] == "5":
            decoded += "2"
        if password[i] == "4":
            decoded += "1"
        if password[i] == "3":
            decoded += "0"
        i += 1
    return decoded

if __name__ == "__main__":
    main()
