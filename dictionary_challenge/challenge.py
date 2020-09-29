#! python3

superheroes = { "flash": {"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman": {"speed": "slowest", "intelligence": "highest", "strength": "money"}, "superman": {"speed": "fast", "intelligence": "average", "strength": "strongest"} }

char_name = input("Which character do you want to know about? (Flash, Batman, Superman)\n").lower()

char_stat = input("What statistic do you want to know about? (strength, speed, or intelligence)\n").lower()

print(f"{char_name}'s {char_stat} is: {superheroes[char_name][char_stat]}")