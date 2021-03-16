class Food:
    def __init__(self, name, carbs, protein, fat):
        self.name = name
        self.carbs = carbs
        self.protein = protein
        self.fat = fat

    def __str__(self):
        return "Name: " + self.name \
            + " Carbs" + self.carbs \
            + " protein" + self.protein \
            + "fat" + self.fat


dishes = [Food("lasagne", 11, 12, 13), Food("chicken", 1, 5, 7)]

for foods in dishes:
    print(foods)
