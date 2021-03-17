class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        return "name: " + self.name \
            + " calories: " + str(self.total_calories())

    def total_calories(self):
        all_calories = 0
        for y in self.ingredients:
            all_calories = y.calories() + all_calories
        return all_calories


class Food:
    def __init__(self, name, carbs, protein, fat):
        self.name = name
        self.carbs = carbs
        self.protein = protein
        self.fat = fat

    def calories(self):
        return (self.carbs*4) + (self.protein*4) + (self.fat*9)

    def __str__(self):
        return "Name: " + self.name \
            + " Carbs " + str(self.carbs) \
            + " protein " + str(self.protein) \
            + " fat " + str(self.fat) \
            + " calories: " + str(self.calories())


# dishes = [Food(), Food()]
dishes = [Food("lasagne", 11, 12, 13),
          Food("chicken", 1, 5, 7)]


recipe = [Recipe("crazyfood", dishes)]

# print(dishes)
for x in dishes:
    print(x)

# print(recipe)

for x in recipe:
    print(x)
