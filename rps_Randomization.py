# import random module
import random
import images

# Welcome user and ask them what rock(0), paper(1), and scissors(2).
name = input("Please enter your name: ")
choice = int(input(f"Welcome, {name}! Today we will be playing Rock, Paper, Scissors. Type 0 for Rock, 1 for Paper, "
                   f"or 2 for Scissors.\n"))

game_images = [images.rock, images.paper, images.scissors]

comp_choice = random.randint(0, 2)
computer = game_images[comp_choice]


if choice >= 3 or choice < 0:
    print("You typed an invalid number, you lose.")
else:
    player = game_images[choice]
    print(player)
    if player == computer:
        print("Computer chose:\n" + computer)
        print("It's a draw.")
    elif choice == 0:
        if comp_choice == 1:
            print("Computer chose:\n" + computer)
            print("You lose.")
        elif comp_choice == 2:
            print("Computer chose:\n" + computer)
            print("You win.")
    elif choice == 1:
        if comp_choice == 0:
            print("Computer chose:\n" + computer)
            print("You win.")
        elif comp_choice == 2:
            print("Computer chose:\n" + computer)
            print("You lose.")
    elif choice == 2:
        if comp_choice == 0:
            print("Computer chose:\n" + computer)
            print("You lose.")
        elif comp_choice == 1:
            print("Computer chose:\n" + computer)
            print("You win.")

