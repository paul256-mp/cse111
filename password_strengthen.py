# Character type constants
LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0","1","2","3","4","5","6","7","8","9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", '"', ",", ".", "<", ">", "?", "/", "`", "~"]

def word_in_file(word, filename, case_sensitive=False):
    """Check if a word exists in a file with case sensitivity option."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                file_word = line.strip()
                if case_sensitive:
                    if file_word == word:
                        return True
                else:
                    if file_word.lower() == word.lower():
                        return True
        return False
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return False

def word_has_character(word, character_list):
    """Check if any character in the word exists in the character list."""
    for char in word:
        if char in character_list:
            return True
    return False

def word_complexity(word):
    """Calculate the complexity score of a word based on character types used."""
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

def password_strength(password, min_length=10, strong_length=16):
    """Evaluate and return the strength of a password (0-5) with appropriate messages."""
    # Check if password is in dictionary (case insensitive)
    if word_in_file(password, "wordlist.txt"):
        print("Password is a dictionary word and is not secure.")
        return 0
    
    # Check if password is in top passwords list (case sensitive)
    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0
    
    # Check password length
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    
    # Calculate complexity-based strength
    complexity = word_complexity(password)
    strength = 1 + complexity
    return strength

def main():
    """Main program loop for password strength checker."""
    print("Password Strength Checker")
    print("Enter a password to check its strength or 'q' to quit.")
    
    while True:
        password = input("\nEnter password: ").strip()
        
        if password.lower() == 'q':
            print("Exiting password strength checker.")
            break
        
        strength = password_strength(password)
        print(f"Password strength: {strength}/5")

if __name__ == "__main__":
    main()