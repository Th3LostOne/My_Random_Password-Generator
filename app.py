import sys
import random
import string

def generate_password(words):
    # Concatenate the input words
    combined_words = ''.join(words)

    # Add some random characters to the combined words
    symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    random_symbols = ''.join(random.choice(symbols) for _ in range(3))

    # Generate a random password by shuffling the characters
    password = list(combined_words + random_symbols)
    random.shuffle(password)
    password = ''.join(password)

    return password

def main():
    print("Welcome to the Password Generator!")

    # Get user input for words
    if len(sys.argv) > 1:
        user_words = sys.argv[1:]
    else:
        user_words = input("Enter some words (separated by spaces) to generate a password: ").split()

    # Generate and display the password
    password = generate_password(user_words)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
