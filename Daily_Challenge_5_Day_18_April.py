###########################
# 5Y Daily Challenge 6
###########################
"""
Challenge 1 - Pattern Focus: if/elif/else Multiple Choices
========================
Fionn is grading a quiz out of 10.
Write a program that:
(a) Asks the user for their quiz score
(b) Prints "Excellent!" if the score is 9 or 10
(c) Prints "Good!" if the score is 6, 7, or 8
(d) Prints "Keep Practising!" if the score is 5 or below

Hint: Use int() to convert the score.
      You need three branches: if, elif, else.
      Think about what condition each branch needs.

                Expected output (if user enters 10):
                Excellent!

                Expected output (if user enters 7):
                Good!

                Expected output (if user enters 3):
                Keep Practising!
========================
"""

score = int(input("Score? "))
print(["Keep Practising!", "Good!", "Excellent!", "Keep Practising!"][(score//3)-1])

"""
Challenge 2 - Pattern Focus: if/elif/else with Multiple Outputs
========================
Róisín is checking the weather to decide what to wear.
Write a program that:
(a) Asks the user for the temperature in degrees Celsius
(b) If the temperature is 20 or above, print "Wear a t-shirt!"
(c) If the temperature is between 10 and 19 (inclusive), print "Bring a jacket!"
(d) If the temperature is below 10, print "Wrap up warm!"
(e) Also print the temperature back to the user in each message

Hint: Use float() to convert the temperature.
      Use an f-string, e.g. f"It's 15.0°C — Bring a jacket!"

                Expected output (if user enters 22):
                It's 22.0°C — Wear a t-shirt!

                Expected output (if user enters 15):
                It's 15.0°C — Bring a jacket!

                Expected output (if user enters 4):
                It's 4.0°C — Wrap up warm!
========================
"""
i = int(input("temp: "))
print(["Wrap up warm!", "Bring a jacket!", "Wear a t-shirt!"][2 if int(str(i).zfill(2)[:-1]) >= 2 else int(str(i).zfill(2)[:-1])])

"""
Challenge 3 - Pattern Focus: if/elif/else + Arithmetic
========================
Caoilfhinn works at a car park in town.
The parking charges are:
  - Up to 1 hour:    €2.00
  - 1 to 3 hours:    €5.00
  - More than 3 hours: €10.00

Write a program that:
(a) Asks the user how many hours they parked
(b) Calculates and prints the correct charge
(c) If the user enters 0 or less, print "Invalid entry"

Hint: Use float() for the hours.
      Check the invalid entry first — handle it before the normal cases.
      Use an f-string to display the charge: f"Parking charge: €2.00"

                Expected output (if user enters 0.5):
                Parking charge: €2.00

                Expected output (if user enters 2):
                Parking charge: €5.00

                Expected output (if user enters 4):
                Parking charge: €10.00

                Expected output (if user enters -1):
                Invalid entry
========================
"""
