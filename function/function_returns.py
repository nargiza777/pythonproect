def addition(num1,num2):
    return num1+num2

returned_value = addition(2,3)
print(returned_value)

def is_male(g):
    if g=="M":
        return True
    else:
        return False
def is_older_than18(age):
    if age>=18:
        return True
    else:
        return False

def greetings(name, lastname,title):
    return f"Hello {title} {lastname}, is your name {name}"

print(greetings("John", "Smith", "Dr"))

if addition(2,5)>=5:
    print("Greater than 5")
else:
    print("Less than 5")

print(is_male("M"))

if is_male("M"):
    print("you can take the left route")
else:
    print("you can take the right route")
name=str(input("Please enter your name>>:"))
yourage=int(input("Please enter your age..:"))

if is_older_than18(yourage):
    print(f"Deaf {name} you are welcome")
else:
    print(f"Dear {name} we can't admit you")