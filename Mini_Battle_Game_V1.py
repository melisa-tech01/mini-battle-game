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
        print(self.name, self.health, self.level)

player1 = Player("Aria", 100, 2)
player1.attack()
player1.take_damage(20)
player1.level_up()
player1.show_status()



class Wizard():
    def __init__(self, name, magic, level):
        self.name = name
        self.magic = magic
        self.level = level

    def introduce(self):
        print("I am", self.name, ", I have", self.magic, "and I am level", self.level)

    def cast_spell(self):
        print(self.name, "casts a spell.")

    def level_up(self):
        self.level = self.level + 1

    def take_damage(self, damage):
        self.magic = self.magic - damage


wizard1 = Wizard("Arya", 80, 3)
wizard1.introduce()
wizard1.cast_spell()
wizard1.level_up()
wizard1.introduce()
wizard1.take_damage(20)
wizard1.introduce()