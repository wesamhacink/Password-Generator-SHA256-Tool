
import secrets
import string
import hashlib


# Function to generate a secure password
def generate_password(length):

    if length < 4:
        raise ValueError("Password length must be at least 4.")

    characters = string.ascii_letters + string.digits + string.punctuation

    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    for _ in range(length - 4):
        password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


# Function to calculate SHA-256 hash
def calculate_hash(text):

    encoded_text = text.encode('utf-8')

    hash_object = hashlib.sha256(encoded_text)

    return hash_object.hexdigest()


# Main program
def main():

    print("=" * 45)
    print("     PASSWORD GENERATOR & SHA-256 TOOL")
    print("=" * 45)

    try:
        length = int(input("\nEnter password length: "))

        password = generate_password(length)

        print("\n[+] Generated Password:")
        print(password)

        hash_value = calculate_hash(password)

        print("\n[+] SHA-256 Hash:")
        print(hash_value)

    except ValueError as error:
        print("\n[!] Error:", error)


if __name__ == "__main__":
    main()
