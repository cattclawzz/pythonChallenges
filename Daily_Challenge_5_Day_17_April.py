###########################
# 5Y Daily Challenge 5
###########################
"""
Challenge 1 - Pattern Focus: Simple if/else Decision
========================
Ciarán is checking if a number is positive or negative.
Write a program that:
(a) Asks the user to enter a number
(b) Prints "Positive!" if the number is greater than or equal to 0
(c) Prints "Negative!" if the number is less than 0

Hint: Convert the input to a float first.
      Use if/else with a single condition: if number >= 0

                Expected output (if user enters 7):
                Positive!

                Expected output (if user enters -3):
                Negative!
========================
"""

print("Positive!" if int(input("Enter a number: ")) >= 0 else "Negative!")
print()

"""
Challenge 2 - Pattern Focus: if/else with Calculation
========================
Aoife is buying cinema tickets.
Adult tickets cost €12.50 and child tickets cost €7.00.
Write a program that:
(a) Asks the user for their age
(b) If the user is 18 or older, prints their ticket price as an adult
(c) Otherwise, prints their ticket price as a child
(d) Include the word "Adult" or "Child" in the output

Hint: Use int() to convert the age input.
      Use an f-string to display the price, e.g. f"Adult ticket: €12.50"

                Expected output (if user enters 20):
                Adult ticket: €12.50

                Expected output (if user enters 14):
                Child ticket: €7.00
========================
"""

print("Adult ticket: €12.50" if int(input("Age? ")) >= 18 else "Child ticket: €7.00")
print()

"""
Challenge 3 - Pattern Focus: if/else with Multiple Inputs
========================
Seán and Niamh are comparing their test scores.
Write a program that:
(a) Asks the user for Seán's score
(b) Asks the user for Niamh's score
(c) If Seán's score is higher, print "Seán wins!"
(d) If Niamh's score is higher, print "Niamh wins!"
(e) If the scores are equal, print "It's a draw!"

Hint: You'll need three branches — if, elif, else.
      Convert both scores to int() before comparing.

                Expected output (if Seán=78, Niamh=65):
                Seán wins!

                Expected output (if Seán=50, Niamh=50):
                It's a draw!
========================
"""

scores = {
    int(input("Sean's score? ")): "Seán",
    int(input("Niamh's score? ")): "Niamh"
}

print("It's a draw!" if all(i == list(scores.keys())[0] for i in list(scores.keys())) else f"{scores[max(scores.keys())]} wins!")
