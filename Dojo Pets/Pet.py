
class Pet:
    
    pets = []
    
    def __init__(self, name , type , tricks ):

        self.petName = name
        self.petType = type
        self.petTrick = tricks
        self.pethealth = 100
        self.petenergy = 100
        Pet.pets.append(self)


    
    def sleep(self):
        self.petenergy += 25
        print("hi")
        return self
    
    def eat(self):
        self.petenergy += 5
        self.pethealth += 10
        return self

    def play(self):
        self.pethealth += 5
        return self

    def noise(self):
        print( f"You are cleaning {self.petName}")
        print("oooouuups")        
        if self.petType == "Dog":
            print( f"{self.petName} said... Guaf")
        elif self.petType == "Cat":
            print( f"{self.petName} said...Miauu")
        elif self.petType == "Chiken":
            print( f"{self.petName} said... Pio Pio")
        elif self.petType == "Turtle":
            print( f"{self.petName} said... ...")
        elif self.petType == "Bird":
            print( f"{self.petName} said... Chriip")
        elif self.petType == "Rabbit":
            print( f"{self.petName} said... ... Jump XD")
        else:
            print('This animal sound is not registered')

        print( f"Sorry {self.petName}")

    def infopet(self):
        print( f"You pet's name is {self.petName}")
        print( f"{self.petName} health level is {self.pethealth}")
        print( f"{self.petName} energy level is {self.petenergy}")
        print( f"{self.petName} knows this especial trick: {self.petTrick}")