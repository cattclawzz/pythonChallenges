###########################
# 5Y Daily Challenge 4
###########################
"""
Challenge 1 - Pattern Focus: Simple if/else
========================
Ciarán is checking if the swimming pool in Limerick is warm enough to use.
The pool is fine if the temperature is 18 degrees or above.

Write a program that:
(a) Stores the pool temperature as a variable
(b) Prints "Pool is warm enough!" if the temperature is 18 or above
(c) Prints "Too cold for swimming!" otherwise

Hint: Use an if/else statement. The condition goes between if and the colon.
      Try: if temperature >= 18:

                Expected output (if temperature is 20):
                Pool is warm enough!

                Expected output (if temperature is 15):
                Too cold for swimming!
========================
"""

temperature = 20
print("Pool is warm enough!" if temperature >= 18 else "Too cold for swimming!")

print()
"""
Challenge 2 - Pattern Focus: if/else with Input
========================
Síofra is checking if leaving cert students have passed their mock exam.
A student passes if they score 40 or more out of 100.

Write a program that:
(a) Asks the user to enter a student's exam score
(b) Converts it to an integer
(c) Prints "Pass - well done!" if the score is 40 or above
(d) Prints "Fail - keep studying!" otherwise

Hint: Remember input() always gives you a string — use int() to convert it.
      Store it like this: score = int(input("Enter score: "))

                Expected output (if score is 67):
                Pass - well done!

                Expected output (if score is 35):
                Fail - keep studying!
========================
"""

score = int(input("Enter score: "))
print("Pass - well done!" if score >= 40 else "Fail - keep studying!")

print()
"""
Challenge 3 - Pattern Focus: if/else + Arithmetic
========================
Aoife is buying cinema tickets in Galway.
Tickets cost €9.50 each. If a group buys 4 or more tickets, they get a 10% discount.

Write a program that:
(a) Asks the user how many tickets they want to buy
(b) Calculates the total cost (tickets × €9.50)
(c) If they are buying 4 or more tickets, applies a 10% discount
(d) Prints the final total, rounded to 2 decimal places

Hint: Calculate the full price first, then check the condition.
      To apply 10% off: total = total * 0.9

                Expected output (if tickets = 5):
                Total cost: €42.75

                Expected output (if tickets = 2):
                Total cost: €19.0
========================
"""
price = 9.5
discount = 0.9
totalPrice = int(input("How many tickets do you want to buy? "))* price
print(f"Total cost: €{(totalPrice if totalPrice < (4*price) else totalPrice * discount):.2F}")
