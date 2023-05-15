name = ""
students=[]
while name !="quit" :                #this loop will run until name is not equal to "quit"
    name = input("Enter a name :")
    if name=="quit":
        print("Good Bye")
        break
    else:
        students.append(name)
    print("You have entered {}".format(name))
    print("To quit enter quit")
print("These are the students {} ".format(students))