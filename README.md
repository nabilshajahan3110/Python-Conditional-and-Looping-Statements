# Python-Conditional-and-Looping-Statements
Python exercise covering the concepts of conditional and looping statements

Created by NABIL SHAJAHAN

CONDITIONAL AND LOOPING STATEMENTS

Exercise 1
Name your file: MonthNames.py
Write a program that reads an integer value between 1 and 12 from the user and prints output the corresponding month of the year.
An example run of the program (numbers in bold are typed in by the user)
Enter the month: 3
Month 3 is March

months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

month_id = int(input("Enter the month number (1-12): "))

if 1 <= month_id <= 12:
    print(f"Month number {month_id} is {months[month_id - 1]}")
else:
    print("Invalid input! Please enter a number between 1 and 12")


 ![CL 1](https://github.com/user-attachments/assets/9642fbce-ee66-4038-95d9-e7380b17c9e1)


 ![CL 1 II](https://github.com/user-attachments/assets/16eab484-0780-4605-9c5a-7ea843d47fc8)




Exercise 2
A certain cinema currently sells tickets for a full price of 6 pounds, but always sells tickets for half price to people who are less than 16 years old, and for a third of the price for people who are 60 years old or more.
An example run of the program (numbers in bold are typed in by the user)
Enter your age: 63
Your ticket costs £2.00

age = int(input("Enter your age: "))

if age < 16:
    print("Your ticket costs GBP 3.00")
elif age < 60:
    print("Your ticket costs GBP 6.00")
else:
    print("Your ticket costs GBP 2.00")



 ![CL 2](https://github.com/user-attachments/assets/eb39ea74-eeeb-46cb-a691-666772348478)




Exercise 3
Name your file: BodyMassIndex.py
Write a program to calculate your BMI and give weight status. Body Mass Index (BMI) is an internationally used measurement to check if you are a healthy weight for your height. BMI formula accepts weight in kilograms and height in meters:
BMI= weight(kg)/height2(m2)
BMI Weight Status Categories table
BMI range - kg/m2   Category
Below 18.5                    Underweight
18.5 -24.9         Normal
25 - 29.9          Overweight
30 & Above     Obese
An example run of the program (numbers in bold are typed in by the user)
Enter your weight in (kg): 75
Enter your height in (m): 1.70
Your BMI is: 25.95
You are in the “overweight” range.

weight = float(input("Enter your weight in (kg): "))
height = float(input("Enter your height in (m): "))

bmi = weight / (height**2)

if bmi < 18.5:
    weight_status = "Underweight"
elif bmi < 24.9:
    weight_status = "Normal"
elif bmi < 29.9:
    weight_status = "Overweight"
else:
    weight_status = "Obese"

print(f"Your BMI is: {bmi:.2f}")
print(f"You are in the '{weight_status}' range")

 

![CL 3](https://github.com/user-attachments/assets/9776f926-db99-4303-9dbd-393518dd048a)




Exercise 4
Write a Python program to receive 3 numbers from the user and print the greatest among them.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("The greatest number amongst the entered values is the first number",a)
elif b > a and b > c:
    print("The greatest number amongst the entered values is the second number", b)
elif c > a and c > b:
    print("The greatest number amongst the entered values is the third number", c)



![CL 4](https://github.com/user-attachments/assets/4c6f5057-ee99-4fb5-b73a-9fc6ef8ee1da)




Exercise 5
Find the factorial of a given number using loops (note the number is received from the user)

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



![CL 5](https://github.com/user-attachments/assets/bd0b985a-6749-4c99-a974-d788fdbe97da)


![CL 5 II](https://github.com/user-attachments/assets/5bc49b7c-2ab2-437a-b167-2df1d45449c4)




Exercise 6
Reverse a number using while loop

num4 = int(input("Enter the number: "))

r = 0

while num4 > 0:
    d = num4 % 10
    r = r * 10 + d
    num4 = num4 // 10
print(f"The reverse of the entered number is {r}")



![CL 6](https://github.com/user-attachments/assets/99695dce-7ff4-4f93-8b2e-975267ce213d)




Exercise 7
Finding the multiples of a number using loop

num2 = int(input("Enter the number: "))
num3 = int(input("Enter number of multiples you need: "))

print(f"The first {num3} multiples of {num2} are: ")
for i in range(1,num3+1):
    print(num2 * i, end=" ")


![CL 7](https://github.com/user-attachments/assets/6ac49ee6-17ce-48fc-bcde-bd56881eb412)




Exercise 8
Write a program to print the inputted value as it is and break the loop if the value is 'done'.
Example run of the program
:hello there
hello there
:finished
finished
:done
Done

while True:
    word = input("Enter a word (type 'done' to end): ")
    print(f"The word you entered is {word}")
    if word == 'done' or word == 'Done' or word == 'DONE':
        break


![CL 8](https://github.com/user-attachments/assets/128c545c-b801-45a0-aadf-2cde6cd7389f)




Exercise 9
Write a program that prints the numbers from 1 to 15. But for multiples of three print "Fizz" instead of the number and for the multiple of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"

for i in range (1,16):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

 

![CL 9](https://github.com/user-attachments/assets/985c5838-8f2a-4127-ac65-83f3c0d6a77a)

![CL 9 II](https://github.com/user-attachments/assets/68cbec41-55a3-4a3c-a498-28224c7196bd)




Exercise 10
Write a program to print the following pattern:

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j, end='')
    print()



![CL 10](https://github.com/user-attachments/assets/85cc1fb7-bb77-4764-bb38-8d7b11dc157b)




 
