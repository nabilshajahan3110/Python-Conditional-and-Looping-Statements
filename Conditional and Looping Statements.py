# CONDITIONAL AND LOOPING STATEMENTS

# Created by NABIL SHAJAHAN

# 2. A certain cinema currently sells tickets for a full price of 6 pounds,
# but always sells tickets for half price to people who are less than 16 years old,
# and for a third of the price for people who are 60 years old or more.
# An example run of the program (numbers in bold are typed in by the user)
# Enter your age: 63
# Your ticket costs £2.00


age = int(input("Enter your age: "))

if age < 16:
    print("Your ticket costs GBP 3.00")
elif age < 60:
    print("Your ticket costs GBP 6.00")
else:
    print("Your ticket costs GBP 2.00")


# 4. Write a Python program to receive 3 numbers from the user and print the greatest among them.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("The greatest number amongst the entered values is the first number",a)
elif b > a and b > c:
    print("The greatest number amongst the entered values is the second number", b)
elif c > a and c > b:
    print("The greatest number amongst the entered values is the third number", c)


# 5. Find the factorial of a given number using loops(note the number is received from the user)

num1 = int(input("Enter the number to calculate factorial: "))

factorial = 1

if num1 < 0:
    print("Factorials do not exist for negative numbers")
elif num1 == 0:
    print("Factorial of 0 is 1")
else:
    for i in range (1,num1+1):
        factorial *= i
    print(f"The factorial for {num1} is {factorial}.")


# 6. Reverse a number using while loop

num4 = int(input("Enter the number: "))

r = 0

while num4 > 0:
    d = num4 % 10
    r = r * 10 + d
    num4 = num4 // 10
print(f"The reverse of the entered number is {r}")


# 7. Finding the multiples of a number using loop

num2 = int(input("Enter the number: "))
num3 = int(input("Enter number of multiples you need: "))

print(f"The first {num3} multiples of {num2} are: ")
for i in range(1,num3+1):
    print(num2 * i, end=" ")


# 8. Write a program to print the inputted value as it is and break the loop if the value is 'done'.
# Example run of the program
# :hello there
# hello there
# :finished
# finished
# :done
# Done

# value = input("Enter a value: ")
#
# if value == 'done':
#     print("Breaking the loop")
# print(f"The value you entered is {value}")

while True:
    word = input("Enter a word (type 'done' to end): ")
    print(f"The word you entered is {word}")
    if word == 'done' or word == 'Done' or word == 'DONE':
        break


# 9. Write a program that prints the numbers from 1 to 15.
# But for multiples of three print "Fizz" instead of the number and for the multiple of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz"

for i in range (1,16):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# 10. Write a program to print the following pattern:
#
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j, end='')
    print()