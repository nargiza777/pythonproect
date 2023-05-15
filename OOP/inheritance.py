class Animal:
    def __init__(self,color,age,weight):
        self.color=color
        self.age=age
        self.weight = weight
    def move(self):
        print("I am moving")
    def eat(self):
        print("Eating like an animal")
class Dog(Animal):
    def __init__(self,color,age,weight,name):
        super().__init__(color,age,weight)
        self.name = name
    def move(self):
        print("I am a dog I am moving like a dog")
    def jump(self):
        print("Jump like a dog")
    def eat(self):
        print("Eating food like a dog")

class Cat(Animal):
    def __init__(self,color,age,weight,name):
        super().__init__(color,age,weight)
        self.name = name
    def move(self):
        print("I am moving as cat mirrrr")
    def jump(self):
        print("Jump")
    def eat(self):
        print("Eating food like a cat")

class Cow:
    def die(self):
        print("Dieng")

class Farmer:
    def feed(self,creture):
        creture.eat()
    def slaughter(self,animal):
        if isinstance(animal,Cow):
            animal.die()
        else:
            print("You can't slaughter me{}".format(animal.__class__))
class Wolf(Dog):
    def __init__(self,color,age,weight,name=None):
        super().__init__(color,age,weight,name)
        #Dog(color, age, weight, name)
        self.name = name
    def make_sound(self):
        print("howl")
animal = Animal("Green",15,10)
animal.move()
dog = Dog("Browm",20,30,"Browny")
cat = Cat("White",10,15,"Fur ball")
cat.move()
cat.jump()
dog.jump()
farmer = Farmer()
farmer.feed(dog)
farmer.feed(cat)
farmer.feed(animal)
wlf = Wolf("Gray",100,20)
wlf.make_sound()
farmer.slaughter(wlf)
cow = Cow()
farmer.slaughter(cow)
farmer.slaughter(dog)
farmer.slaughter(cat)