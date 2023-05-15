tuple_1=('History','Math','Physics','CompSci',1,3,3.14,['a','b','c'])

tuple_2=tuple_1

print(id(tuple_2))
print(id(tuple_1))
print(tuple_1[0])
print(tuple_1[1])
print(tuple_1[3])

print('Math' in tuple_1)
print('Cars' in tuple_1)

print(tuple_1)

for element in tuple_1:
    print("The type of element is {}".format(type(element)))