#! python3

superheroes = { "flash": {"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman": {"speed": "slowest", "intelligence": "highest", "strength": "money"}, "superman": {"speed": "fast", "intelligence": "average", "strength": "strongest"} }

start_again = True

def get_char_name():
    char_name = input("Which character do you want to know about? (Flash, Batman, Superman)\n")
    return char_name
def get_char_stat():
    char_stat = input("What statistic do you want to know about? (strength, speed, or intelligence)\n")
    return char_stat

while start_again == True:
    # Collect user input for name and validate input
    char_name = get_char_name()

    while char_name != "Flash" and char_name != "Batman" and char_name != "Superman":
        print("Enter a valid name\n")
        char_name = get_char_name()

    # Collect user input for stat and validate input
    char_stat = get_char_stat().lower()
    
    while char_stat != "strength" and char_stat != "speed" and char_stat != "intelligence":
        print("Enter a valid stat\n")
        char_stat = get_char_stat().lower()

    # Prints info from dictionary based on user input
    print(f"{char_name}'s {char_stat} is: {superheroes[char_name.lower()][char_stat]}")

    # Sets our while conditional
    try_again = input("Would you like to start again?\n").lower()
    if try_again == "yes":
        start_again = True
    else:
       break