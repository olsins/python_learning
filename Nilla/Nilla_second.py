

class Weapon:
    def __str__(self):
        return "{}, Beschreibung: {}".format(self.name, self.description)

class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist-sized rock, suitable for bludgeoning"
        self.damage = 5

class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust." \
                            "Somewhat more dangerous than a rock."
        self.damage = 10
    
class Rustysword(Weapon):
    def __init__(self):
        self.name = "Rusty sword"
        self.description = "This sword is showing its age, " \
                            "but still has some fight in it."
        self.damage = 20


""" class Weapon:
    def __init__(self, name, description, damage):
        self.name: name
        self.description: description
        self.damage: damage
    
    def __str__(self):
        return "Name: " + self.name \

weapons_list = [Weapon("Dagger", "scharfes Teil", 10)
    , Weapon("Rock", "nicht so scharfes Teil", 5)
    , Weapon("Rustysword", "showing its age", 20)] """


def play():
    inventory = [Dagger(), 'Gold(5)', 'Crusty Bread',
                 'Vanilla(10)', 'Chocolate(0)']
    print("Escape from Nillas Castle")
    while True:
        action_input = get_player_command()
        if action_input in ['n', 'N']:
            print("Go North")
        elif action_input in ['s', 'S']:
            print("Go South")
        elif action_input in ['e', 'E']:
            print("Go East")
        elif action_input in ['w', 'W']:
            print("Go West")
        elif action_input == 'i' or action_input == 'I':
            print("Inventory: ")
            for item in inventory:
                print('* ' + str(item))
        else:
            print("Invalid Action")


def get_player_command():
    return input('Action: ')


play()
