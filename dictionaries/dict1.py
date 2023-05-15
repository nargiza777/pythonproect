student1 = {
    "name":"John",
    "lastname":"Smith",
    "Profession":"Doctor",
    "Age":45,
    "Hobbies": ["Cycling", "Swimming", "Rock Climbing", "Running"],
    "Branch":"Computers"
}

student2 = {
    "name":"Johny",
    "lastname":"Smithy",
    "Profession":"Dentist",
    "Age":26,
    "Hobbies": ["Swimming", "Rock Climbing", "Running"],
    "Branch":"Computers"
}
student3 = {
    "name":"Memis",
    "lastname":"Cetinkaya",
    "Profession":"Devops",
    "Age":26,
    "Hobbies": ["Swimming", "Cycling"],
    "Branch":"Computers"
}

students={
    "student1":student1,
    "student2":student2,
    "student3":student3
}


print(students)

# print(student.get('name')) #get name separately
# print(student['name'])
# print(student['lastname'])
# print(student['Profession'])
# print(student['Age'])
# print(student['Hobbies'])
# print(student['Branch'])

print("Student 1 {}".format(students['student1'])) #print students separately
print("Student 2 {}".format(students['student2']))
print("Student 3 {}".format(students['student3']))

print(len(students)) #check the length of dictionery

#check some conditions
if "student4" in students:
    print("Student is there")
else:
    print("Students is not there")

#TO REMOVE SOME ITEM-STUDENT
students.pop('student1')
print(students)
