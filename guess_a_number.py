import random

computer_number = random.randint(1, 100)


while True:
    player_input = input("Guess the number (1-100):")

    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue

    player_number = int(player_input)

    if player_number > 100 or player_number <= 0:
        print("The number is not in range.Please use only permissible range!")
        continue
    if player_number == computer_number:
        print("Yes you guess it!")
        break
    difference = abs(player_number - computer_number)
    if player_number > computer_number:
        if difference > 20:
            print("Too High!")
        else:
            print("Is High!")
    elif player_number < computer_number:
        if difference > 20:
            print("Is low")
        else:
            print("Too Low!")



