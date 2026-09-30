class Player:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def attack(self):
        print(self.name, "attacks!")

    def take_damage(self, damage):
        self.health = self.health - damage
        print(self.name, "took", damage, "damage!", self.name, "has now", self.health, "health.")

    def level_up(self):
        self.level = self.level + 1 

    def show_status(self):
        print("Name:", self.name)
        print("Health:", self.health)
        print("Level:", self.level)

player1 = Player("Lucky", 100, 2)
player1.attack()
player1.take_damage(20)
player1.level_up()
player1.show_status()



class Wizard(Player):
    def __init__(self, name, health, magic, level):
        super().__init__(name, health, level)
        self.magic = magic

    def show_status(self):
        print("Name:", self.name)
        print("Health:", self.health)
        print("Level:", self.level)
        print("Magic:", self.magic)

    def cast_spell(self):
        self.magic = self.magic - 10
        print(self.name, "casts a spell.")

    def attack(self):
        print("The Wizard strikes!")


wizard1 = Wizard("Arya", 80, 40, 3)
wizard1.show_status()
wizard1.cast_spell()
wizard1.attack()
wizard1.level_up()
wizard1.show_status()
wizard1.take_damage(20)
wizard1.show_status()
