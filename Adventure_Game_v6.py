# Adventure game by Chris Darden
# 11/30/2020
import time
import random

weapons = ["a shovel", "a sword", "a pencil",
           "an axe", "a golf club", "scissors"]
creatures = ["troll", "penguin", "dog", "puppy",
             "hobgoblin", "wild Joy", "a lion"]
speed = int(input("1=Fast 2=A short pause 0=Instant\n"))
global success
global tool
global weapon
global greeting
global option


def setDefaults():
    global tool
    global greeting
    tool = "a dagger"
    greeting = "You find yourself standing in an open field, filled with "\
               "grass & yellow wildflowers. Rumor has it that a wicked "\
               "fairie is somewhere around here, & has been terrifying "\
               "the nearby village.\n"


def main():
    setDefaults()
    print_pause(greeting)
    path()


def validate(option):
    while True:
        if option not in ["1", "2"]:
            print("Please enter only 1 or 2\n")
            option = input("Enter a valid choice:")
        else:
            return option


def getWeapon():
    return weapon


def getTool():
    return tool


def weapon():
    weapon = random.choice(weapons)
    return weapon


def cave():
    global tool
    tool = weapon()
    print_pause("You have entered the cave.")
    print_pause("There's a chest by the cave wall and a extinguished flame.")
    print_pause("Someone was recently here...")
    print_pause("You decide to open the chest......")
    time.sleep(speed)
    print_pause("The chest was hard to open but you found " + tool + "!")
    print_pause("Maybe this might come in handy...")
    print_pause("Let's go back to the field with our new tool..")
    field()


def fight():
    creature = random.choice(creatures)
    weapon = random.choice(weapons)
    print_pause("It's time to fight!")
    print_pause("A " + creature + " has appeared and has " + weapon + "!")
    toolTest = getTool()
    if tool == "":
        print_pause("You have no weapon.")
        print_pause("You have died.")
        again()
    else:
        print_pause("You are weilding " + toolTest + ".")
        print_pause("Do you want to fight the " + creature + "?\n")
        option = validate(input("1 for yes, 2 for no\n"))
        if option == "1":
            print("You swing your " + toolTest + " at the " + creature + "!")
            if toolTest == "a dagger":
                print("Your " + toolTest + " was inaffective. You died.")
                again()
            else:
                print_pause("You win!")
                again()
        elif option == "2":
            print_pause("You attempt to run away.")
            field()


def cabin():
    print_pause("You have entered the cabin!")
    print_pause("You hear footsteps in another room..")
    print_pause("You realize you are not alone..")
    fight()


def field():
    print_pause("You have reached the field! You are safe, for now.")
    path()


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(speed)


def path():
    option = validate(input("1 for the cabin, 2 for the cave\n"))
    if "1" in option:
        cabin()
    elif "2" in option:
        cave()


def again():
    again = 0
    print_pause("Would you like to play again?")
    again = validate(input("1 for yes, 2 for no\n"))
    if again == "1":
        main()
    elif again == "2":
        print("Thanks for playing.")


main()
