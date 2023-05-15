class Person:
    pass
    def speak(self):
        print("Hi my name is {} {}".format(self.name,self.lastname))

person1 = Person()
person1.name = "Jony"
person1.lastname = "Brown"
person1.email = "email"

print("{}- {} - {}".format(person1.name,person1.lastname,person1.email))

person1.speak
