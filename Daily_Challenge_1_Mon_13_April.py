###########################
# 5Y Daily Challenge 1
###########################
"""
Challenge 1 - Pattern Focus: Storing and Displaying Values
========================
Ciarán is filling out his school profile.
Write a program that:
(a) Stores his name, age, and town in three variables
(b) Prints each one on its own line

Hint: Use a variable for each piece of information.
      To print a variable, just write: print(variable_name)

            Expected output:
                Ciarán
                16
                Galway
========================
"""

name, age, town = input("name: "), int(input("age: ")), input("town: ")
print(f"{name} \n{age} \n{town}")

print()
"""
Challenge 2 - Pattern Focus: Storing and Displaying Values
========================
Aoife wants her school ID card printed to the screen.
Write a program that:
(a) Stores her name, year, and school name in variables
(b) Prints all three on one line, separated by a space

Hint: You can print multiple values in one print() by separating them with commas:
      print(name, year, school)

            Expected output:
                Aoife 5 Coláiste na hAbhann
========================
"""

name, year, schoolName = input("name: "), int(input("year: ")), input("school name: ")
print(f"{name} {year} {schoolName}")

print()
"""
Challenge 3 - Pattern Focus: Storing and Displaying Values
========================
Seán is entering a talent show. Store his details and
display them as a neatly labelled profile card.

Write a program that:
(a) Stores his name, act (e.g. "Guitar"), and hometown in variables
(b) Prints each detail on its own line with a label in front of it

Hint: You can join a label and a variable using an f-string:
      print(f"Name: {name}")
      Or using +, but the variable must be a string:
      print("Name: " + name)

            Expected output:
                Name: Seán
                Act: Guitar
                Hometown: Cork
========================
"""

name, act, hometown = input("Name: "), input("Act: "), input("Hometown: ")
print(f"Name: {name} \nAct: {act} \nHometown: {hometown}")
