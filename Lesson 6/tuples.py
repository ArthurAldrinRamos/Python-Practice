# Tuples are similar to lists.. the difference is, you can't change tuples

myTuple = tuple(("Arthur", 25, True))
anotherTuple = (1, 5, 2, 6, 5, 5)

print(myTuple)
print(anotherTuple)

copyTuple = list(myTuple)  # You can copy a tuple to another list by unpacking it..
copyTuple.append("Kekw")

print(copyTuple)
print(anotherTuple.count(5))  # Counts the instance of the argument inserted
