import random

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_score = 0
computer_score = 0

rounds = int(input("How many rounds do you want to play? "))

for _ in range(rounds):
    player_move = input("Choose [r]ock, [p]aper, [s]cissors: ")
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        print(RED + "Invalid input. Try again...." + RESET)
        continue

    computer_random_number = random.randint(1, 3)
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f"Player move: {player_move}")
    print(f"Computer move: {computer_move}")

    if (player_move == rock and computer_move == scissors) or \
       (player_move == paper and computer_move == rock) or \
       (player_move == scissors and computer_move == paper):
        print(GREEN + "You win this round!" + RESET)
        player_score += 1
    elif player_move == computer_move:
        print(YELLOW + "Draw!" + RESET)
    else:
        print(RED + "You lose this round!" + RESET)
        computer_score += 1

    print(f"Score -> Player: {player_score} | Computer: {computer_score}\n")

print("Final Score:")
print(f"Player: {player_score} | Computer: {computer_score}")

if player_score > computer_score:
    print(GREEN + "You are the overall winner!" + RESET)
elif player_score < computer_score:
    print(RED + "Computer wins overall!" + RESET)
else:
    print(YELLOW + "Overall result is a draw!" + RESET)
