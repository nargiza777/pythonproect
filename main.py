lst_courses = ['History','Math','Physics','CompSci','CompSci','CompSci','Physics']
print(lst_courses)
lst1_courses = ['Driving','Public Speaking']
print(lst1_courses)
lst_courses.extend(lst1_courses) #extend - adds as new items
print("#####This is after the extention###########")
print(lst1_courses)
print(lst_courses)
#
lst_courses.append(lst1_courses) #append - adds as a new list(if it was saved lst1_courses as a list
print(lst_courses)
# print(lst_courses)
# print(lst_courses[0])
# print(lst_courses[1])
# print(lst_courses[3])
lst_courses.append('Art')
print(lst_courses)
# lst_courses.insert(0,'Music')
# print(lst_courses)
# lst_courses.insert(3,'Piano')
# print(lst_courses)
# print(['History','Math','Physics','CompSci','CompSci','CompSci','Physics'].count('CompSci'))
# print(lst_courses.count('CompSci'))
# print(lst1_courses.__len__())

print(lst_courses.__len__())
for elements in lst_courses:
    print("These are the elements of the list...{}".format(elements))

# print("################")
# print(lst_courses.count('CompSci'))
# print(lst_courses.count('Physics'))
# poped=lst_courses.pop()
# poped1=lst_courses.pop()
# print(poped)
lst_courses.remove('CompSci')
print(lst_courses)
# lst_courses.remove('CompSci')
# print(lst_courses)
# lst_courses.remove('CompSci')
# print(lst_courses)

# myList = ['History','Math','Physics','CompSci','CompSci','CompSci','Physics']
# valueToBeRemoved = 'CompSci'
#
# myList = [value for value in myList if value != valueToBeRemoved]
# myList
# print(myList)
#
# courses_str = ','.join(myList)
# courses_str1 = '-'.join(myList)
#
# print(courses_str)
# print(courses_str1)

# myList = [value for value in myList if value != valueToBeRemoved] #removed CompSci from the list
# print(myList)
#
# #TO CONVERT INTO A STRING
# courses_str = ','.join(myList)
# courses_str1 = '-'.join(myList) #prints list as a string separated by dash
# print(courses_str)
# print(courses_str1)
