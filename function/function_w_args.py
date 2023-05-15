def addition(num1=5,num2=2):
    return num1+num2

print(addition(1,2))

def sumation(*args):
    print(type(args))
    print(args)
    total=0
    for item in args:
        #total=total+item
        total+=item
    return total
print(sumation(1,2,3,4,5,6,7))

def print_arguments(*names):
    return (name for name in names)

def return_many_args(*names):
    for name in names:
        print(f"{name}")

print(print_arguments("Memis", "Mike", "Jake"))

return_many_args("Memis","Hello","Mello")
print_arguments("Marry","Gary","harry")
print(print_arguments("Marry","Gary","harry")) #print the output
output=print_arguments("Marry","Gary","harry")
print(output)