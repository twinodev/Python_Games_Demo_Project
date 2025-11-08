#one will tell whether a number is even or odd
import random
import string

#welcome message
print("------------------------")
print("Welcome to Odd Even Game!\nVersion 1.0.1\nBy twinocode")
print("------------------------\n")

if input("Press Enter to Play or any key For help: ") :
    print("Please follow instructions to play the Odd Even game.\n"
          "1. Tell whether a displayed number is Odd or even.\n"
          "2. This is a single attempt game.\n"
          "3. Respond with numbers eg. 1 for Odd.\n"
          "Good luck!\n")
while True:
    numbers = string.digits
    random_number = random.choice(numbers)

    print(f"\n{random_number} is: \n1. Odd\n2.Even\n")
    remainder = int(random_number) % 2
    response  = input("Type here👉: ")

    if response == "1":
        if remainder == 0:
            print(f"\n{random_number} is Even.\nYou Lose!")
        elif remainder == 1:
            print(f"\n{random_number} is Odd.\nYou Win!")
    elif response == "2":
        if remainder == 0:
            print(f"\n{random_number} is Even.\nYou Win!")
        elif remainder == 1:
            print(f"\n{random_number} is Odd.\nYou Lose!")
    elif response.isalpha():
        print("\nPlease enter a number.")
    else:
        print("\ninvalid response!")

    if input("\n🔨Give it another try? y/n: ") == "y":
        pass
    else:
        print("\n👍Thanks for playing twinocode games.\n🌐www.twinocode.com\nExiting...")
        exit()