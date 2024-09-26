import random

tools = ("rock", "paper", "scissors")

while True:
    computer_choice = random.choice(tools) 
    menu = int(input("Please choose a number\n1-Paper\n2-Rock\n3-Scissors\n4-Quit\n"))
    
    if menu == 1:
        player_choice = "paper"
        if computer_choice == "rock":
            print(f"You chose {player_choice}, computer chose {computer_choice}. You win!")
        elif computer_choice == "paper":
            print(f"You chose {player_choice}, computer chose {computer_choice}. It's a tie!")
        elif computer_choice == "scissors":
            print(f"You chose {player_choice}, computer chose {computer_choice}. You lose!")
    
    elif menu == 2:
        player_choice = "rock"
        if computer_choice == "paper":
            print(f"You chose {player_choice}, computer chose {computer_choice}. You lose!")
        elif computer_choice == "scissors":
            print(f"You chose {player_choice}, computer chose {computer_choice}. You win!")
        elif computer_choice == "rock":
            print(f"You chose {player_choice}, computer chose {computer_choice}. It's a tie!")
    
    elif menu == 3:
        player_choice = "scissors"
        if computer_choice == "rock":
            print(f"You chose {player_choice}, computer chose {computer_choice}. You lose!")
        elif computer_choice == "paper":
            print(f"You chose {player_choice}, computer chose {computer_choice}. You win!")
        elif computer_choice == "scissors":
            print(f"You chose {player_choice}, computer chose {computer_choice}. It's a tie!")
    
    elif menu == 4:
        print("Thanks for playing! Goodbye!")
        break
    
    else:
        print("Please enter a valid number!")
