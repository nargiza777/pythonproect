lst_courses = ['History','Math','Physics','CompSci','CompSci','CompSci','Physics',1,2,3,4,['1',3,'CARS']]
#in lists assignments take the reference of the object.
lst2=lst_courses
lst3=lst_courses
copied_list = lst_courses [0:4]
print(copied_list)
print(lst_courses)
print(lst2)
lst2.append("Race Car")
lst3.remove('CompSci')
print(lst_courses)
print(lst2)
print(lst3)

print(id(lst_courses))
print(id(lst2))
print(id(lst3))
print(id(copied_list))
#int,str,floats

#for int,str,float assignments takes the value of the variable
num1=10
num2=num1
num1=5

print(num1)
print(num2)

print(copied_list)

copied_list[0]='Bike'
print(copied_list)

