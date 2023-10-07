# Loops

# value = 1
# while value <= 10:
#     print(value)
#     value += 1

print("")

names = ["Arthur", "Aldrin", "Ramos"]
actions = ["codes", "eats", "sleeps"]

for name in names:
    for action in actions:
        print(name + " " + action + ".")

# for x in names:
#     print(x)

# for x in names:
#     if x == "Aldrin":
#         break
#     print(x)

# for x in names:
#     if x == "Aldrin":
#         continue
#     print(x)

# for x in range(4):
#     print(x)

for x in range(0, 110, 10):
    print(x)
else:
    print("Good thing that's over!")
