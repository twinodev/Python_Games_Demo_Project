import random

districts = ["Kampala", "Gulu", "Mbarara", "Jinja", "Arua", "Masaka", "Mbale", "Fortportal", "Lira", "Soroti"]

chosen_district = random.choice(districts)
chosen_district = chosen_district.lower() 
hidden_word = ["_"] * len(chosen_district)
lives = len(chosen_district) - 1

print("Welcome to the Hangman Game!")

print("Guess the name of a district in Uganda.")
print("You have", lives, "lives.")
print(" ".join(hidden_word))

while "_" in hidden_word and lives > 0:
    guess = input("\nGuess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in chosen_district:
        for index in range(len(chosen_district)):
            if chosen_district[index] == guess:
                hidden_word[index] = guess
        print("Good job! You found a letter.")
    else:
        lives -= 1
        print("Wrong guess! You lost a life.")
        print("Lives left:", lives)

    print(" ".join(hidden_word))
if "_" not in hidden_word:
    print("\nCongratulations! You guessed the district:", chosen_district.capitalize())
else:
    print("\nYou ran out of lives. The district was:", chosen_district.capitalize())
