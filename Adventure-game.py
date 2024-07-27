import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


def start_game():
    print_pause("You find yourself standing in an open field, \nfilled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere around here,\n and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty \n(but not very effective) dagger.")


def get_choice():
    while True:
        choice = input("Enter 1 to knock on the door of the house.\n"
                       "Enter 2 to peer into the cave.\n"
                       "What would you like to do? (Please enter 1 or 2): ")
        if choice in ['1', '2']:
            return choice
        else:
            print("Invalid input. Please enter 1 or 2.")


def knock_on_door():
    print_pause("You knock on the door and a friendly wizard opens it.")
    print_pause("He gives you a magical item and wishes you well on your journey.")
   


def peer_into_cave():
    print_pause("You peer into the cave and see a treasure chest.")
    print_pause("As you approach the chest, a monster jumps out!")
   


def play_game():
    start_game()
    choice = get_choice()
    if choice == '1':
        knock_on_door()
    elif choice == '2':
        peer_into_cave()


def random_enemy():
    enemies = ['pirate', 'troll', 'dragon']
    return random.choice(enemies)


def fight():
    outcome = random.choice(['win', 'lose'])
    if outcome == 'win':
        print_pause("You defeated the monster and won the game!")
    else:
        print_pause("You were defeated by the monster. Game over!")


def play_again():
    while True:
        again = input("Would you like to play again? (y/n): ").lower()
        if again == 'y':
            play_game()
        elif again == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def main():
    play_game()
    play_again()


if __name__ == "_main_":
    main()