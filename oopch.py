class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type=None, count=1, **kwargs):
        # Handle kwargs (multiple animals at once)
        if kwargs:
            for animal, qty in kwargs.items():
                if animal in self.animals:
                    self.animals[animal] += qty
                else:
                    self.animals[animal] = qty
        else:
            # Handle single animal
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count

    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
        info += "\n    E-I-E-I-0!"
        return info

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()
        animals_plural = []

        for animal in animal_types:
            if self.animals[animal] > 1:
                animals_plural.append(animal + "s")
            else:
                animals_plural.append(animal)

        if len(animals_plural) == 1:
            animals_str = animals_plural[0]
        else:
            animals_str = ", ".join(animals_plural[:-1]) + " and " + animals_plural[-1]

        return f"{self.name}'s farm has {animals_str}."



macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
print(macdonald.get_short_info())


macdonald2 = Farm("McDonald")
macdonald2.add_animal(cow=5, sheep=2, goat=12)
print(macdonald2.get_info())
