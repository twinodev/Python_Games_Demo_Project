#tells whether input is vowel or consonant
import string

letters = string.ascii_letters
vowels = ['a', 'e', 'i', 'o', 'u']
#welcome message
print("--------------------------")
print("Welcome to Vowel Cons Game!\nVersion 1.0.1\nBy twinocode")
print("--------------------------")

while True:
    result = ""

    prompt = input("\nPlease enter a letter: ").lower()

    if len(prompt) ==1 and prompt.isalpha():
        if prompt in vowels:
            result = "vowel"
        else:
            result = "consonant"
        print(f"\n{prompt} is a {result}")
    else:
        print("\nInvalid input!\nPlease Enter a letter and try again.")


    if input("\n🔨Try another letter? y/n: ") == "y":
        pass
    else:
        print("\n👍Thanks for playing twinocode games.\n🌐www.twinocode.com\nExiting...")
        exit()