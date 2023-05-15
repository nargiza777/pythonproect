#WHILE LOOP
# counter=0

# while counter < 10:
#     print(counter)   #it will print loop forever, because counter is less than 10

counter = 0
while counter<10:
    print("The value of the counter is {}".format(counter))
    counter = counter + 1

#ANOTHER EXAMPLE
i=6
while i<6:
    print(i)
    if i==3:
        break #when i = 3 it will get out of the loop
        #continue - will continue loop even i = 3 and it will not increment +1 - it'll always be 3
    i+=1
#CONTINUE LOOP
i=6
while i<6:
    print(i)
    if i==3:
        continue
    else:
        print("is {}".format(i)) #it will NOT get out of the loop IT'S A BUG - SINCE IT NEVER STOPS
    i+=1