i=1

# while i<=4:
#     print(i)
#     i+=1

#break
while i<=4:
    if i==3:
        print("is is {}, get out of the loop".format(i))
        break  #when i=3 it gets out of the loop
    print(i)
    i+=1

#continue
i=0
while i<=4:
    i += 1
    if i==3:
        print("is is {}, get out of the loop".format(i))
        continue #it doesn't let you to go to next step, goes back to step 1(while)
    print(i) #
