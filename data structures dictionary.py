logic building questions
#1. positive, negative, zero
num = int(input("Enter your number"))
if num > 0:
    print("POSITIVE")
elif num < 0:
    print("NEGATIVE")
else:
    print("ZERO")
#2. odd or even
if num%2==0:
    print("even")
else:
    print("odd")
#3. last digit
a=int(input("enter first number: "))
b=int(input("enter second number: "))
if a%10 == b%10:
    print("True")
else:
    print( False)
#4. number 1 to 10
for i in range(1,11):
    print (i)
#5. even number between 23 and 57
for i in range (23, 57):
    if i%2==0:
        print(i)
#6. prime numbers
num = int(input("Enter a number: "))

count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")
#7. prime numbers between 10 and 99
for num in range(10, 100):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num, end=" ")
        break
#8. sum of all digits
q= input("Enter a number")
total = 0
for digit in q:
    total+=int(digit)
print("sum of digits:", total)
#9. reverse
r= input("enter the number")
reverse = r[::-1]
print("reversed string:" , reverse)
#10. palindrome
s= input("enter a value")
if s==s[::-1]:
    print("is a palindrome")
else:
    print("is not a palindrome")