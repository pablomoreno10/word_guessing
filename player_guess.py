import random

# Game loop
while True:
    player_list = ['messi', 'ronaldo', 'neymar', 'aubameyang', 'isco', 'pele', 'pedri', 'neymar']

    choice = random.choice(player_list)
    len_choice = len(choice)
    initial = '_' * len_choice
    list_guessed = list(initial)
    p = 10  # Player's lives

    # Single game logic
    while p > 0:
        print("\nYour soccer player is: " + ''.join(list_guessed))
        
        letter = input("Guess a letter: ").lower()

        if letter in choice and len(letter) == 1:
            for i in range(len(choice)):
                if choice[i] == letter:
                    list_guessed[i] = letter
            print("\nCorrect, you have " + str(p) + " lives left!")
        else:
            p -= 1
            print("Incorrect, you have: " + str(p) + " lives left!")
        
        if '_' not in list_guessed:
            print('\nCongratulations, you won the game! \nThe name of the player is: ' + ''.join(list_guessed))
            break

    if p == 0 and '_' in list_guessed:
        print('\nSorry, you lost the game! You have 0 lives left. \nThe name of the player is: ' + choice)

    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("\nThanks for playing! Goodbye.")
        break
