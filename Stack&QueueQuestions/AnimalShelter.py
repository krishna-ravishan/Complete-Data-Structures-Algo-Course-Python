class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal, type):
        if type == "Cat":
            self.cats.append(animal)
        else:
            self.dogs.append(animal)
    
    
