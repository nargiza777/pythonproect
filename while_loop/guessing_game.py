from random import randrange
guess=-1 #we initialize that number


#computer will generate a random number from 1 to 10
number = randrange(10) #it randomly takes the number from  1 to 10
#user will guess that number until user can find the number
while guess!=number:
    guess=int(input("Guess a number...:"))
#once user finds the number
    if number == guess:
    #print you guessed the number and then print the number computer guessed
        print(f"You have guessed {number} it's {number}".format(number,guess))
        break
    #if ti's wrong print the number that you guessed and try again.
    else:
        print(f"You have guessed {guess}, try again".format(guess))
