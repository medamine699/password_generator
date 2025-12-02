import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    """
    Génère un mot de passe aléatoire selon les critères choisis.

    Args:
        min_length (int): longueur minimale du mot de passe
        numbers (bool): inclure des chiffres
        special_characters (bool): inclure des caractères spéciaux

    Returns:
        str: mot de passe généré
    """
    letters = string.ascii_letters  # lettres majuscules et minuscules
    digits = string.digits          # chiffres 0-9
    special = string.punctuation    # symboles spéciaux

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meet_criteria = False
    has_numbers = False
    has_special = False

    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_numbers = True
        elif new_char in special:
            has_special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_numbers
        if special_characters:
            meet_criteria = meet_criteria and has_special

    return pwd

# ---------------------- Exécution du programme ----------------------
if __name__ == "__main__":
    min_length = int(input("Enter the minimum length: "))
    has_number = input("Do you want to include numbers (y/n)? ").lower() == "y"
    has_special = input("Do you want to include special characters (y/n)? ").lower() == "y"

    pwd = generate_password(min_length, has_number, has_special)
    print("The generated password is:", pwd)
