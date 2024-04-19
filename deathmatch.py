import random

class World(object):
    creatures = []
    day = 0

    def do_a_day():
        World.day += 1
        random.shuffle(World.creatures)
        left_side = World.creatures[:len(World.creatures)//2]
        right_side = World.creatures[len(World.creatures)//2:]

        for left_creature, right_creature in zip(left_side, right_side):  # if the overall number of creatures is odd, the one that doesn't have a pair simply doesn't interact
            left_creature.interact(right_creature)

    def get_creatures():
        return(World.creatures)

    def get_population(species):
        population_count = 0
        for creature in World.creatures:
            if isinstance(creature, species):
                population_count += 1
        return(population_count)

class _Creature(object):
    def __init__(self):
        World.creatures.append(self)

    def die(self):
        World.creatures.remove(self)
        del self

    def interact(self, opponent):
        if type(opponent) == self.wins_against:
            opponent.die()
        elif type(opponent) == self.looses_against:
            self.die()
        elif type(opponent) == type(self):
            # introduce sexual reproduction here
            pass

class Rock(_Creature):
    def __init__(self):
        super().__init__()
        self.wins_against = Scissor
        self.looses_against = Paper

class Paper(_Creature):
    def __init__(self):
        super().__init__()
        self.wins_against = Rock
        self.looses_against = Scissor

class Scissor(_Creature):  # one creature is scissor, many creatures are scissors
    def __init__(self):
        super().__init__()
        self.wins_against = Paper
        self.looses_against = Rock

def spawn(species, number):
    for i in range(number):
        species()

def print_current_state():
    print(f"""Day {World.day}\nrocks: {World.get_population(Rock)}\t papers: {World.get_population(Paper)} scissors: {World.get_population(Scissor)}""")

def main():

    spawn(Rock, 100)
    spawn(Paper, 100)
    spawn(Scissor, 100)
    for i in range(20):
        print_current_state()
        World.do_a_day()
    print_current_state()

if __name__ == "__main__":
    main()