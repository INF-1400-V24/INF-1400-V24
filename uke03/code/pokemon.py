
class Pokemon:

    def __init__(self, name, level, base_moves):
        self.name = name
        self.level = level
        self.healthpoints = level * 5
        self.moves = {}
        for move, dmg in base_moves.items():
            self.moves[move] = dmg * level / 10
    
    def calculate_hit(self, choice, other):
        return self.moves[choice]

    def use_move(self, other):
        print(self.name, "is about to attack", other.name)
        print("Available moves:", self.moves)
        choice = input("Select move: ")
        if choice not in self.moves:
            print("You failed, haha...")
            return
        other.healthpoints -= self.calculate_hit(choice, other)
        if other.healthpoints <= 0:
            print(other.name, "fainted!!!")
        else:
            print(other.name, "has", other.healthpoints, "HP left")
    
    def __str__(self):
        info = "Pokemon: " + self.name + "\n"
        info += "Level: " + str(self.level) + "\n"
        info += "HP: " + str(self.healthpoints)
        return info
    

class FireTypePokemon(Pokemon):

    def __init__(self, name, level, base_moves):
        super().__init__(name, level, base_moves)

    def calculate_hit(self, choice, other):
        if isinstance(other, GrassTypePokemon):
            return self.moves[choice] * 2
        return self.moves[choice]



class GrassTypePokemon(Pokemon):

    def __init__(self, name, level, base_moves):
        super().__init__(name, level, base_moves)

    def calculate_hit(self, choice, other):
        if isinstance(other, FireTypePokemon):
            return self.moves[choice] / 2
        return self.moves[choice]
    


if __name__ == "__main__":
    char = FireTypePokemon("Charmander", 10, {"Ember": 20})
    bulba = GrassTypePokemon("Bulbasaur", 10, {"Tackle": 15})

    char.use_move(bulba)
    bulba.use_move(char)

    print("\nBattle has ended!")
    print(char)
    print(bulba)








