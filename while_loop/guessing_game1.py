from random import randrange
guess = 0
#ask how many users will play this game
number_of_players = int(input("How many users will play...:"))
user_names=[]
#keep the number of users in a list
winner=""

for user in range(number_of_players):
#ask name of the users one by one
    user_names.append(input("Enter the user name...:"))
number = randrange(1,10)
print("Users {} are playing".format(user_names))
while guess!=number:
    for index, name in enumerate(user_names):
        print(f"it's {index} user {name}\'s turn".format(index,name))
        guess=int(input("Guess a number"))
        if number == guess:
            print(f"{name} guessed {guess} it's {number}".format(name, guess, number))
            winner=user_names[index]
            break
        else:
            print("{name} guessed, guess again".format(name,number))
print("winner is {}".format(winner))
#make the users guess the numbers
#if user guesses the number
#print the winning user on the screen
#else make the other user guess the game