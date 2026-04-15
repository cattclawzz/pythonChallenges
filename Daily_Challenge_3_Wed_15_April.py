###########################
# 5Y Daily Challenge 3
###########################
"""
Challenge 1 - Pattern Focus: Input + int()
========================
You're running the school tuck shop for the day.
A student comes in and buys a few rolls.

Write a program that:
(a) Asks how many rolls the student is buying
(b) Asks the price of one roll in cent (whole number)
(c) Calculates and prints the total cost in cent

Hint: Any number typed by the user comes in as text — use int() to convert it:
      rolls = int(input("How many rolls? "))

                Expected output:
                How many rolls did you buy? 3
                Price per roll (cent): 85
                Total cost: 255 cent
========================
"""

def price(quan, price):
    return price * quan

rolls = int(input("How many rolls? "))
cost = int(input("Price per roll (cent): "))
print(f"Total cost: {price(rolls, cost)} cent")

print()

"""
Challenge 2 - Pattern Focus: Input + Arithmetic + round()
========================
Two students just got their results back for two class tests.
Each test was out of 30, giving a total of 60 marks.

Write a program that:
(a) Asks the student to enter their mark for Test 1 and Test 2
(b) Calculates their total mark out of 60
(c) Calculates their percentage and rounds it to 1 decimal place
(d) Prints the total and percentage

Hint: To get a percentage: divide the total by 60, multiply by 100.
      Use round() to tidy up the answer:
      percentage = round((total / 60) * 100, 1)

                Expected output:
                Enter Test 1 mark: 24
                Enter Test 2 mark: 21
                Total: 45/60
                Percentage: 75.0%
========================
"""

marks = [int(input(f"Enter Test {i} mark: ")) for i in range(1,3)]
print(f"Total: {sum(marks)}/60 \nPercentage: {int(round((sum(marks) / 60) * 100, 1))}%")

print()

"""
Challenge 3 - Pattern Focus: Input + int() + float() + round()
========================
You're building an ordering system for a local chipper.
The program should take the customer's name and work out their bill.

Write a program that:
(a) Asks for the customer's name
(b) Asks how many items they're ordering (whole number)
(c) Asks the price per item in euro (can include cent, e.g. 4.50)
(d) Calculates the total bill, rounded to 2 decimal places
(e) Prints a receipt showing the name, number of items, and total

Hint: Use int() for the number of items and float() for the price:
      items = int(input("How many items? "))
      price = float(input("Price per item (€): "))

                Expected output:
                Customer name: Aoife
                How many items? 3
                Price per item (€): 4.50
                ---
                Order for: Aoife
                Items ordered: 3
                Total bill: €13.5
========================
"""

name = input("Customer name: ")
items = int(input("How many items? "))
cost = float(input("Price per item (€): "))

print(f"--- \nOrder for: {name} \nItems ordered: {items} \nTotal bill: €{cost*items:.2F}")

