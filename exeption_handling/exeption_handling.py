num1=10
num2=0

try:
    num1/num2
except:
    print("divided by zero")
    num2=2
finally: #regardless of result it always executes the code
    print(num1/num2)