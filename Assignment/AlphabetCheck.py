# It uses a function called `check_alphabet` that takes an alphabet as an argument.
# The function checks if the lowercase version of the alphabet is present in the list of vowels.
# If it is, the function returns "Vowel". Otherwise, it returns "Consonance".
# The result is then printed to the console.
def check_alphabet(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if alphabet.lower() in vowels:
        return "Vowel"
    else:
        return "Consonance"

alphabet = input("Enter an alphabet: ")
print(check_alphabet(alphabet))


