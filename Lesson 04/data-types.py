import math

# String Data Type

# Literal Assignment
firstName = "Arthur"
lastName = "Ramos"

print(type(firstName))
print(type(firstName) == str)
print(isinstance(firstName, str))

# Constructor Function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
fullName = firstName + " " + lastName
print(fullName)

fullName += "!"
print(fullName)

# Casting a number to a string
decade = str(1990)
print(type(decade))
print(decade)

statement = "I miss the " + decade + "s!"
print(statement)

# Multiple Lines

multiLine = """
Hey, what's up???

I was just checkin', my dude...

                                    All good?
"""

print(multiLine)

# String Methods
print(firstName)
print(firstName.lower())  # Converts to lowercase
print(firstName.upper())  # Converts to uppercase
print(firstName.capitalize())  # Converts the first letter to uppercase

print(multiLine.title())
print(multiLine.replace("dude", "bro"))  # Replaces the 1st args with the 2nd args

print(len(multiLine))
print(len(multiLine.strip()))  # Removes white spaces
print(multiLine.strip())

# Build a Menu
title = "menu".upper().center(
    20, "="
)  # Creates padding on both sides and put the string to the center
coffee = "coffee".ljust(16, ".") + "$1".rjust(4)
muffin = "muffin".ljust(16, ".") + "$3".rjust(4)
cookies = "cookies".ljust(16, ".") + "$3".rjust(4)
print(title)
print(coffee.capitalize())
print(muffin.capitalize())
print(cookies.capitalize())

print("")

# String Index Values
print(firstName[0])
print(firstName[2:])
print(firstName[1:-1])

# Boolean String Methods
print(firstName.startswith("A"))
print(firstName.startswith("a"))
print(firstName.casefold().startswith("a"))

# Boolean Data Type
myValue = True

# Numeric Data Types
# Integer Types
price = 100
bestPrice = int(80)

# Float Types
gpa = 4.24
y = float(4.20)
print(type(gpa))

# Complex Types
compValue = 5 + 3j
print(type(compValue))
print(compValue.real)
print(compValue.imag)

# Built-in Functions for Numbers

print(abs(gpa))
print(round(gpa))  # Output is 4
print(round(gpa, 1))  # Output is 4.2

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a String to a Number

zipCode = "101"
zipValue = int(zipCode)
print(type(zipValue))
