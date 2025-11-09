n = int(input("Enter a number: "))
temp = n
sum = 0
while temp > 0:
    digit = temp % 10
    if digit == 2 or digit == 3 or digit == 5 or digit == 7:
        sum += digit
    temp //= 10
print("Sum of prime digits in", n, "=",sum)





n = int(input("Enter a number: "))
temp = n
sum = 0
while temp > 0:
    digit = temp % 10
    temp//= 10
    if digit % 2 == 0:
        sum += digit
print("Sum of even digits in", n, "=",sum)





n = int(input("Enter a number: "))
temp = n
sum = 0
while temp > 0:
    digit = temp % 10
    if digit % 2 == 0:
        sum += digit
    temp //= 10
if sum % 2 == 0:
    print("Even")
else:
    print("Odd")
