# A player is vs a computer to get who wins the queen
# Player 1 is human, Player 2 is computer and plays optimally.

#function to display the herds
def display_herds(herds):
    print("\nCurrent herds:")
    for i, h in enumerate(herds, 1):
        print(f"  Herd {i}: {h} cows")
    print()

#function for handling error when the cows in all herd are over.
def all_empty(herds):
    return all(h == 0 for h in herds)

#function for players turn actions
def player_turn(player, herds):
    print(f"\n{player}'s turn.")
    while True:
        try:
            herd_choice = int(input("Choose a herd number (1–3): "))
            if 1 <= herd_choice <= 3:
                #Denying selection from empty herds and error message
                if herds[herd_choice - 1] == 0:
                    print("That herd is empty! Choose another.")
                    continue
                break
            else:
                #for non integers and numbers not in range of herds
                print("Invalid herd number! Enter 1, 2, or 3.")
        except ValueError:
            # for non integers entered as herd_choice
            print("Enter a valid integer.")

    max_take = herds[herd_choice - 1]
    while True:
        try:
            cows = int(input(f"How many cows to take from herd {herd_choice} (1–{max_take}): "))
            if 1 <= cows <= max_take:
                return herd_choice - 1, cows
            else:
                print(f"Invalid number! You can take 1 to {max_take} cows.")
        except ValueError:
            print("Enter a valid integer.")

def computer_move(herds):
    print("\nComputer's turn 🤖")

    # Separate heaps
    non_empty = [h for h in herds if h > 0]
    heaps_more_than_one = [i for i, h in enumerate(herds) if h > 1]
    heaps_of_one = [i for i, h in enumerate(herds) if h == 1]

    # Endgame: all heaps have 1 cow
    if len(heaps_more_than_one) == 0:
        if len(heaps_of_one) % 2 == 1:
            # Losing position: take 1 from any heap
            herd_index = heaps_of_one[0]
            cows = 1
        else:
            # Winning position: take 1 to leave opponent with odd number
            herd_index = heaps_of_one[0]
            cows = 1
    else:
        # Normal Nim XOR strategy
        xor_sum = 0
        for h in herds:
            xor_sum ^= h

        if xor_sum == 0:
            # Losing position: take 1 from first heap > 1
            herd_index = heaps_more_than_one[0]
            cows = 1
        else:
            # Find a heap to reduce XOR to 0
            for i, h in enumerate(herds):
                target = h ^ xor_sum
                if target < h:
                    herd_index = i
                    cows = h - target
                    break

    print(f"Computer takes {cows} cow(s) from herd {herd_index + 1}")
    return herd_index, cows



def princess_win(herd1, herd2, herd3):
    print("🐄 Welcome to the Princess Win!")
    print("Rules:")
    print(" - 3 herds of cows.")
    print(" - On your turn, you can take any number of cows from ONE herd.")
    print(" - The player who makes the last pick that empties all herds loses!")
    print(" - The opponent Wins and takes The Princess!")
    print("Wish to see you back with the Crown!\n")

    herds = [herd1, herd2, herd3]
    player_name = input("Enter your name: ")
    turn = 0  # 0 = human, 1 = computer

    while True:
        display_herds(herds)

        if turn % 2 == 0:
            herd_index, cows_taken = player_turn(player_name, herds)
        else:
            herd_index, cows_taken = computer_move(herds)

        herds[herd_index] -= cows_taken

        if all_empty(herds):
            if turn % 2 == 0:
                print(f"\nAll herds are now empty!")
                print(f"{player_name} made the last pick and loses!")
                print("I won you!")
            else:
                print(f"\nAll herds are now empty!")
                print("Computer made the last pick and loses!")
                print(f"{player_name} Wins\nHe takes the Princess!")
            break

        turn += 1

#running the game
princess_win(20, 10, 13)
