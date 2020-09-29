import argparse

superheroes = { "flash": {"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman": {"speed": "slowest", "intelligence": "highest", "strength": "money"}, "superman": {"speed": "fast", "intelligence": "average", "strength": "strongest"} }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find a superhero's stats")
    parser.add_argument('-hero', choices=superheroes.keys(), help="Pick a superhero")
    parser.add_argument('-stat', choices=superheroes['superman'].keys(), help="Pick speed, intelligence, or strength")

args = parser.parse_args()
hero = args.hero
stat = args.stat

print(f"{hero}'s {stat} is: {superheroes[hero][stat]}")