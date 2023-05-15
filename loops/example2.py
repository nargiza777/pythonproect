fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1