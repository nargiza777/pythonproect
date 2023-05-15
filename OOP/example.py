class Person:
    Count=0
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname
        self.email = "{}.{}@company.com".format(self.name,self.lastname)
        Person.Count+=1 #Person.Count=Person.Count+1 #increment by 1
    def __del__(self):
        Person.Count-=1

user1 = Person("A","B")
user2 = Person("AV","BC")
user3 = Person("Harry","Blue")

print(user1.email)
print(user2.email)
print(user3.email)

print(Person.Count)
del(user1)
del(user2)
del(user3)
print(Person.Count)