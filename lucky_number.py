#importing important modules
import random #to randomly pick numbers
import string #to use inbuilt module digits

#welcome message
print("-----------------------------")
print("Welcome to Lucky Number Game!\nVersion 1.0.1\nBy SizzyTech")
print("-----------------------------\n")

#Help and game instructions
if input("Press Enter to Play or any key For help: ") :
    print("Please follow instructions to play the Lucky Number game.\n"
          "1. Only a single digit is allowed in the game.\n"
          "2. You are given 3 chances to guess a number.\n"
          "3. When you enter a wrong number, chances reduce by 1.\n"
          "Good luck!\n")

#Initializing the game
while True :
    numbers = string.digits #a list of numbers to be used
    chances = 3 #this will be used to limit number of attempts
    lucky_number = random.choice(numbers) #picking a random number
    win = False #this will be used to control our loop in case one wins the game

    while chances > 0 and not win: #this runs when one still has chances and has not won the game
        choice = input("\nEnter your Lucky number: ") #Users guessed number

        if len(choice)==1 and choice.isdigit(): #comfirms if a single digit is entered

            if int(choice)==int(lucky_number): #comparing the guessed number with the lucky number
                print("✅Congratulations! You got it!\n") #message if they are same
                win = True #this will kill the loop

            else:
                #Hint
                if choice < lucky_number:
                    print(f"❌{choice} is less than The lucky number!")
                elif choice > lucky_number:
                    print(f"❌{choice} is greater than The lucky number!")
                chances -= 1 #decrement of chances
                print(f"👺You have {chances} chances left.\n") #notice of remaining chances
                if chances == 0:
                    print("😫You lose!")  #if chances are over then you lose
                    print(f"The lucky number was 👉 {lucky_number}\n.")
        else:
            print("🔄️Please enter a valid Lucky number.eg.1,2 or 3.") #error message for non digits and digits more than 1
            print(f"👺You have {chances} chances left\n")

    if input("🔨Give it another try? y/n: ") == "y":
        pass
    else:
        print("\n👍Thanks for playing twinocode games.\n🌐www.twinocode.com\nExiting...")
        exit()