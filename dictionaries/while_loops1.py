#WE WANT TO GUESS A NUMBER
# num1 = 10
#
# while num1 !="9":     #WHILE num1 is not equal 1 - run the loop
#     num1 = input("ENTER a name: ")
#     print("You have entered {}".format(num1))
#     print("To quit enter 9 ")
# print("Good Bye")

name = ""
students=[]
while name !="quit":
    name = input("ENTER a name: ")
    if name=="quit":    #WE CAN USE CONDITIONS TO GET OUT OF THE LOOP
        print("Good Bye")
        break
    else:
        students.append(name)
    print("You have entered {}".format(name))
    print("To quit enter quit ")
print("Good Bye")

print("These are the students {}".format(students)) #this is the way to print input from user