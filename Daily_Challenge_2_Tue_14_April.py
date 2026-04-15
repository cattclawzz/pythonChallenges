###########################
# 5Y Daily Challenge 2
###########################
"""
Challenge 1 - Pattern Focus: Input + Arithmetic
========================
Ciarán is saving up his pocket money.
Write a program that:
(a) Asks the user how much money they already have
(b) Asks how much more they will save this week
(c) Prints the total amount they will have

Hint: Use input() to get each value and convert with float().
      Then just add the two numbers together and print the result.

                Expected output:
                How much money do you have? 12.50
                How much will you save this week? 5.00
                You will have €17.50 in total.
========================
"""

def totalMoney(current, add):
    return current + add
print(f"You will have €{totalMoney(float(input('How much money do you have? ')), float(input('How much will you save this week? '))):.2f} in total.")

print()
"""
Challenge 2 - Pattern Focus: Input + Arithmetic
========================
Aoife is buying rolls for the school lunch order.
Write a program that:
(a) Asks how many rolls she wants to buy
(b) Asks the price of one roll in cent
(c) Calculates the total cost in euro
(d) Prints the total cost

Hint: Total cost = number of rolls × price per roll
      To convert cent to euro, divide by 100.
      Use int() for the number of rolls and float() for the price.

                Expected output:
                How many rolls? 6
                Price per roll (cent)? 85
                Total cost: €5.10
========================
"""

def price(quan, price):
    return price * quan
print(f"Total cost: €{price(int(input('How many rolls? ')), float(input('Price per roll (cent)? '))/100):.2f}")

print()
"""
Challenge 3 - Pattern Focus: Input + Arithmetic + Variables
========================
Seán runs a small tuck shop after school.
Write a program that:
(a) Asks for the name of the item being sold
(b) Asks for the price of one item
(c) Asks how many items were sold today
(d) Calculates the total money made
(e) Prints a summary showing the item name, number sold, and total earned

Hint: Store each input in its own descriptive variable.
      Multiply the price by the quantity to get the total.
      Use an f-string to print a neat summary at the end.

                Expected output:
                Item name: Crisps
                Price per item: 1.20
                How many sold today? 15
                --- Tuck Shop Summary ---
                Item: Crisps
                Sold: 15
                Total earned: €18.00
========================
"""
item = input('Item name: ')
cost = float(input('Price per item: '))
sold = int(input("How many sold today? "))
print(f"--- Tuck Shop Summary --- \nItem: {item} \nSold: {sold} \nTotal earned: €{price(sold, cost):.2f}")