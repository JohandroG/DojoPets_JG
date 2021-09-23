from Pet import Pet
from Ninja import Ninja


dog = Pet("Moly","Dog","Eat Apples")
rabbit = Pet("Cleo","Rabbit","Fly")
cat = Pet("Juanito","Cat","Make Funny Videos")

ninja1 = Ninja("Bryan","Cascante","Bone","Dog Food", dog)
ninja2 = Ninja("Valera","Perez","Candy","Rabbit Food", cat)
ninja3 = Ninja("Julian","Alvarez","Carrot","Rabbit Food", rabbit)

ninja1.walk().feed().feed().petstatus()
ninja2.walk().feed().feed().petstatus()
ninja3.walk().feed().feed().petstatus()





