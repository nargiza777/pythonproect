#without list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []  #Based on a list of fruits, we want a new list, containing only the fruits with the letter "a" in the name.

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#with list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)