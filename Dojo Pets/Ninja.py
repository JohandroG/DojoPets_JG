from Pet import Pet

class Ninja:

    ninjas = []

    def __init__( self, first_name , last_name , treats , pet_food, pet):
        
        self.firstName = first_name
        self.lastName = last_name
        self.treatS = treats
        self.petFood = pet_food
        self.Pet = pet
        Ninja.ninjas.append(self)

    
    def walk(self):
        print('You went in a walk with your pet, +5 health')
        self.Pet.play()
        return self
    
    def feed(self):
        print( f"You feed your pet, with {self.petFood}, +5 energy, +10 health")
        self.Pet.eat()
        return self

    def bathe(self):
        print("It's time to bath")
        self.Pet.noise()
        return self

    def petstatus(self):
        print("==========================")
        print("THIS IS YOUR PET'S STATUS")
        print("==========================")
        self.Pet.infopet()
        print("==========================")
        return self
