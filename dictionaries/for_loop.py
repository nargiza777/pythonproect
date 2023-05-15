list1 = ["apple", "orange", "kiwi", "grapes"]


# for k,v in  enumerate(list1): #GETS INDEX NUMBERS FOR ITEMS and PRINTS THEM TOGETHER
#     print("index of list is {} {}".format(k,v))

print(dir(enumerate))
for k,v in  enumerate(list1,start=1): #STARTS ENUMERATION WITH 1 FOR ITEMS and PRINTS THEM TOGETHER
    print("index of list is {} {}".format(k,v))

for k in range(len(list1)):
    print(" {} {}".format(k, list1[k])) #THIS IS ANOTHER WAY OF PRINTING ITEM WIN AN INDEX


#COMPREHENSION
squares = [i * i for i in range(10)] #IT WILL PRINT SQUARES(КВАДРАТНОЕ ЗНАЧЕНИЕ)
print(squares)

input_from_user = input("Enter a fruit name..:")
if input_from_user in list1: