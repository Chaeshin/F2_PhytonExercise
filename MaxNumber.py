max = 0

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if(num1 > max):
    max = num1
if(num2 > max):
    max = num2
if(num3 > max):
    max = num3

print("Max number is ", max)
