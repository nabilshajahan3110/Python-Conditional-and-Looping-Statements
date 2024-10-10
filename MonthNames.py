# 1. Write a program that reads an integer value between 1 and 12 from the user and prints output
# the corresponding month of the year.
# An example run of the program (numbers in bold are typed in by the user)
# Enter the month: 3
# Month 3 is March

months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

month_id = int(input("Enter the month number (1-12): "))

if 1 <= month_id <= 12:
    print(f"Month number {month_id} is {months[month_id - 1]}")
else:
    print("Invalid input! Please enter a number between 1 and 12")