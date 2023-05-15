def div(num1,num2):
    return num1/num2

num1 = int(input("Enter num1...:"))
num2 = int(input("Enter num2...:"))

try:
    print(div(num1,num2))
except Exception as e:
    print(f"Something Happened {e}".format(e))
else:
    print("Execute this block when there is no error")
finally:
    print("This block gets executed regardless of the exception")
####################################################