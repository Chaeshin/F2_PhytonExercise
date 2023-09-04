num = int(input("Please enter number: "))
count = 0
min = 9
max = 0
while num > 0:
    val = num % 10
    count += 1
    if val < min:
        min = val
    if val > max:
        max = val
    num //= 10
print("Number of digits in the given number is:",count)
print("Smallest number is:",min)
print("Highest number is:",max)