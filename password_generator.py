import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    """Generate a random password with specified criteria."""
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("At least one character type must be selected.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_preferences():
    """Prompt the user for password preferences."""
    print("Password Generator Settings:")
    try:
        length = int(input("Enter password length (8-64): "))
        if not validate_length(length):
            print("Invalid length. Defaulting to 12 characters.")
            length = 12
        
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        
        return {
            'length': length,
            'use_uppercase': use_uppercase,
            'use_digits': use_digits,
            'use_symbols': use_symbols
        }
    except ValueError:
        print("Invalid input. Using default settings.")
        return {
            'length': 12,
            'use_uppercase': True,
            'use_digits': True,
            'use_symbols': True
        }

def validate_length(length):
    """Check if password length is within the valid range (8-64)."""
    return 8 <= length <= 64

def main():
    """Main function to run the password generator."""
    print("=== Secure Password Generator ===")
    prefs = get_user_preferences()
    
    try:
        password = generate_password(
            length=prefs['length'],
            use_uppercase=prefs['use_uppercase'],
            use_digits=prefs['use_digits'],
            use_symbols=prefs['use_symbols']
        )
        print(f"\nGenerated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()