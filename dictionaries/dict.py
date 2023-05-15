dict1={
    "apple":"Elma",
    "Pear":"Armut",
    "Cherry":"Kiraz"
}
print(dict1['apple'])
print(dict1['Pear'])
print(dict1['Cherry'])

dict1['Watermelon']="Karpuz"
print(dict1['Watermelon'])
print(dict1) #will list all keys and values
print(dict1.values()) #list all values only
print(dict1.keys()) #print keys only

student = {
    "name":"John",
    "lastname":"Smith",
    "Profession":"Doctor",
    "Age":45,
    "Hobbies": ["Cycling", "Swimming", "Rock Climbing", "Running"],
    "Branch":"Computers"
}

print(student)
print(student.get('name')) #get name separately
print(student['name'])
print(student['lastname'])
print(student['Profession'])
print(student['Age'])
print(student['Hobbies'])
print(student['Branch'])