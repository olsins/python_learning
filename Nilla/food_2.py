class Person:  
    def __init__(self, name, age, favorite_foods):
        self.name = name
        self. age = age
        self.favorite_foods = favorite_foods
    
    def __str__(self):
        return "Name: " + self.name \
            + "Age: " + str(self.age) \
            + " Favorite food: " + str(self.favorite_foods[0])

people = [Person("Ed", 11, ["hotdogs", "jawbreakers"])
            , Person("Edd", 11, ["broccoli"])
            , Person("Eddy", 12, ["chunky puffs", "jawbreakers"])]

for person in people:
    print(person)
