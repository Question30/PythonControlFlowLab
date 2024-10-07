'''
1. Write a program that declares 1 variable x, and then assigns 7 to it. Write an if statement to print out “Less than 10” if x is less than 10. Change x to equal 15, and notice the result (console should not display anything).
'''
x = 10

if x < 10:
    print("Less than 10")

'''
2. Write a program that declares 1 variable x, and then assigns 7 to it. Write an if-else statement that prints out “Less than 10” if x is less than 10, and “Greater than 10” if x is greater than 10. Change x to 15 and notice the result. 
'''
x = 15

if x < 10:
    print("Less than 10")
elif x > 10:
    print("Greater than 10")

'''
3. Write a program that declares 1 variable x, and then assigns 15 to it. Write an if...elif...else statement that prints out “Less than 10” if x is less than 10; “Between 10 and 20” if x is greater than 10 but less than 
'''
x = 50

if x < 10:
    print("Less than 10")
elif x > 10 and x < 20:
    print("Between 10 and 20")
else:
    print("Greater than or equal to 20")

'''
 4. Write a program that declares 1 variable x, and then assigns 15 to it. Write an if-else statement that prints “Out of range” if the number is less than 10 or greater than 20 and prints “In range” if the number is between 10 and 20 (including equal to 10 or 20). Change x to 5 and notice the result. 
'''
x = 5
if x < 10 or  x > 20:
    print("Out of range")
else:
    print("In range")

'''
5. Write a program that uses if...elif...else statements to print out grades A, B, C, D, F, according to the following criteria:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: <60
Use the input() function  to accept a number score from the user to determine the letter grade. Print out “Score out of range” if the score is less than 0 or greater than 100.
'''

number = int(input("Enter a number"))

if number < 0 or number > 100:
    print("Out of range")
elif number >= 90 and number <= 100:
    print("A")
elif number >= 80 and number < 90:
    print("B")
elif number >= 70 and number < 80:
    print("C")
elif number >= 60 and number < 70:
    print("D")
else:
    print("F")

'''
 6. Create a program that lets the users input their filing status and income. Display how much tax the user would have to pay according to status and income.
The U.S. federal personal income tax is calculated based on the filing status and taxable income. 
There are four filing statuses: Single, Married Filing Jointly, Married Filing Separately, and Head of Household. 
The tax rates for 2009 are shown below.

'''
def print_tax_rate(status, income):
    result = 0
    arr = get_status_arr(status)

    if income >= 0 and income <= arr[0]:
        result = income * 0.10
    elif income > arr[0] and income <= arr[1]:
        result = income * 0.15
    elif income > arr[1] and income <= arr[2]:
        result = income * 0.25
    elif income > arr[2] and income <= arr[3]:
        result = income * 0.28
    elif income > arr[3] and income <= arr[4]:
        result = income * 0.33
    elif income > arr[4]:
        result = income * 0.35
    else:
        print("Out of range")
        result = 0

    return result


def get_status_arr(status):
    single_arr = [8350, 82250, 171550, 372950]
    jointly_arr = [16700, 67900, 137050, 208850, 372950]
    separate_arr = [8350, 33950, 68525, 104425, 186475]
    head_arr = [11950, 45500, 117450, 190200, 372950]

    if status == "single":
        return single_arr
    elif status == "jointly":
        return jointly_arr
    elif status == "separate":
        return separate_arr
    elif status == "head":
        return head_arr
    else:
        return None


def main():
    status = input("Enter filling status: (ex. Single, Married, Head) ").strip().lower()
    if status == "married":
        status = input("Are you filing Jointly or Separate? ").strip().lower()

    income = int(input("What is your yearly income? "))
    
    tax = print_tax_rate(status, income)
    print(f"Your tax amount is: {tax}")


if __name__ == "__main__":
    main()

