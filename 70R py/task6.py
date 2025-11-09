n = int(input("Enter a number: "))
num_digits = len(str(n))
sum_of_powers = 0
for digit in str(n):
    sum_of_powers += int(digit) ** num_digits
if sum_of_powers == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")



n = int(input("Enter a number: "))
print("Factors of", n, "are:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")



n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial of", n, "is:", fact)




n = int(input("Enter a number: "))
count = 0
for digit in str(n):
    count += 1
print("Number of digits in", n, "is:", count)
