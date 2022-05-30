import random

while True:

    choices = [ "rock" , "paper" , "scissors" ]

    CPU = random.choice ( choices )
    player = None

    while player not in choices:
        player = input("rock, paper or scissors: ? ").lower()
    if player == CPU:
        print("CPU ", CPU + " : " + "Player", player)
        print("tie!")
    elif player == "rock":
        if CPU == "paper":
            print ( "CPU " , CPU + " : " + "Player", player)
            print("You Lose!")
        if CPU == "scissors":
            print ( "CPU " , CPU + " : " + "Player" , player )
            print("You win!")
    elif player == "scissors":
        if CPU == "paper":
            print("CPU ", CPU + ":" + "Player", player)
            print("You win!")
        if CPU == "rock":
            print ( "CPU " , CPU + " : " + "Player " , player )
            print("You Lose!")
    elif player == "paper":
        if CPU == "rock":
            print("CPU ", CPU + " : " + "Player", player)
            print("You win!")
        if CPU == "scissors":
            print("CPU ", CPU + " : " + "Player", player)
            print("You Lose!")
    play_again = input("Play again ? : yes / no ").lower()

    if play_again != "yes":
        break

print("bye!")



